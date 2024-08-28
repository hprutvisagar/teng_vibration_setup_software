import sys
import serial
import pyvisa
import datetime
import pandas as pd
import numpy as np
import matplotlib
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QVBoxLayout, QWidget, QGraphicsScene, QGraphicsProxyWidget
from PySide6.QtCore import Qt, QTimer, Signal, Slot
from ui_form import Ui_main_widget  
from RsInstrument import RsInstrument
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

import matplotlib.animation as animation
from collections import deque
from scipy.fft import fft, fftfreq

class MainWindow(QMainWindow, Ui_main_widget):
    def __init__(self):
        super(MainWindow, self).__init__()

        central_widget = QWidget()

        self.ui = Ui_main_widget()
        self.ui.setupUi(central_widget)
        self.setCentralWidget(central_widget)

        self.rm = pyvisa.ResourceManager()

        self.ui.output_message.setReadOnly(True) # setting the terminal to read only
        self.message_id = 1

        # Connect signals to your slots (functions) here
        self.ui.identify_res_button.clicked.connect(self.identify_and_print_devices) # resource identification button
        self.ui.fun_save_button.clicked.connect(self.save_function_generator_config) # function generator configuration save button
        self.ui.fun_config_send_button.clicked.connect(self.send_waveform_to_fun) # send waveform to function generator
        self.ui.scope_config_save_button.clicked.connect(self.save_scope_config) # oscilloscope config save button
        self.ui.accel_status_check_button.clicked.connect(self.accel_config_check_status) # accelerometer comport status check button
        self.ui.accel_config_save_button.clicked.connect(self.accel_save) # accelerometer configuration save button
        self.ui.scope_fetch_button.clicked.connect(self.fetch_and_update_scope_data) # oscilloscope data fetch button
        self.ui.scope_data_save_button.clicked.connect(self.save_scope_data)  # oscilloscope data save button
        self.ui.accel_fetch_button.clicked.connect(self.fetch_serial_port_data)
        self.ui.accel_disconnect_button.clicked.connect(self.disconnect_serial_port)
        self.ui.accel_save_button.clicked.connect(self.save_data_to_excel)

    def set_main_widget(self, widget):
        self.setCentralWidget(widget)

    def print_message_to_output(self, message):
        # self.ui.output_message.clear()
        self.ui.output_message.append(f"Output#{self.message_id}:  {message}")
        self.message_id = self.message_id+1
        
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

    def accel_config_check_status(self):
        self.accel_com_text = self.ui.accel_config_com_input.text()
        self.accel_com_baud_rate = self.ui.com_baud_rate_input.currentText()

        if not self.accel_com_text:
            self.ui.accel_com_status_label.setText("Error!!!")
            self.print_message_to_output("Entered valid COM port number!")
        elif not self.accel_com_baud_rate:
            self.ui.accel_com_status_label.setText("Error!!!")
            self.print_message_to_output("Entered valid BAUD Rate for communication!")
        else:
            self.print_message_to_output("COM port parameters saved!")

        try:
            accel_com = int(self.accel_com_text)
        except ValueError:
            self.ui.accel_com_status_label.setText("Error!!!")
            self.print_message_to_output("Entered valid COM port number!")
            return
        
        # Check the COM port status
        self.accel_com_status = self.get_com_status(f"COM{accel_com}")

        if self.accel_com_status == "Active and readable":
            self.ui.accel_com_status_label.setText(f"COM{accel_com} Available!")
        else:
            self.ui.accel_com_status_label.setText("Error!!!")
            self.print_message_to_output(f"Port{self.accel_com_text} is open but no data available")

    def get_com_status(self, com_port):
        try:
            with serial.Serial(com_port, timeout=1) as ser:
                if ser.in_waiting > 0:
                    return "Active and readable"
                else:
                    return "Port is open but no data available"
        except serial.SerialException:
            self.print_message_to_output("COM Port is not accessible") 
            return "Error!!! COM Port is not accessible"

    def accel_save(self):
        self.accel_config_check_status()

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
                    dpi = 600

                    # Step 6: figure settings
                    self.scope_figure = Figure(figsize=(size.width()/dpi, size.height()/dpi), dpi=dpi)
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
                

    def save_scope_data(self):
        if self.scope_data:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"data_{timestamp}.xlsx"
            with pd.ExcelWriter(filename, engine='xlsxwriter') as writer:
                for channel, df in self.scope_data.items():
                    sheet_name = f"Channel_{channel[-1]}"
                    df.to_excel(writer, sheet_name=sheet_name, index=False)
            
            self.print_message_to_output("Data fetched and saved successfully.")
        else:
             self.print_message_to_output("No data available.")

    def fetch_serial_port_data(self):
        # Check if the COM port is available
        if "Available" not in self.ui.accel_com_status_label.text():
            self.accel_config_check_status()
            return
        else:
            if self.ui.accel_config_com_input:

            # Initialize serial port parameters
                serial_port = f'COM{int(self.ui.accel_config_com_input.text())}'
                baudrate = self.ui.com_baud_rate_input.currentData()
                timeout = 1
                max_points = 100
                update_interval = 10

                try:
                    # Initialize the serial connection
                    self.ser = serial.Serial(serial_port, baudrate, timeout=timeout)
                except serial.SerialException as e:
                    self.print_message_to_output(f"Failed to open serial port: {e}")
                    return

                # Data storage
                self.data_queue = deque(maxlen=max_points)
                self.time_data = []
                self.fft_data = []

                # Setup the time series plot
                self.time_series_scene = QGraphicsScene()
                self.ui.accel_graph.setScene(self.time_series_scene)
                self.time_series_fig = Figure()
                self.ax1 = self.time_series_fig.add_subplot(111)
                self.time_series_canvas = FigureCanvas(self.time_series_fig)
                self.time_series_scene.addWidget(self.time_series_canvas)

                # Setup the FFT plot
                self.fft_scene = QGraphicsScene()
                self.ui.accel_fft_graph.setScene(self.fft_scene)
                self.fft_fig = Figure()
                self.ax2 = self.fft_fig.add_subplot(111)
                self.fft_canvas = FigureCanvas(self.fft_fig)
                self.fft_scene.addWidget(self.fft_canvas)

                # Start data acquisition and plotting loop
                self.running = True
                while self.running:
                    self.update_plots()

                # Close the serial connection when done
                self.ser.close()
            else:
                self.print_message_to_output("Missing COM port number!")


    def update_plots(self):
        if self.ser.in_waiting > 0:
            try:
                line = self.ser.readline().decode('utf-8').strip()
                if line:
                    self.data_queue.append(float(line))
            except ValueError:
                self.print_message_to_output("Received non-numeric data")

        # Update the time series plot
        self.ax1.clear()
        self.ax1.plot(range(len(self.data_queue)), list(self.data_queue), lw=2)
        self.ax1.set_xlim(0, len(self.data_queue))
        self.ax1.set_ylim(min(self.data_queue) - 1, max(self.data_queue) + 1)
        self.ax1.set_title('Real-Time Data Plot')
        self.time_series_canvas.draw()

        # Update the FFT plot every update_interval seconds
        if len(self.data_queue) > 1:
            self.compute_and_plot_fft()

        # Store data for saving
        self.time_data.append(list(self.data_queue))
        if len(self.data_queue) > 1:
            self.fft_data.append(self.compute_and_plot_fft())

    def compute_and_plot_fft(self):
        n = len(self.data_queue)
        T = 1.0  # Assuming 1 Hz sampling rate
        yf = fft(self.data_queue)
        xf = fftfreq(n, T)[:n//2]
        magnitudes = 2.0/n * np.abs(yf[0:n//2])
        dominant_freq = xf[np.argmax(magnitudes)]

        self.ax2.clear()
        self.ax2.plot(xf, magnitudes, lw=2)
        self.ax2.set_xlim(0, xf[-1])
        self.ax2.set_ylim(0, np.max(magnitudes) * 1.1)
        self.ax2.set_title(f'FFT - Dominant Frequency: {dominant_freq:.2f} Hz')
        self.fft_canvas.draw()

        return magnitudes
    
    def disconnect_serial_port(self):
        if hasattr(self, 'ser') and self.ser.is_open:
            self.running = False
            self.ser.close()
            self.print_message_to_output("Serial port disconnected.")
        else:
            self.print_message_to_output("Serial port is not connected.")

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



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()  # Create an instance of your MainWindow class
    main_window.setGeometry(0, 0, 1400, 800)
    main_window.show()  # Show the main window
    sys.exit(app.exec())  # Start the application loop
