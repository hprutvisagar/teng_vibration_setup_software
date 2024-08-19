from PySide6 import QtWidgets, QtCore
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from RsInstrument import RsInstrument

class TestMeasurementSetupTab(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Main layout
        layout = QtWidgets.QGridLayout(self)
        self.setLayout(layout)

        # Define the grid layout areas
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 1)
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)

        # Top Left: Identify Connected Devices
        self.identify_devices_group = QtWidgets.QGroupBox("Identify Connected Devices")
        self.identify_devices_layout = QtWidgets.QVBoxLayout()

        # Identify Connected Devices Button
        self.identify_devices_button = QtWidgets.QPushButton("Identify Connected Devices")
        self.identify_devices_button.clicked.connect(self.identify_connected_devices)
        
        # Table for displaying connected devices
        self.devices_table = QtWidgets.QTableWidget()
        self.devices_table.setColumnCount(2)
        self.devices_table.setHorizontalHeaderLabels(["Device Type", "Device Address"])
        self.devices_table.horizontalHeader().setStretchLastSection(True)
        
        # Adding the button and table to the layout
        self.identify_devices_layout.addWidget(self.identify_devices_button)
        self.identify_devices_layout.addWidget(self.devices_table)
        self.identify_devices_group.setLayout(self.identify_devices_layout)
        layout.addWidget(self.identify_devices_group, 0, 0)

        # Top Right: Instrument Connections
        self.instrument_connections_group = QtWidgets.QGroupBox("Instrument Connections")
        self.instrument_connections_layout = QtWidgets.QVBoxLayout()
        self.instrument_connections_group.setLayout(self.instrument_connections_layout)
        layout.addWidget(self.instrument_connections_group, 0, 1)

        # Bottom Left: Oscilloscope Section
        self.oscilloscope_group = QtWidgets.QGroupBox("Oscilloscope Section")
        self.oscilloscope_layout = QtWidgets.QVBoxLayout()
        self.oscilloscope_group.setLayout(self.oscilloscope_layout)
        layout.addWidget(self.oscilloscope_group, 1, 0)

        # Bottom Right: Accelerometer Data
        self.accelerometer_group = QtWidgets.QGroupBox("Accelerometer Data")
        self.accelerometer_layout = QtWidgets.QVBoxLayout()
        self.accelerometer_group.setLayout(self.accelerometer_layout)
        layout.addWidget(self.accelerometer_group, 1, 1)

        # Add Function Generator Configuration
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

        func_freq_label = QtWidgets.QLabel("Frequency (Hz):")
        self.func_freq_input = QtWidgets.QLineEdit()
        function_gen_layout.addRow(func_freq_label, self.func_freq_input)

        # Add Apply and Send buttons
        func_button_layout = QtWidgets.QHBoxLayout()
        self.func_apply_button = QtWidgets.QPushButton("Apply")
        self.func_send_button = QtWidgets.QPushButton("Send")
        func_button_layout.addWidget(self.func_apply_button)
        func_button_layout.addWidget(self.func_send_button)

        function_gen_layout.addRow(func_button_layout)
        function_gen_group.setLayout(function_gen_layout)

        # Add to Top Right Section
        self.instrument_connections_layout.addWidget(function_gen_group)

        # Add Oscilloscope Configuration
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

        # Add to Bottom Left Section
        self.oscilloscope_layout.addWidget(oscilloscope_group)

        # Add Accelerometer Configuration
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

        # Add to Bottom Right Section
        self.accelerometer_layout.addWidget(accel_group)

        # Connect button actions
        self.func_apply_button.clicked.connect(self.apply_function_gen_settings)
        self.func_send_button.clicked.connect(self.send_function_gen_settings)
        self.osc_apply_button.clicked.connect(self.apply_oscilloscope_settings)
        self.osc_send_button.clicked.connect(self.send_oscilloscope_settings)
        self.osc_save_button.clicked.connect(self.save_waveform_data)
        self.accel_apply_button.clicked.connect(self.apply_accelerometer_settings)
        self.accel_send_button.clicked.connect(self.send_accelerometer_settings)
        self.identify_devices_button.clicked.connect(self.identify_connected_devices)

        self.fun_gen = None  # Will hold the function generator connection
        self.rtb = None  # Will hold the oscilloscope connection

    def identify_connected_devices(self):
        # Example implementation of device identification
        # Replace this with actual logic to detect and identify devices
        connected_devices = [
            ("Function Generator", "Address 1"),
            ("Oscilloscope", "Address 2"),
            ("Accelerometer", "Address 3")
        ]
        
        self.devices_table.setRowCount(len(connected_devices))
        for row, (device_type, device_address) in enumerate(connected_devices):
            self.devices_table.setItem(row, 0, QtWidgets.QTableWidgetItem(device_type))
            self.devices_table.setItem(row, 1, QtWidgets.QTableWidgetItem(device_address))
        
        QtWidgets.QMessageBox.information(self, "Identify Devices", "Connected devices identified and displayed in the table.")

    def get_instrument_address(self, instrument):
        # Placeholder for method to get instrument address
        # Implement this method according to how you manage instrument connections
        return None

    def apply_function_gen_settings(self):
        try:
            waveform_type = self.func_waveform_input.currentText()
            vpp = float(self.func_vpp_input.text())
            offset = float(self.func_offset_input.text())
            freq = float(self.func_freq_input.text())

            if self.fun_gen is not None:
                self.fun_gen.write(f'APPL:{waveform_type} {vpp}, {offset}, {freq}')
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
            freq = float(self.func_freq_input.text())

            address = self.get_instrument_address("Function Generator")
            if address:
                self.fun_gen = RsInstrument(address, True, True)
                self.fun_gen.write(f'APPL:{waveform_type} {vpp}, {offset}, {freq}')
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
                self.rtb.write_str(f"TRIG:LEVEL {trigger}")
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
                self.rtb.write_str(f"TRIG:LEVEL {trigger}")
                QtWidgets.QMessageBox.information(self, "Settings Sent", "Oscilloscope settings sent.")
            else:
                QtWidgets.QMessageBox.warning(self, "Connection Error", "Oscilloscope not connected.")
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Error", f"An error occurred: {str(e)}")

    def save_waveform_data(self):
        # Placeholder for saving waveform data
        QtWidgets.QMessageBox.information(self, "Save Data", "Waveform data has been saved.")

    def apply_accelerometer_settings(self):
        try:
            sensitivity = float(self.accel_sensitivity_input.text())
            range_ = float(self.accel_range_input.text())

            # Implement logic to apply accelerometer settings
            QtWidgets.QMessageBox.information(self, "Settings Applied", "Accelerometer settings have been applied.")
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Input Error", "Please enter valid numerical values.")

    def send_accelerometer_settings(self):
        try:
            sensitivity = float(self.accel_sensitivity_input.text())
            range_ = float(self.accel_range_input.text())

            # Implement logic to send accelerometer settings
            QtWidgets.QMessageBox.information(self, "Settings Sent", "Accelerometer settings sent.")
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Input Error", "Please enter valid numerical values.")
