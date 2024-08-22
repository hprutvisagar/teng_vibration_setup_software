import sys
import serial
import pyvisa
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QVBoxLayout, QWidget
from ui_form import Ui_main_widget  # Import the generated class
from RsInstrument import RsInstrument
from PySide6.QtWidgets import QApplication, QMainWindow

class PlotWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.figure, self.ax = plt.subplots(figsize=(8, 6))
        self.canvas = FigureCanvas(self.figure)
        
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def plot_data(self, data_dict):
        self.ax.clear()  # Clear the previous plot
        
        for channel, data in data_dict.items():
            self.ax.plot(data['time_data'], data['waveform'], label=f'Channel {channel}')
        
        self.ax.set_xlabel('Time (s)')
        self.ax.set_ylabel('Voltage (V)')
        self.ax.set_title('Oscilloscope Waveforms')
        self.ax.grid(True)
        self.ax.legend()
        self.canvas.draw()  # Redraw the canvas with the new plot

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_main_widget()  # Instantiate the UI class
        self.ui.setupUi(self)  # Set up the UI

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
        self.ui.scope_fetch_button.clicked.connect(self.scope_fetch_data)
        self.ui.scope_data_save_button.clicked.connect(self.scope_save_data)

    ## essential methods defined here
    def print_message_to_output(self,message):
        self.ui.output_message.clear()
        self.ui.output_message.setPlainText(message)

    ## Identify section definitions
    def identify_and_print_devices(self):
        # Get the list of connected devices
        resources = self.rm.list_resources()
        resources = [x for x in set(resources)]  # eliminates duplicates
        
        # Clear the table before populating it
        self.ui.connected_devices_table.clearContents()
        self.ui.connected_devices_table.setRowCount(len(resources))
        self.ui.connected_devices_table.setColumnCount(2)
        self.ui.connected_devices_table.setHorizontalHeaderLabels(["Resource ID", "Resource Identification"])
        self.ui.connected_devices_table.setColumnWidth(0,200)

        # Set the second column to take up the remaining space
        self.ui.connected_devices_table.horizontalHeader().setStretchLastSection(True)

        if len(resources) == 0:
            # If no resources are found, display a message in the first row
            print('no devices connected')
            self.ui.connected_devices_table.setRowCount(1)
            item = QTableWidgetItem("No resources available")
            self.ui.connected_devices_table.setItem(0, 0, item)
        else:
        # Populate the table with the list of resources        
            for row, resource in enumerate(resources):
                resource_item = QTableWidgetItem(resource)
                self.ui.connected_devices_table.setItem(row, 0, resource_item)

                try:
                    instrument = self.rm.open_resource(resource)
                    idn_string = instrument.query("*IDN?")
                except Exception as e:
                    idn_string = f"Error: {str(e)}"
                finally:
                    instrument.close()

                # Add the IDN string to the second column
                idn_item = QTableWidgetItem(idn_string)
                self.ui.connected_devices_table.setItem(row, 1, idn_item)     
        self.print_message_to_output("resources identification completed!")

    ## function generator definitions
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
            'Sine' : 'SIN',
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

    ## oscilloscope definitions
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

    ## accelerometer definitions
    def accel_config_check_status(self):
        accel_com_text = self.ui.accel_config_com_input.text()

        # if len(accel_com) == 0:
        #     self.ui.accel_com_status_label.setText("Error!!!")

        if not accel_com_text:
            self.ui.accel_com_status_label.setText("Error!!!")
            self.print_message_to_output("Entered valid COM port number!")
            return
        try:
            accel_com = int(accel_com_text)
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
            self.print_message_to_output("Port is open but no data available")

    def get_com_status(self, com_port):
        try:
            with serial.Serial(com_port, timeout=1) as ser:
                # Check if the port is readable
                if ser.in_waiting > 0:
                    return "Active and readable"
                else:
                    return "Port is open but no data available"
        except serial.SerialException:
            self.print_message_to_output("COM Port is not accessible") 
            return "Error!!! COM Port is not accessible"

    def accel_save(self):
        self.accel_config_check_status()

    def scope_fetch_data(self):
        # self.ch1_checked = "checked" if self.ui.scope_channel1.isChecked() else "unchecked"
        # self.ch2_checked = "checked" if self.ui.scope_channel2.isChecked() else "unchecked"
        # self.ch3_checked = "checked" if self.ui.scope_channel3.isChecked() else "unchecked"
        # self.ch4_checked = "checked" if self.ui.scope_channel4.isChecked() else "unchecked"

        # self.print_message_to_output(f"ch1: {self.ch1_checked}, ch2: {self.ch2_checked}, ch3= {self.ch3_checked}")
        if self.save_scope_config():
            try:
                channels = [
                self.ui.scope_channel1.isChecked(),
                self.ui.scope_channel2.isChecked(),
                self.ui.scope_channel3.isChecked(),
                self.ui.scope_channel4.isChecked()
                ]
                # Connect to oscilloscope
                rtb = RsInstrument(self.scope_id, True, True)
                rtb.write_str(f"TIM:ACQT {self.scope_xrange}")
                for i, ch in enumerate(channels, start=1):
                    if ch:
                        rtb.write_str(f"CHAN{i}:RANG {self.scope_yrange}")
                        rtb.write_str(f"CHAN{i}:OFFS 0.0")
                        rtb.write_str(f"CHAN{i}:COUP ACL")
                        rtb.write_str(f"CHAN{i}:STAT ON")
                    else:
                        rtb.write_str(f"CHAN{i}:STAT OFF")

                # Trigger Settings
                rtb.write_str("TRIG:A:MODE AUTO")
                rtb.write_str(f"TRIG:A:TYPE EDGE;:TRIG:A:EDGE:SLOP POS")
                rtb.write_str(f"TRIG:A:SOUR CH1")
                rtb.write_str(f"TRIG:A:LEV1 {self.scope_trigger_pos}")
                rtb.query_opc()

                # Fetch data from checked channels
                self.scope_data = {}
                for i, ch in enumerate(channels, start=1):
                    if ch:
                        rtb.write_str(f"CHAN{i}:DATA:SOURCE CHAN{i}")
                        waveform = rtb.query_bin_or_ascii_float_list('FORM ASC;:CHAN{i}:DATA?')
                        x_increment = float(rtb.query(f'CHAN{i}:DATA:XINC?'))
                        x_origin = float(rtb.query(f'CHAN{i}:DATA:XOR?'))
                        time_data = np.arange(0, len(waveform)) * x_increment + x_origin
                        self.scope_data[f'Channel_{i}'] = pd.DataFrame({
                            'time_data': time_data,
                            'waveform': waveform
                        })
                rtb.close()

                self.plot_widget = PlotWidget()
                self.setCentralWidget(self.plot_widget)

                # Plot data
                self.plot_widget.plot_data(self.scope_data)

            except Exception as e:
                self.print_message_to_output(f"Error: {str(e)}")
        else:
            self.print_message_to_output("Missing scope parameters!")

    def scope_save_data(self):
        if self.scope_data:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            for channel, df in self.scope_data.items():
                filename = f"data_{timestamp}_channel_{channel[-1]}.csv"
                df.to_csv(filename, index=False)
            self.identify_and_print_devices("Data fetched and saved successfully.")
        else:
            self.identify_and_print_devices("No data available.")


        

        




    #     self.save_function_generator_config() # trying to save the variables here

    #     if not (self.fun_id or self.fun_waveform or self.fun_freq or self.fun_vpp):
    #         print()


        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()  # Create an instance of your MainWindow class
    main_window.show()  # Show the main window
    sys.exit(app.exec())  # Start the application loop

