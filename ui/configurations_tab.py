from PySide6 import QtWidgets
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from RsInstrument import RsInstrument

class ConfigurationsTab(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Main layout
        layout = QtWidgets.QVBoxLayout(self)

        # Function Generator Configuration
        function_gen_group = QtWidgets.QGroupBox("Function Generator Configuration")
        function_gen_layout = QtWidgets.QFormLayout()

        func_waveform_label = QtWidgets.QLabel("Waveform Type:")
        self.func_waveform_input = QtWidgets.QComboBox()
        self.func_waveform_input.addItems(["SIN", "TRI", "SQU"])
        function_gen_layout.addRow(func_waveform_label, self.func_waveform_input)

        func_vpp_label = QtWidgets.QLabel("Peak-to-Peak Voltage (Vpp):")
        self.func_vpp_input = QtWidgets.QLineEdit()
        function_gen_layout.addRow(func_vpp_label, self.func_vpp_input)

        func_offset_label = QtWidgets.QLabel("Offset (V):")
        self.func_offset_input = QtWidgets.QLineEdit()
        function_gen_layout.addRow(func_offset_label, self.func_offset_input)

        # Add Apply and Send buttons
        func_button_layout = QtWidgets.QHBoxLayout()
        self.func_apply_button = QtWidgets.QPushButton("Apply")
        self.func_send_button = QtWidgets.QPushButton("Send")
        func_button_layout.addWidget(self.func_apply_button)
        func_button_layout.addWidget(self.func_send_button)

        function_gen_layout.addRow(func_button_layout)
        function_gen_group.setLayout(function_gen_layout)
        function_gen_group.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        layout.addWidget(function_gen_group)

        # Oscilloscope Configuration
        oscilloscope_group = QtWidgets.QGroupBox("Oscilloscope Configuration")
        oscilloscope_layout = QtWidgets.QFormLayout()

        osc_x_min_label = QtWidgets.QLabel("X Min:")
        self.osc_x_min_input = QtWidgets.QLineEdit()
        oscilloscope_layout.addRow(osc_x_min_label, self.osc_x_min_input)

        osc_x_max_label = QtWidgets.QLabel("X Max:")
        self.osc_x_max_input = QtWidgets.QLineEdit()
        oscilloscope_layout.addRow(osc_x_max_label, self.osc_x_max_input)

        osc_y_min_label = QtWidgets.QLabel("Y Min:")
        self.osc_y_min_input = QtWidgets.QLineEdit()
        oscilloscope_layout.addRow(osc_y_min_label, self.osc_y_min_input)

        osc_y_max_label = QtWidgets.QLabel("Y Max:")
        self.osc_y_max_input = QtWidgets.QLineEdit()
        oscilloscope_layout.addRow(osc_y_max_label, self.osc_y_max_input)

        osc_trigger_label = QtWidgets.QLabel("Trigger Value:")
        self.osc_trigger_input = QtWidgets.QLineEdit()
        oscilloscope_layout.addRow(osc_trigger_label, self.osc_trigger_input)

        # Add Apply, Send, and Save buttons
        osc_button_layout = QtWidgets.QHBoxLayout()
        self.osc_apply_button = QtWidgets.QPushButton("Apply")
        self.osc_send_button = QtWidgets.QPushButton("Send")
        self.osc_save_button = QtWidgets.QPushButton("Save")
        osc_button_layout.addWidget(self.osc_apply_button)
        osc_button_layout.addWidget(self.osc_send_button)
        osc_button_layout.addWidget(self.osc_save_button)

        oscilloscope_layout.addRow(osc_button_layout)

        # Add matplotlib canvas for plotting
        self.figure = plt.Figure()
        self.canvas = FigureCanvas(self.figure)
        oscilloscope_layout.addWidget(self.canvas)

        oscilloscope_group.setLayout(oscilloscope_layout)
        layout.addWidget(oscilloscope_group)

        # Accelerometer Configuration
        accel_group = QtWidgets.QGroupBox("Accelerometer Configuration")
        accel_layout = QtWidgets.QFormLayout()

        accel_sensitivity_label = QtWidgets.QLabel("Sensitivity (mV/g):")
        self.accel_sensitivity_input = QtWidgets.QLineEdit()
        accel_layout.addRow(accel_sensitivity_label, self.accel_sensitivity_input)

        accel_range_label = QtWidgets.QLabel("Range (g):")
        self.accel_range_input = QtWidgets.QLineEdit()
        accel_layout.addRow(accel_range_label, self.accel_range_input)

        # Add Apply and Send buttons
        accel_button_layout = QtWidgets.QHBoxLayout()
        self.accel_apply_button = QtWidgets.QPushButton("Apply")
        self.accel_send_button = QtWidgets.QPushButton("Send")
        accel_button_layout.addWidget(self.accel_apply_button)
        accel_button_layout.addWidget(self.accel_send_button)

        accel_layout.addRow(accel_button_layout)
        accel_group.setLayout(accel_layout)
        accel_group.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        layout.addWidget(accel_group)

        # Connect button actions
        self.func_apply_button.clicked.connect(self.apply_function_gen_settings)
        self.func_send_button.clicked.connect(self.send_function_gen_settings)
        self.osc_apply_button.clicked.connect(self.apply_oscilloscope_settings)
        self.osc_send_button.clicked.connect(self.send_oscilloscope_settings)
        self.osc_save_button.clicked.connect(self.save_waveform_data)
        self.accel_apply_button.clicked.connect(self.apply_accelerometer_settings)
        self.accel_send_button.clicked.connect(self.send_accelerometer_settings)

        self.fun_gen = None  # Will hold the function generator connection
        self.rtb = None  # Will hold the oscilloscope connection

    def get_instrument_address(self, instrument):
        # Placeholder for method to get instrument address
        # Implement this method according to how you manage instrument connections
        # For example:
        # return self.connection_tab.get_selected_instrument_address(instrument)
        return None

    def apply_function_gen_settings(self):
        try:
            waveform_type = self.func_waveform_input.currentText()
            vpp = float(self.func_vpp_input.text())
            offset = float(self.func_offset_input.text())

            if self.fun_gen is not None:
                self.fun_gen.write(f'APPL:{waveform_type} {vpp}, {offset}')
                QtWidgets.QMessageBox.information(self, "Settings Applied", "Function generator settings have been applied.")
            else:
                QtWidgets.QMessageBox.warning(self, "Connection Error", "Function generator not connected.")
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Input Error", "Please enter valid numerical values.")

    def send_function_gen_settings(self):
        try:
            waveform_type = self.func_waveform_input.currentText()
            vpp = float(self.func_vpp_input.text())
            offset = float(self.func_offset_input.text())

            address = self.get_instrument_address("Function Generator")
            if address:
                self.fun_gen = RsInstrument(address, True, True)
                self.fun_gen.write(f'APPL:{waveform_type} {vpp}, {offset}')
                QtWidgets.QMessageBox.information(self, "Settings Sent", "Function generator settings sent.")
            else:
                QtWidgets.QMessageBox.warning(self, "Connection Error", "Function generator not connected.")
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Error", f"An error occurred: {str(e)}")

    def apply_oscilloscope_settings(self):
        try:
            x_min = float(self.osc_x_min_input.text())
            x_max = float(self.osc_x_max_input.text())
            y_min = float(self.osc_y_min_input.text())
            y_max = float(self.osc_y_max_input.text())
            trigger = float(self.osc_trigger_input.text())

            if self.rtb is not None:
                self.rtb.write_str(f"TIM:ACQT {x_max - x_min}")
                self.rtb.write_str(f"CHAN1:RANG {y_max - y_min}")
                self.rtb.write_str(f"CHAN1:OFFS {(y_max + y_min) / 2}")
                self.rtb.write_str(f"TRIG:A:LEV1 {trigger}")
                QtWidgets.QMessageBox.information(self, "Settings Applied", "Oscilloscope settings have been applied.")
            else:
                QtWidgets.QMessageBox.warning(self, "Connection Error", "Oscilloscope not connected.")
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Input Error", "Please enter valid numerical values.")

    def send_oscilloscope_settings(self):
        try:
            x_min = float(self.osc_x_min_input.text())
            x_max = float(self.osc_x_max_input.text())
            y_min = float(self.osc_y_min_input.text())
            y_max = float(self.osc_y_max_input.text())
            trigger = float(self.osc_trigger_input.text())

            address = self.get_instrument_address("Oscilloscope")
            if address:
                self.rtb = RsInstrument(address, True, True)
                self.rtb.write_str(f"TIM:ACQT {x_max - x_min}")
                self.rtb.write_str(f"CHAN1:RANG {y_max - y_min}")
                self.rtb.write_str(f"CHAN1:OFFS {(y_max + y_min) / 2}")
                self.rtb.write_str(f"TRIG:A:LEV1 {trigger}")
                self.rtb.query_opc()

                # Initiate a single acquisition and wait for it to finish
                self.rtb.write_str_with_opc("SINGle", 3000)
                waveform = self.rtb.query_bin_or_ascii_float_list('FORM ASC;:CHAN1:DATA?')

                # Fetch timebase settings
                x_increment = float(self.rtb.query('CHAN1:DATA:XINC?'))
                x_origin = float(self.rtb.query('CHAN1:DATA:XOR?'))

                # Calculate time data
                time_data = np.arange(0, len(waveform)) * x_increment + x_origin

                # Plot data
                self.figure.clear()
                ax = self.figure.add_subplot(111)
                ax.plot(time_data, waveform, label='Waveform')
                ax.set_xlabel('Time (s)')
                ax.set_ylabel('Voltage (V)')
                ax.set_title('Oscilloscope Waveform')
                ax.grid(True)
                ax.legend()
                self.canvas.draw()

                QtWidgets.QMessageBox.information(self, "Data Sent", "Oscilloscope settings applied and data sent.")
            else:
                QtWidgets.QMessageBox.warning(self, "Connection Error", "Oscilloscope not connected.")
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Error", f"An error occurred: {str(e)}")

    def save_waveform_data(self):
        try:
            x_min = float(self.osc_x_min_input.text())
            x_max = float(self.osc_x_max_input.text())
            y_min = float(self.osc_y_min_input.text())
            y_max = float(self.osc_y_max_input.text())

            if self.rtb is None:
                QtWidgets.QMessageBox.warning(self, "Connection Error", "Oscilloscope not connected.")
                return

            # Fetch the waveform data
            waveform = self.rtb.query_bin_or_ascii_float_list('FORM ASC;:CHAN1:DATA?')

            # Fetch timebase settings
            x_increment = float(self.rtb.query('CHAN1:DATA:XINC?'))
            x_origin = float(self.rtb.query('CHAN1:DATA:XOR?'))

            # Calculate time data
            time_data = np.arange(0, len(waveform)) * x_increment + x_origin

            # Save waveform data to CSV file
            data = pd.DataFrame({
                'time_data': time_data,
                'waveform': waveform
            })
            csv_filename, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save File", "", "CSV Files (*.csv)")

            if csv_filename:
                data.to_csv(csv_filename, index=False)
                QtWidgets.QMessageBox.information(self, "Data Saved", f"Waveform data saved to '{csv_filename}'")

        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Error", f"An error occurred: {str(e)}")

    def apply_accelerometer_settings(self):
        try:
            sensitivity = float(self.accel_sensitivity_input.text())
            range_g = float(self.accel_range_input.text())

            # Implement accelerometer setting application logic here
            QtWidgets.QMessageBox.information(self, "Settings Applied", "Accelerometer settings have been applied.")
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Input Error", "Please enter valid numerical values.")

    def send_accelerometer_settings(self):
        try:
            sensitivity = float(self.accel_sensitivity_input.text())
            range_g = float(self.accel_range_input.text())

            # Implement accelerometer setting sending logic here
            QtWidgets.QMessageBox.information(self, "Settings Sent", "Accelerometer settings sent.")
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Error", f"An error occurred: {str(e)}")
