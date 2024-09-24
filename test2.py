import sys
import serial
import pyvisa
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PySide6 import QtCore, QtGui, QtUiTools, QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QVBoxLayout, QWidget, QGraphicsScene, QGraphicsProxyWidget
from PySide6.QtCore import Qt, QTimer, Signal, Slot, QThread, Signal
from ui_form import Ui_main_widget  
from RsInstrument import RsInstrument
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

import matplotlib.animation as animation
from collections import deque
from scipy.fft import fft, fftfreq

import threading


def loadUiWidget(uifilename, parent=None):
    loader = QtUiTools.QUiLoader()
    uifile = QtCore.QFile(uifilename)
       
    uifile.open(QtCore.QFile.ReadOnly)
    
    try:
        ui = loader.load(uifile, parent)
    except Exception as e:
        print(f"Failed to load UI: {e}")
        ui = None
    finally:
        uifile.close()
    return ui

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = loadUiWidget("ui/form.ui", self)
        if self.ui:
            self.setupUi()
            self.list_all_widgets() ## debug only...lists all available objects in the UI
        else:
            print("Failed to load UI.")
            
    def list_all_widgets(self):    ### support script to list all the available objects in UI
        # Get all child widgets of any type
        all_widgets = self.ui.findChildren(QtWidgets.QWidget)

        # Print the object names and their types
        for widget in all_widgets:
            print(f"Widget: {widget.objectName()}, Type: {type(widget).__name__}")
            
    def setupUi(self):
        #############################################################################################
        ##   initializations                                                                       ##
        #############################################################################################
        
        # output message settings
        self.ui.output_message.setReadOnly(True) # setting the terminal to read only
        self.message_id = 1
        
        #resource manager settings
        self.rm = pyvisa.ResourceManager()
        
        # logos addition
        self.logo_scene = QGraphicsScene()
        self.ui.logo_space.setScene(self.logo_scene)
        self.logo = QtGui.QPixmap()
        self.logo.load("livmats.jpg")
        self.logo_scene.addPixmap(self.logo)
        self.ui.logo_space.fitInView(self.logo_scene.sceneRect(), Qt.KeepAspectRatio)

        self.imtek_logo_scene = QGraphicsScene()
        self.ui.imtek_logo.setScene(self.imtek_logo_scene)
        self.imtek_logo = QtGui.QPixmap()
        self.imtek_logo.load("logo_imtek.jpg")
        self.imtek_logo_scene.addPixmap(self.imtek_logo)
        self.ui.imtek_logo.fitInView(self.imtek_logo_scene.sceneRect())
        
        #############################################################################################
        ##   connections to GUI elements                                                           ##
        #############################################################################################
        self.ui.identify_res_button.clicked.connect(self.identify_and_print_devices) # resource identification button
        self.ui.fun_save_button.clicked.connect(self.save_function_generator_config) # function generator configuration save button
        self.ui.fun_start_button.clicked.connect(self.send_waveform_to_fun) # send waveform to function generator
        self.ui.fun_stop_button.clicked.connect(self.stop_fun_generator) # stop the output of function generator
        self.ui.scope_config_save_button.clicked.connect(self.save_scope_config) # oscilloscope config save button
        self.ui.accel_config_save_button.clicked.connect(self.accel_save) # accelerometer configuration save button
        self.ui.scope_fetch_button.clicked.connect(self.fetch_and_update_scope_data) # oscilloscope data fetch button
        self.ui.accel_fetch_button.clicked.connect(self.start_acquisition)
        self.ui.accel_disconnect_button.clicked.connect(self.stop_acquisition)
        self.ui.accel_save_button.clicked.connect(self.save_data_to_excel)
        
    def identify_and_print_devices(self):
        resources = self.rm.list_resources()
        resources = list(set(resources))  # Eliminate duplicates
        
        # Clear the table before populating it
        self.ui.connected_devices_table.clearContents()
        self.ui.connected_devices_table.setRowCount(len(resources))
        self.ui.connected_devices_table.setColumnCount(2)
        self.ui.connected_devices_table.setHorizontalHeaderLabels(["Resource ID", "Resource Identification"])
        self.ui.connected_devices_table.setColumnWidth(0, 200)

        # Set the second column to take up the remaining space
        self.ui.connected_devices_table.horizontalHeader().setStretchLastSection(True)

        identified_resources = []

        for resource in resources:
            close_resource = True
            try:
                self.instrument = self.rm.open_resource(resource)
                idn_string = self.instrument.query("*IDN?")
                if idn_string.strip():  # Ensure IDN string is not empty
                    identified_resources.append((resource, idn_string))
                    close_resource = False
            
            except Exception as e:
                print(f"Error with resource {resource}: {str(e)}")
            
            finally:
                if close_resource:
                    try:
                        self.instrument.close()
                    except Exception as e:
                        self.print_message_to_output(f"Failed to close resource {resource}: {str(e)}")

        if not identified_resources:
            self.print_message_to_output("No identifiable devices connected")
            self.ui.connected_devices_table.setRowCount(1)
            item = QTableWidgetItem("No identifiable resources available")
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)
            self.ui.connected_devices_table.setItem(0, 0, item)
        else:
            self.ui.connected_devices_table.setRowCount(len(identified_resources))
            for row, (resource, idn_string) in enumerate(identified_resources):
                resource_item = QTableWidgetItem(resource)
                resource_item.setFlags(resource_item.flags() & ~Qt.ItemIsEditable)  # Make the item non-editable
                self.ui.connected_devices_table.setItem(row, 0, resource_item)

                idn_item = QTableWidgetItem(idn_string)
                idn_item.setFlags(idn_item.flags() & ~Qt.ItemIsEditable)  # Make the item non-editable
                self.ui.connected_devices_table.setItem(row, 1, idn_item)

        self.print_message_to_output("Resources identification completed!")
        
    def print_message_to_output(self, message):
        # self.ui.output_message.clear()
        self.ui.output_message.append(f"Output#{self.message_id}:  {message}")
        self.message_id = self.message_id+1
    
    def save_function_generator_config(self):
        self.fun_id = self.ui.fun_id_input.text()
        self.fun_waveform = self.ui.fun_config_waveform_input.currentText()  
        self.fun_freq = self.ui.fun_config_freq_input.text()     
        self.fun_vpp = self.ui.fun_config_vpp_input.text() 

        if not self.fun_id:
            self.print_message_to_output("Missing Function generator device ID.")
            return False
        elif not self.fun_waveform:
            self.print_message_to_output("Missing waveform type.")
            return False
        elif not self.fun_freq:
            self.print_message_to_output("Missing frequency value.")
            return False
        elif not self.fun_vpp:
            self.print_message_to_output("Missing Vpp value.")
            return False
        else:
            self.print_message_to_output("Function generator parameters saved!")
            return True

    def send_waveform_to_fun(self):
        if not self.save_function_generator_config():
            return

        self.waveform_dict = {
            'Sine': 'SIN',
            'Square': 'SQU',
            'Triangular': 'TRI'
        }

        try:
            self.function_generator = self.rm.open_resource(self.fun_id)
            self.function_generator.write(f"APPL:{self.waveform_dict[self.fun_waveform]} {self.fun_freq}, {self.fun_vpp}, 0")
            self.function_generator.close()
            self.print_message_to_output(f"APPL:{self.waveform_dict[self.fun_waveform]} {self.fun_freq}, {self.fun_vpp}, 0")
        except Exception as e:
            self.print_message_to_output(f"Error: {str(e)}")
        finally:
            self.function_generator.close()

    def stop_fun_generator(self):
        try:
            self.function_generator = self.rm.open_resource(self.fun_id)
            self.function_generator.write("OUTP OFF")
            self.function_generator.close()
            self.print_message_to_output("Function generator output stopped")
        except Exception as e:
            self.print_message_to_output(f"Error: {str(e)}")
        finally:
            self.function_generator.close()
            
    def save_scope_config(self):
        self.scope_id = self.ui.scope_config_id_input.text()
        self.scope_xrange = self.ui.scope_config_xrange_input.text()
        self.scope_yrange = self.ui.scope_config_yrange_input.text()
        self.scope_trigger_pos = self.ui.scope_config_trigger_input.text()

        if not self.scope_id:
            self.print_message_to_output("Missing Scope ID!")
            return False
        elif not self.scope_xrange:
            self.print_message_to_output("Missing X range!")
            return False
        elif not self.scope_yrange:
            self.print_message_to_output("Missing Y range!")
            return False
        elif not self.scope_trigger_pos:
            self.print_message_to_output("Missing Trigger value!")
            return False
        else:
            self.print_message_to_output("Scope parameters saved!")
            return True

    def accel_save(self):
        self.port = self.ui.accel_config_com_input.text()
        self.baudrate = self.ui.com_baud_rate_input.currentText()

        if not self.port:
            # self.ui.accel_com_status_label.setText("Error!!!")
            self.print_message_to_output("Entered valid COM port number!")
            return False
        elif not self.baudrate:
            self.print_message_to_output("Entered valid BAUD Rate for communication!")
            return False
        else:
            self.print_message_to_output("COM port parameters saved!")
            return True

    def fetch_and_update_scope_data(self):
        if not self.save_scope_config():
            return
        else:
            self.save_scope_config()

            # step 1: Check selected channels and fetch waveform data
            channels = [
                    self.ui.scope_channel1.isChecked(),
                    self.ui.scope_channel2.isChecked(),
                    self.ui.scope_channel3.isChecked(),
                    self.ui.scope_channel4.isChecked()
                ]
            
            if sum(channels) > 0:
                try:
                    # Step 2: Connect to oscilloscope
                    rtb = RsInstrument(self.scope_id, True, False)
                    rtb.write_str(f"TIM:ACQT {self.scope_xrange}")
                    

                    # step 3: fetch selected data
                    scope_data = {}
                    colors = ['blue', 'green', 'red', 'purple']
                    for i, ch in enumerate(channels, start=1):
                        if ch:
                            rtb.write_str(f"CHAN{i}:DATA:SOURCE CHAN{i}")
                            rtb.write_str(f'CHAN: RANG {self.scope_yrange}')
                            waveform = rtb.query_bin_or_ascii_float_list(f'FORM ASC;:CHAN{i}:DATA?')
                            x_increment = float(rtb.query(f'CHAN{i}:DATA:XINC?'))
                            x_origin = float(rtb.query(f'CHAN{i}:DATA:XOR?'))
                            time_data = np.arange(0, len(waveform)) * x_increment + x_origin
                            scope_data[f'Channel_{i}'] = pd.DataFrame({
                                'time_data': time_data,
                                'waveform': waveform,
                                'color': colors[i-1]
                                })
                    rtb.close()
                    # Step 4: Set up the QGraphicsScene and QGraphicsView
                    self.scope_scene = QGraphicsScene()
                    self.ui.scope_graphics_view.setScene(self.scope_scene)

                    # Step 5: Get the current size of the QGraphicsView
                    size = self.ui.scope_graphics_view.size()
                    self.dpi = 600

                    # Step 6: figure settings
                    self.scope_figure = Figure(figsize=(size.width()/self.dpi, size.height()/self.dpi), dpi=self.dpi)
                    self.ax = self.scope_figure.add_subplot(111)
                    self.scope_canvas = FigureCanvas(self.scope_figure)
                    self.scope_canvas.setFixedSize(size.width()*0.85, size.height()*0.85)
                    self.scope_scene.addWidget(self.scope_canvas)

                    # Step 7: Plot the data from the selected channels
                    for channel_name, data in scope_data.items():
                        self.ax.plot(data['time_data'], data['waveform'], label=channel_name, color=data['color'])

                    self.ax.legend()

                    # Step 7: Draw the plot
                    self.scope_canvas.draw()

                    self.print_message_to_output("Scope data plotted!")
                    self.print_message_to_output("Scope data fetched successfully!")
                except Exception as e:
                    self.print_message_to_output(str(e))
                    rtb.close()
            else:
                self.print_message_to_output("Error! No channels selected.")

    def start_acquisition(self):
        self.accel_save()

        self.ser = serial.Serial(self.port, self.baudrate)
        self.com_status = True

        while self.com_status:
            if self.ser.is_open:
                try:
                    self.print_message_to_output("serial port connected!")

                    line_data = self.ser.readline().decode('utf-8').strip()
                    if line_data:
                        print(f"Raw data read from serial: {line_data}")
                    # print(line_data)
                    # self.print_message_to_output(line_data)

                    time_str, g_value_str = line_data.split(", ")
                    time = float(time_str[1:])
                    g_value = float(g_value_str[:-1])

                    self.accel_time_data.append(time)
                    self.accel_g_value_data.append(g_value)

                    print(f"lengths: {len(self.accel_time_data)},{len(self.accel_g_value_data)}")

                    if len(self.accel_time_data) % 5 == 0:
                        self.update_plot()
                except Exception as e:
                    self.print_message_to_output(f"Error: {e}")

    def update_plot(self):
        self.accel_time_line.set_data(self.accel_time_data, self.accel_g_value_data)
        # self.accel_time_ax.clear()
        self.accel_time_ax.grid(True)
        self.accel_time_ax.set_ylim(-50, 50)
        self.accel_time_ax.plot(self.accel_time_data, self.accel_g_value_data, lw=2)

        self.time_series_canvas.draw()
        
    def stop_acquisition(self):
        if self.ser.is_open:
            self.ser.close()
            self.com_status = False
            self.print_message_to_output("port closed")        
        
    def save_data_to_excel(self):
        if not (self.time_data and self.fft_data):
            self.print_message_to_output("No data available to save.")
            return
    
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"data_{timestamp}.xlsx"
    
        try:
            with pd.ExcelWriter(filename) as writer:
                # Save time series data
                df_time = pd.DataFrame(self.time_data)
                df_time.to_excel(writer, sheet_name='Time Data', index=False)

                # Save FFT data
                df_fft = pd.DataFrame(self.fft_data)
                df_fft.to_excel(writer, sheet_name='FFT Data', index=False)

            self.print_message_to_output(f"Data saved successfully as {filename}.")
        except Exception as e:
            self.print_message_to_output(f"Failed to save data: {e}")        
        
    def closeEvent(self, event):
        """Handle the window close event to clean up resources."""
        # Stop the animation if it's running
        # if self.ani:
        #     self.ani.event_source.stop()
        
        # Check if the serial port is open and close it
        if self.ser and self.ser.is_open:
            print("Closing serial port...")
            self.ser.close()
        
        # Accept the close event
        event.accept()                    
                
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main_window = MainWindow() #loadUiWidget("form.ui")
    main_window.show()
    sys.exit(app.exec_())