from PySide6 import QtWidgets, QtCore
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from RsInstrument import RsInstrument
import serial.tools.list_ports

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

        # Top Right: Configuration Widgets
        self.configurations_widget = QtWidgets.QWidget()
        self.configurations_layout = QtWidgets.QVBoxLayout(self.configurations_widget)
        self.configurations_widget.setLayout(self.configurations_layout)
        layout.addWidget(self.configurations_widget, 0, 1)

        # Device Configuration Section
        self.device_config_widget = QtWidgets.QWidget()
        self.device_config_layout = QtWidgets.QVBoxLayout(self.device_config_widget)
        self.device_config_widget.setLayout(self.device_config_layout)
        self.configurations_layout.addWidget(self.device_config_widget)

        # Identify Connected Devices Button
        self.identify_devices_button = QtWidgets.QPushButton("Identify Connected Devices")
        self.identify_devices_button.clicked.connect(self.identify_connected_devices)

        # Table for displaying connected devices
        self.devices_table = QtWidgets.QTableWidget()
        self.devices_table.setColumnCount(2)
        self.devices_table.setHorizontalHeaderLabels(["Device Type", "Device Address"])
        self.devices_table.horizontalHeader().setStretchLastSection(True)

        # Save Button
        self.save_devices_button = QtWidgets.QPushButton("Save")
        self.save_devices_button.clicked.connect(self.save_device_settings)

        # Add the button and table to the device config layout
        self.device_config_layout.addWidget(self.identify_devices_button)
        self.device_config_layout.addWidget(self.devices_table)
        self.device_config_layout.addWidget(self.save_devices_button)

        # Oscilloscope Configuration
        self.oscilloscope_group = QtWidgets.QGroupBox("Oscilloscope Configuration")
        self.oscilloscope_layout = QtWidgets.QFormLayout(self.oscilloscope_group)
        self.oscilloscope_group.setLayout(self.oscilloscope_layout)
        self.configurations_layout.addWidget(self.oscilloscope_group)

        # Inputs for Oscilloscope
        osc_x_min_label = QtWidgets.QLabel("X Min:")
        self.osc_x_min_input = QtWidgets.QLineEdit()
        self.oscilloscope_layout.addRow(osc_x_min_label, self.osc_x_min_input)

        osc_x_max_label = QtWidgets.QLabel("X Max:")
        self.osc_x_max_input = QtWidgets.QLineEdit()
        self.oscilloscope_layout.addRow(osc_x_max_label, self.osc_x_max_input)

        osc_y_range_label = QtWidgets.QLabel("Y Range:")
        self.osc_y_range_input = QtWidgets.QLineEdit()
        self.oscilloscope_layout.addRow(osc_y_range_label, self.osc_y_range_input)

        osc_trigger_label = QtWidgets.QLabel("Trigger Value:")
        self.osc_trigger_input = QtWidgets.QLineEdit()
        self.oscilloscope_layout.addRow(osc_trigger_label, self.osc_trigger_input)

        # Add Apply, Send, and Save buttons for Oscilloscope
        osc_button_layout = QtWidgets.QHBoxLayout()
        self.osc_apply_button = QtWidgets.QPushButton("Apply")
        self.osc_send_button = QtWidgets.QPushButton("Send")
        self.osc_save_button = QtWidgets.QPushButton("Save")
        osc_button_layout.addWidget(self.osc_apply_button)
        osc_button_layout.addWidget(self.osc_send_button)
        osc_button_layout.addWidget(self.osc_save_button)
        self.oscilloscope_layout.addRow(osc_button_layout)

        # Function Generator Configuration
        self.func_waveform_input = QtWidgets.QComboBox()
        self.func_waveform_input.addItems(["SINE", "SQUARE", "TRIANGLE"])
        self.func_vpp_input = QtWidgets.QLineEdit()
        self.func_offset_input = QtWidgets.QLineEdit()
        self.func_freq_input = QtWidgets.QLineEdit()

        # Adding the Function Generator input fields to the layout
        self.oscilloscope_layout.addRow(QtWidgets.QLabel("Waveform Type:"), self.func_waveform_input)
        self.oscilloscope_layout.addRow(QtWidgets.QLabel("Vpp:"), self.func_vpp_input)
        self.oscilloscope_layout.addRow(QtWidgets.QLabel("Offset:"), self.func_offset_input)
        self.oscilloscope_layout.addRow(QtWidgets.QLabel("Frequency:"), self.func_freq_input)

        # Adding the Function Generator configuration buttons
        func_button_layout = QtWidgets.QHBoxLayout()
        self.func_apply_button = QtWidgets.QPushButton("Apply")
        self.func_send_button = QtWidgets.QPushButton("Send")
        self.func_save_button = QtWidgets.QPushButton("Save")
        func_button_layout.addWidget(self.func_apply_button)
        func_button_layout.addWidget(self.func_send_button)
        func_button_layout.addWidget(self.func_save_button)

        # Add them to the layout
        self.oscilloscope_layout.addRow(func_button_layout)

        # Connect button actions
        self.func_apply_button.clicked.connect(self.apply_function_gen_settings)
        self.func_send_button.clicked.connect(self.send_function_gen_settings)
        self.osc_apply_button.clicked.connect(self.apply_oscilloscope_settings)
        self.osc_send_button.clicked.connect(self.send_oscilloscope_settings)
        self.osc_save_button.clicked.connect(self.save_waveform_data)
        self.save_devices_button.clicked.connect(self.save_device_settings)
        self.identify_devices_button.clicked.connect(self.identify_connected_devices)

        # Placeholders for instrument connections
        self.fun_gen = None  # Function generator connection
        self.rtb = None  # Oscilloscope connection

    def identify_connected_devices(self):
        # Example implementation of device identification
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

    def save_device_settings(self):
        # Save device settings
        QtWidgets.QMessageBox.information(self, "Save Settings", "Device settings saved successfully.")

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
            y_range = float(self.osc_y_range_input.text())
            trigger = float(self.osc_trigger_input.text())

            if self.rtb is not None:
                self.rtb.write_str(f"TIM:ACQT {x_max - x_min}")
                self.rtb.write_str(f"CHAN1:RANG {y_range}")
                self.rtb.write_str(f"CHAN1:OFFS {y_range / 2}")
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
            y_range = float(self.osc_y_range_input.text())
            trigger = float(self.osc_trigger_input.text())

            address = self.get_instrument_address("Oscilloscope")
            if address:
                self.rtb = RsInstrument(address, True, True)
                self.rtb.write_str(f"TIM:ACQT {x_max - x_min}")
                self.rtb.write_str(f"CHAN1:RANG {y_range}")
                self.rtb.write_str(f"CHAN1:OFFS {y_range / 2}")
                self.rtb.write_str(f"TRIG:LEVEL {trigger}")
                QtWidgets.QMessageBox.information(self, "Settings Sent", "Oscilloscope settings sent.")
            else:
                QtWidgets.QMessageBox.warning(self, "Connection Error", "Oscilloscope not connected.")
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Error", f"An error occurred: {str(e)}")

    def save_waveform_data(self):
        # Placeholder for saving waveform data
        QtWidgets.QMessageBox.information(self, "Save Data", "Waveform data has been saved.")

    def save_accelerometer_settings(self):
        try:
            com_port = int(self.accel_com_input.text())
            if self.is_com_port_available(com_port):
                QtWidgets.QMessageBox.information(self, "COM Port Status", f"COM port {com_port} is available.")
            else:
                QtWidgets.QMessageBox.warning(self, "COM Port Status", f"COM port {com_port} is occupied.")
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Input Error", "Please enter a valid COM port number.")

    def is_com_port_available(self, com_port):
        ports = [port.device for port in serial.tools.list_ports.comports()]
        return f"COM{com_port}" not in ports

    def get_instrument_address(self, instrument):
        # Placeholder for method to get instrument address
        # Implement this method according to how you manage instrument connections
        return None
