import sys
import serial
import pyvisa
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PySide6 import QtCore, QtGui, QtUiTools, QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QVBoxLayout, QWidget, QGraphicsScene, QGraphicsProxyWidget, QFileDialog
from PySide6.QtCore import Qt, QTimer, Signal, Slot, QThread, Signal, QObject
from ui_form import Ui_main_widget  
from RsInstrument import RsInstrument
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

import matplotlib.animation as animation
from collections import deque
from scipy.fft import fft, fftfreq

import json
import os

import threading

import pyqtgraph as pg


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

class DataAcquisitionWorker(QObject):
    data_ready = Signal(float, float)  # Signal to emit new data
    error_occurred = Signal(str)       # Signal to emit error messages
    finished = Signal()                # Signal to indicate the thread has finished

    def __init__(self, port, baudrate):
        super().__init__()
        self.port = port
        self.baudrate = baudrate
        self.com_status = True  # Control variable for stopping the loop

    def run(self):
        """Function to be executed in a separate thread."""
        try:
            self.ser = serial.Serial(self.port, self.baudrate)
            self.com_status = True
        except Exception as e:
            self.error_occurred.emit(f"Error opening serial port: {e}")
            return

        while self.com_status:
            if self.ser.is_open:
                try:
                    line_data = self.ser.readline().decode('utf-8').strip()
                    time_str, g_value_str = line_data.split(", ")
                    time = float(time_str[1:])
                    g_value = float(g_value_str[:-1])
                    self.data_ready.emit(time, g_value)
                except Exception as e:
                    self.error_occurred.emit(f"Error reading serial data: {e}")
                    self.stop()

        self.finished.emit()

    def stop(self):
        """Stop the data acquisition."""
        self.com_status = False
        if self.ser and self.ser.is_open:
            self.ser.close()
            
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = loadUiWidget("ui/form.ui", self)
        if self.ui:
            self.setupUi()
            # self.list_all_widgets() ## debug only...lists all available objects in the UI
        else:
            print("Failed to load UI.")
        
        self.thread = None
        self.worker = None
        self.accel_time_data = []
        self.accel_g_value_data = []
            
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
        
        self.last_used_directory = self.load_last_used_directory()
        
        #resource manager settings
        self.rm = pyvisa.ResourceManager()
        
        # replacing the graph of oscilloscope
        self.scope_graph = pg.PlotWidget()
        scope_parent_layout = self.ui.scope_graphics_view.parent().layout()
        scope_parent_layout.replaceWidget(self.ui.scope_graphics_view, self.scope_graph)
        self.ui.scope_graphics_view.deleteLater()
        
        # replacing the accelerometer graph object
        self.accel_graph = pg.PlotWidget()
        accel_parent_layout = self.ui.accel_graph.parent().layout()
        accel_parent_layout.replaceWidget(self.ui.accel_graph, self.accel_graph)
        self.ui.accel_graph.deleteLater()
        
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
        self.ui.scope_data_save_button.clicked.connect(self.scope_data_save)
        self.ui.accel_fetch_button.clicked.connect(self.start_acquisition)
        self.ui.accel_disconnect_button.clicked.connect(self.stop_acquisition)
        self.ui.accel_save_button.clicked.connect(self.save_data_to_excel)
        
        #############################################################################################
        ##   logos addition                                                           ##
        #############################################################################################
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

        # step 1: Check selected channels and fetch waveform data
        channels = [
                self.ui.scope_channel1.isChecked(),
                self.ui.scope_channel2.isChecked(),
                self.ui.scope_channel3.isChecked(),
                self.ui.scope_channel4.isChecked()
            ]
        
        self.scope_data = {}
        colors = ['blue', 'green', 'red', 'purple']
            
        if sum(channels) > 0:
            try:
                # Step 2: Connect to oscilloscope
                rtb = RsInstrument(self.scope_id, True, True)
                rtb.write_str(f"TIM:ACQT {self.scope_xrange}")
                
                # step 3: fetch selected data
                for i, ch in enumerate(channels, start=1):
                    if ch:
                        rtb.write_str(f"CHAN{i}:RANG {self.scope_yrange}")
                        rtb.write_str(f"CHAN{i}:OFFS 0.0")
                        rtb.write_str(f"CHAN{i}:COUP ACL")
                        rtb.write_str(f"CHAN{i}:STAT ON") 
                        
                        rtb.write_str(f"PROBe{i}:SETup:ATTenuation:UNIT V")  # probe set to 1:1 attenuation factor
                        rtb.write_str(f'PROBe{i}:SETup:ATTenuation:MANual 1.0')
                        
                        rtb.write_str(f"TRIG:A:MODE AUTO")
                        rtb.write_str(f"TRIG:A:TYPE EDGE;:TRIG:A:EDGE:SLOP POS")
                        rtb.write_str(f"TRIG:A:SOUR CH{i}")
                        rtb.write_str(f"TRIG:A:LEV1 {self.scope_trigger_pos}")                        
                        rtb.query_opc()
                        
                        rtb.write_str_with_opc("SINGle", 3000)
                        
                        waveform = rtb.query_bin_or_ascii_float_list(f"FORM ASC;:CHAN{i}:DATA?")
                        
                        # waveform = float(rtb.query(f'CHAN{i}:DATA?'))
                        x_increment = float(rtb.query(f"CHAN{i}:DATA:XINC?"))
                        x_origin = float(rtb.query(f'CHAN{i}:DATA:XOR?'))
                        time_data = np.arange(0, len(waveform)) * x_increment + x_origin
                        
                        self.scope_data[f'Channel_{i}'] = pd.DataFrame({
                            'time_data': time_data,
                            'waveform': waveform,
                            })
                rtb.close()
                
                # Step 4: plot the data
                self.scope_graph.clear()  # Clears the existing plots
                
                scope_legend = self.scope_graph.addLegend()
                scope_legend.setPos(0,0)
                
                for channel_name, data in self.scope_data.items():
                    self.scope_graph.plot(data['time_data'], data['waveform'], name=channel_name, pen = pg.mkPen(colors[int(channel_name.split("_")[1]) - 1], width=2), width=2)
                
                scope_legend.setBrush(pg.mkBrush(255, 255, 255, 200))
                
                self.print_message_to_output("Scope data fetched & plotted successfully!")
                
            except Exception as e:
                self.print_message_to_output(str(e))
            finally:
                rtb.close()
        else:
            self.print_message_to_output("Error! No channels selected.")
            
    def load_last_used_directory(self):
        # Load the last used directory from a JSON file
        try:
            with open('last_used_directory.json', 'r') as file:
                data = json.load(file)
                return data.get('last_directory', os.path.expanduser("~"))  # Default to home directory
        except (FileNotFoundError, json.JSONDecodeError):
            return os.path.expanduser("~")  # Default to home directory if file not found or invalid
        
    def save_last_used_directory(self, directory):
        # Save the last used directory to a JSON file
        with open('last_used_directory.json', 'w') as file:
            json.dump({'last_directory': directory}, file)
            
    def scope_data_save(self):
        if not self.scope_data:
            return
        
        options = QFileDialog.Options()
        output_directory, _ = QFileDialog.getSaveFileName(self, "Save CSV File", self.last_used_directory, "CSV Files (*.csv);;All Files (*)", options=options)
        
        if output_directory:
            self.last_used_directory = os.path.dirname(output_directory)
            self.save_last_used_directory(self.last_used_directory)

            # Loop through the scope_data dictionary
            for channel_name, data in self.scope_data.items():
                # Create a CSV file name based on the channel name
                csv_filename = f"{output_directory[:-4]}_{channel_name}.csv"
    
                # Save the DataFrame to a CSV file
                data.to_csv(csv_filename, index=False)  # Set index=False to avoid writing row indices
            
        self.print_message_to_output('Data saved')
        
    def start_acquisition(self):
        print('hi')
        # self.accel_save()
        # #####
        # #     def start_acquisition(self):
        # # """Start the data acquisition in a new thread."""
        # # Set up the thread and worker
        # self.thread = QThread()
        # self.worker = DataAcquisitionWorker(port=self.port, baudrate=self.baudrate)

        # # Move the worker to the thread
        # self.worker.moveToThread(self.thread)

        # # Connect signals and slots
        # self.thread.started.connect(self.worker.run)
        # self.worker.data_ready.connect(self.update_plot)
        # self.worker.error_occurred.connect(self.print_message_to_output)
        # self.worker.finished.connect(self.thread.quit)
        # self.worker.finished.connect(self.worker.deleteLater)
        # self.thread.finished.connect(self.thread.deleteLater)

        # # Start the thread
        # self.thread.start()
        ######
        # self.ser = serial.Serial(self.port, self.baudrate)
        # self.com_status = True

        # while self.com_status:
        #     if self.ser.is_open:
        #         try:
        #             self.print_message_to_output("serial port connected!")

        #             line_data = self.ser.readline().decode('utf-8').strip()
        #             # if line_data:
        #             #     print(f"Raw data read from serial: {line_data}")
        #             # print(line_data)
        #             # self.print_message_to_output(line_data)

        #             time_str, g_value_str = line_data.split(", ")
        #             time = float(time_str[1:])
        #             g_value = float(g_value_str[:-1])

        #             self.accel_time_data.append(time)
        #             self.accel_g_value_data.append(g_value)

        #             print(f"lengths: {len(self.accel_time_data)},{len(self.accel_g_value_data)}")

        #             if len(self.accel_time_data) % 5 == 0:
        #                 self.update_plot()
        #         except Exception as e:
        #             self.print_message_to_output(f"Error: {e}")

    def update_plot(self):
        # """Update the plot with new data."""
        # self.accel_time_data.append(time)
        # self.accel_g_value_data.append(g_value)

        # self.accel_plot_widget.clear()
        # self.accel_plot_widget.plot(self.accel_time_data, self.accel_g_value_data, pen='r')
        print("hi")
        
    def stop_acquisition(self):
        # if self.ser.is_open:
        #     self.ser.close()
        #     self.com_status = False
        #     self.print_message_to_output("port closed")        
        
        if self.worker:
            self.worker.stop()
        
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
    sys.exit(app.exec())