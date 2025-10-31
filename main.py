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
from scipy.fft import rfft, rfftfreq



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

class AccelerometerThread(QThread):
    new_accel_data = Signal(float, float)  # Emit z acceleration & time data

    def __init__(self, port, baudrate):
        super().__init__()
        self.serial_port = serial.Serial(port, baudrate, timeout=1)
        self.is_running = False

    def run(self):
        while self.is_running:
            try:
                if self.serial_port.in_waiting:
                    line_data = self.serial_port.readline().decode('utf-8').strip()
                    
                    if line_data:
                        time_str, g_value_str = line_data.split(", ")
                        time = float(time_str[1:])
                        g_value = float(g_value_str[:-1])                        
                        self.new_accel_data.emit(time, g_value)

            except Exception as e:
                print(f"Error reading from accelerometer: {e}")

    def stop(self):
        self.is_running = False
        self.serial_port.close()
        self.quit()
            
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
        
        self.scope_graph.showAxis('left', True)
        self.scope_graph.showAxis('bottom', True)
        self.scope_graph.showAxis('right', True)
        self.scope_graph.showAxis('top', True)
        # self.scope_graph.getAxis('top').setTicks([])  # Disable top ticks
        self.scope_graph.setLabel('left', 'voltage (V)')
        self.scope_graph.setLabel('bottom', 'Time (s)')
        
        # Accelerometer graph adjustments
        self.accel_graph = pg.PlotWidget()
        accel_parent_layout = self.ui.accel_graph.parent().layout()
        accel_parent_layout.replaceWidget(self.ui.accel_graph, self.accel_graph)
        self.ui.accel_graph.deleteLater()
        
        self.accel_graph.showAxis('left', True)
        self.accel_graph.showAxis('bottom', True)
        self.accel_graph.showAxis('right', True)
        self.accel_graph.showAxis('top', True)
        self.accel_graph.setLabel('bottom', 'Time (s)')  
        
        self.curve_g = self.accel_graph.plot([], [], pen='r', name='g-value')
        self.accel_graph.setXRange(0, 5000)
        self.accel_graph.setYRange(-10, 10)        
        
        self.freq_text_item = pg.TextItem("First Frequency: N/A")
        self.accel_graph.addItem(self.freq_text_item)
        self.freq_text_item.setPos(13,10)
        
        # self.first_freq_item = self.accel_legend.addItem(pg.TextItem("First Frequency: N/A", anchor=(1, 0)), name='Peak Frequency')
        # self.accel_legend.setPos(self.accel_graph.viewRange()[0][1], self.accel_graph.viewRange()[1][1])  # Top right corner         
               
        self.accel_thread = None
        self.latest_peak_frequency = None
        
        # Set the time window for visualization
        self.time_window = 5000  # using 5 sec of data
        self.time_data = np.array([]) 
        self.g_values = np.array([])
        self.accel_data = pd.DataFrame({"time": self.time_data, 
                                       "g": self.g_values})
        

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
        self.ui.scope_data_save_button.clicked.connect(self.scope_data_save)  # oscilloscope data save button
        self.ui.accel_fetch_button.clicked.connect(self.accel_start_data_acquisition) # accelerometer connect button
        self.ui.accel_disconnect_button.clicked.connect(self.accel_stop_data_acquisition) # accelerometer disconnect button
        self.ui.accel_save_button.clicked.connect(self.accel_save_data) # accelerometer data save button
        
        #############################################################################################
        ##   logos addition                                                                        ##
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
        resources = list(set(self.rm.list_resources()))

        # Clear and prep table
        self.ui.connected_devices_table.clearContents()
        self.ui.connected_devices_table.setColumnCount(2)
        self.ui.connected_devices_table.setHorizontalHeaderLabels(["Resource ID", "Device Name"])
        self.ui.connected_devices_table.horizontalHeader().setStretchLastSection(True)

        identified_resources = []

        for resource in resources:
            try:
                instr = self.rm.open_resource(resource)
                idn_string = instr.query("*IDN?").strip()
                if idn_string:
                    idn_parts = [part.strip() for part in idn_string.split(',')]
                    device_name = f"{idn_parts[0]} {idn_parts[1]}" if len(idn_parts) > 1 else idn_string
                    identified_resources.append((resource, device_name))
            except Exception as e:
                print(f"Error with resource {resource}: {e}")
            finally:
                try:
                    instr.close()
                except Exception:
                    pass

        # Fill table
        self.ui.connected_devices_table.setRowCount(len(identified_resources))
        for row, (resource, device_name) in enumerate(identified_resources):
            self.ui.connected_devices_table.setItem(row, 0, QTableWidgetItem(resource))
            self.ui.connected_devices_table.setItem(row, 1, QTableWidgetItem(device_name))

        # Resize nicely
        header = self.ui.connected_devices_table.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)


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
        
        # Automatically resize columns to fit text
        self.ui.connected_devices_table.resizeColumnsToContents()

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
                
                # Turn all channels off first
                for i in range(1, 5):
                    rtb.write_str(f"CHAN{i}:STAT OFF")
                    
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
                        
                        rtb.write_str_with_opc("SINGle", 15000)
                        
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
                # scope_legend.LabelTextSize('12')
                
                for channel_name, data in self.scope_data.items():
                    waveform = data['waveform']
                    vpp = np.max(waveform) - np.min(waveform)
                    vrms = np.sqrt(np.mean(np.square(waveform)))
                    vavg = np.mean(waveform)
                    
                    label = f"{channel_name} | Vpp = {vpp:.3f} V"
                    
                    # label = f"{channel_name} | Vpp={vpp:.3f}V | Vrms={vrms:.3f}V | Vavg={vavg:.3f}V"
                    
                    self.scope_graph.plot(data['time_data'], 
                                          data['waveform'], 
                                          name=label, 
                                          pen = pg.mkPen(colors[int(channel_name.split("_")[1]) - 1], width=2), 
                                          width=2)
                
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
            self.print_message_to_output("No data available to save!")
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
        
    def accel_start_data_acquisition(self):
        if not self.accel_save():
            self.identify_and_print_devices("missing COM port information")
            return
        
        # Reset variables
        self.time_data = np.array([])  # Reset time data
        self.g_values = np.array([])    # Reset g-values
        
        self.accel_data = pd.DataFrame({"time": self.time_data, 
                                       "g": self.g_values})  # reset values

        if self.accel_thread is None:
            self.accel_thread = AccelerometerThread(port=self.port, baudrate=self.baudrate)
            self.accel_thread.new_accel_data.connect(self.update_plot)
            self.accel_thread.is_running = True
            self.accel_thread.start()
        
        self.ui.accel_fetch_button.setEnabled(False)
        self.ui.accel_disconnect_button.setEnabled(True)
        
    def accel_stop_data_acquisition(self):
        if self.accel_thread:
            self.accel_thread.stop()
            self.accel_thread = None
        
        self.ui.accel_fetch_button.setEnabled(True)
        self.ui.accel_disconnect_button.setEnabled(False)
        
    @Slot(float, float)
    def update_plot(self, time_val, g_value):
        # Append new data
        new_data = pd.DataFrame({
        "time": [time_val],
        "g": [g_value]
        })
        
        self.accel_data = pd.concat([self.accel_data, new_data], ignore_index=True)
        
        if max(self.accel_data['time']) - min(self.accel_data['time']) < self.time_window:
            valid_data = self.accel_data
        else:
            threshold = time_val  - self.time_window
            valid_data = self.accel_data[self.accel_data['time'] >= threshold] 
        
        self.curve_g.setData(valid_data["time"].values, valid_data['g'].values)
        
        self.accel_graph.setXRange(max(0, valid_data["time"].min()), time_val)
        self.accel_graph.setYRange(valid_data["g"].min(), valid_data["g"].max())
        
        # FFT calculations
        g_values = valid_data['g'].values
        time_values = valid_data['time'].values
        
        if len(g_values) > 1:
            # Compute the FFT of g_values
            fft_values = np.fft.fft(g_values)
            fft_magnitudes = np.abs(fft_values)
            
            n = len(g_values)
            # Calculate time intervals based on the differences of time values
            time_intervals = np.diff(time_values)  # Calculate differences
            avg_time_interval = np.mean(time_intervals) / 1000.0  # Convert to seconds
            
            freqs = np.fft.fftfreq(n, d=avg_time_interval)  # Frequency bins
            
            # Ignore the zero-frequency (DC component)
            fft_magnitudes[0] = 0

            # Find peak frequency
            peak_index = np.argmax(fft_magnitudes)
            peak_freq = freqs[peak_index]
            
            # Update legend text with the first peak frequency
            self.freq_text_item.setText(f"First Frequency: {peak_freq:.2f} Hz")
            x_range = self.accel_graph.viewRange()[0]  #-> [x_min, x_max]
            y_range = self.accel_graph.viewRange()[1]  #-> [y_min, y_max]
            self.freq_text_item.setPos(
                x_range[0], 
                y_range[1]
                )
              
                    
    def accel_save_data(self):
        if len(self.accel_data) == 0:  # Check if g_values is empty
            self.print_message_to_output("No data to save.")
            return

        options = QFileDialog.Options()
        output_directory, _ = QFileDialog.getSaveFileName(self, "Save CSV File", self.last_used_directory, "CSV Files (*.csv);;All Files (*)", options=options)

        if output_directory:
            self.last_used_directory = os.path.dirname(output_directory)
            self.save_last_used_directory(self.last_used_directory)

            # Save the DataFrame to a CSV file
            self.accel_data.to_csv(output_directory, index=False)
            self.print_message_to_output("Data saved successfully.")      
        
    def closeEvent(self, event):
        """Handle the window close event to clean up resources."""
        if self.accel_thread:
            self.accel_thread.stop()
        event.accept()                  
                
if __name__ == "__main__":
    import sys
    from PySide6.QtCore import Qt, QCoreApplication
    
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())