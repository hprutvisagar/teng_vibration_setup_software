import sys
import serial
import pyvisa
import datetime
import pandas as pd
import numpy as np
import matplotlib
#matplotlib.use("Qt5Agg")
# from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QVBoxLayout, QWidget, QGraphicsScene, QGraphicsProxyWidget
from PySide6.QtCore import Qt, QTimer, Signal, Slot
from ui_form import Ui_main_widget  # Import the generated class
from RsInstrument import RsInstrument
from ui_form import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

# from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
# from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QVBoxLayout, QWidget, QGraphicsScene, QGraphicsProxyWidget
# from matplotlib.figure import Figure


class MainWindow(QMainWindow, Ui_main_widget):
    def __init__(self):
        super(MainWindow, self).__init__()

        central_widget = QWidget()

        self.ui = Ui_main_widget()
        self.ui.setupUi(central_widget)
        self.setCentralWidget(central_widget)

        self.initUI()
    
    def initUI(self):
        # Initialize PyVISA resource manager
        self.rm = pyvisa.ResourceManager()

        self.ui.output_message.setReadOnly(True)

        # Connect signals to your slots (functions) here
        self.ui.identify_res_button.clicked.connect(self.identify_and_print_devices)
        self.ui.fun_save_button.clicked.connect(self.save_function_generator_config)
        self.ui.fun_config_send_button.clicked.connect(self.send_waveform_to_fun)
        self.ui.scope_config_save_button.clicked.connect(self.save_scope_config)
        self.ui.accel_status_check_button.clicked.connect(self.accel_config_check_status)
        self.ui.accel_config_save_button.clicked.connect(self.accel_save)
        self.ui.scope_fetch_button.clicked.connect(self.fetch_and_update_data)
        self.ui.scope_data_save_button.clicked.connect(self.scope_save_data)
        
        # Initialize QTimer for real-time plotting
        # self.timer = QTimer()
        # self.timer.timeout.connect(self.fetch_and_update_data)
        # self.timer.setInterval(1000)  # Fetch data every 1000 milliseconds (1 second)

        # Create a QGraphicsScene and set it to the view
        # self.scene = QGraphicsScene()
        # self.ui.scope_graphics_view.setScene(self.scene)

        # # # Create the Matplotlib figure and axes
        # self.figure = Figure()
        # self.ax = self.figure.add_subplot(111)
        # self.canvas = FigureCanvas(self.figure)
        # self.view = FigureCanvas(Figure(figsize=(5, 2)))
        # self.axes = self.view.figure.subplots()

        self.scope_scene = QGraphicsScene()
        self.ui.scope_graphics_view.setScene(self.scope_scene)

        # # Create the Matplotlib figure and axes
        self.scope_figure = Figure(figsize=(12,6))
        self.ax = self.scope_figure.add_subplot(111)
        self.scope_canvas = FigureCanvas(self.scope_figure)
        # self.gridLayout.addWidget(self.canvas, 1,0)

        self.scope_scene.addWidget(self.scope_canvas)

        # # Create a graphics proxy widget and set the canvas
        # #self.proxy_widget = QGraphicsProxyWidget()
        # # self.proxy_widget.setParent(self.scene)  # Add the proxy to the scene
        # # self.canvas.setParent(proxy_widget)  # Set the canvas as child of the proxy
        # #self.proxy_widget.setWidget(self.canvas)

        # # Add the proxy widget to the scene
        # print(type(self.view))

        # self.ui.gridLayout.addWidget(self.view)
        # self.scene.addWidget(self.view)
        # self.plot_data()

        
        

        self.plot_data()

    def plot_data(self):
        # Generate data
        time_data = np.linspace(0, 1, 100)
        waveform_data = np.sin(2 * np.pi * 5 * time_data)
        
        # Plot the data
        self.ax.plot(time_data, waveform_data)
        self.ax.set_xlabel('Time (s)')
        self.ax.set_ylabel('Amplitude')
        self.ax.set_title('Sine Wave')
        self.ax.grid(True)
        
        # Draw the plot
        self.scope_canvas.draw()

            

        # self.scene.addWidget(self.canvas)

    def set_main_widget(self, widget):
        self.setCentralWidget(widget)

    def print_message_to_output(self, message):
        self.ui.output_message.clear()
        self.ui.output_message.setPlainText(message)

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

    def start_real_time_plotting(self):
        if not self.save_scope_config():
            return
    
    # def fetch_and_update_data(self):
    #     # Fetch data from the scope and update the plot
    #     data_dict = self.fetch_scope_data()
    #     self.update_plot(data_dict)

    def fetch_and_update_data(self):
        time_data = np.linspace(0, 1, 100)
        waveform_data = np.sin(2 * np.pi * 5 * time_data)

         # Plot the data
        self.ax.plot(time_data, waveform_data)
        self.ax.set_xlabel('Time (s)')
        self.ax.set_ylabel('Amplitude')
        self.ax.set_title('Sine Wave')
        self.ax.grid(True)

        self.canvas.draw()


        
        return
        try:
            # Connect to oscilloscope
            rtb = RsInstrument(self.scope_id, True, True)
            rtb.write_str(f"TIM:ACQT {self.scope_xrange}")
          
            channels = [
                self.ui.scope_channel1.isChecked(),
                self.ui.scope_channel2.isChecked(),
                self.ui.scope_channel3.isChecked(),
                self.ui.scope_channel4.isChecked()
            ]
          
            # Fetch data from checked channels
            scope_data = {}
            for i, ch in enumerate(channels, start=1):
                if ch:
                    rtb.write_str(f"CHAN{i}:DATA:SOURCE CHAN{i}")
                    waveform = rtb.query_bin_or_ascii_float_list('FORM ASC;:CHAN{i}:DATA?')
                    x_increment = float(rtb.query(f'CHAN{i}:DATA:XINC?'))
                    x_origin = float(rtb.query(f'CHAN{i}:DATA:XOR?'))
                    time_data = np.arange(0, len(waveform)) * x_increment + x_origin
                    scope_data[f'Channel_{i}'] = pd.DataFrame({
                        'time_data': time_data,
                        'waveform': waveform
                    })
            rtb.close()
            # Update the plot with new data
            self.plot_widget.update_plot(scope_data)
      
        except Exception as e:
            self.print_message_to_output(f"Error: {str(e)}")
    
    def update_plot(self, data_dict):
        self.ax.clear()  # Clear the previous plot
        
        for channel, data in data_dict.items():
            self.ax.plot(data['time_data'], data['waveform'], label=f'Channel {channel}')
        
        self.ax.set_xlabel('Time (s)')
        self.ax.set_ylabel('Voltage (V)')
        self.ax.set_title('Oscilloscope Waveforms')
        self.ax.grid(True)
        self.ax.legend()
        self.canvas.draw()  # Redraw the canvas with the new plot

    def scope_save_data(self):
        if self.scope_data:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            for channel, df in self.scope_data.items():
                filename = f"data_{timestamp}_channel_{channel[-1]}.csv"
                df.to_csv(filename, index=False)
            self.print_message_to_output("Data fetched and saved successfully.")
        else:
            self.print_message_to_output("No data available.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()  # Create an instance of your MainWindow class
    main_window.setGeometry(0, 0, 1800, 1800)
    main_window.show()  # Show the main window
    sys.exit(app.exec())  # Start the application loop
