import sys
from PySide6 import QtCore, QtWidgets, QtGui
import pyvisa

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Main layout for the entire window
        main_layout = QtWidgets.QVBoxLayout(self)

        # Create a QTabWidget
        tab_widget = QtWidgets.QTabWidget()

        # Tab 1: Connections
        connect_tab = QtWidgets.QWidget()
        connect_layout = QtWidgets.QVBoxLayout(connect_tab)

        # Section for identifying connected resources
        identify_group = QtWidgets.QGroupBox("Identify Connected Resources")
        identify_layout = QtWidgets.QVBoxLayout()

        self.identify_button = QtWidgets.QPushButton("Identify Connected Resources")
        self.resources_display = QtWidgets.QTextEdit()
        self.resources_display.setReadOnly(True)

        identify_layout.addWidget(self.identify_button)
        identify_layout.addWidget(self.resources_display)

        identify_group.setLayout(identify_layout)
        connect_layout.addWidget(identify_group)

        # Section for Oscilloscope
        oscilloscope_conn_group = QtWidgets.QGroupBox("Oscilloscope Connection")
        oscilloscope_conn_layout = QtWidgets.QVBoxLayout()

        # COM Port Input
        com_port_layout = QtWidgets.QFormLayout()
        self.com_port_input = QtWidgets.QLineEdit()
        com_port_layout.addRow("COM Port:", self.com_port_input)
        oscilloscope_conn_layout.addLayout(com_port_layout)

        # Buttons for Oscilloscope
        button_layout = QtWidgets.QHBoxLayout()
        self.connect_button = QtWidgets.QPushButton("Connect")
        self.disconnect_button = QtWidgets.QPushButton("Disconnect")
        button_layout.addWidget(self.connect_button)
        button_layout.addWidget(self.disconnect_button)
        oscilloscope_conn_layout.addLayout(button_layout)

        oscilloscope_conn_group.setLayout(oscilloscope_conn_layout)
        connect_layout.addWidget(oscilloscope_conn_group)

        # Adding Connections tab to the QTabWidget
        tab_widget.addTab(connect_tab, "Connections")

        # Tab 2: Configurations
        config_tab = QtWidgets.QWidget()
        config_layout = QtWidgets.QVBoxLayout(config_tab)

        # Section for Oscilloscope Configuration
        oscilloscope_group = QtWidgets.QGroupBox("Oscilloscope Configuration")
        oscilloscope_layout = QtWidgets.QFormLayout()

        osc_timebase_label = QtWidgets.QLabel("Timebase (ms/div):")
        self.osc_timebase_input = QtWidgets.QLineEdit()
        oscilloscope_layout.addRow(osc_timebase_label, self.osc_timebase_input)

        osc_volts_per_div_label = QtWidgets.QLabel("Volts/Div:")
        self.osc_volts_per_div_input = QtWidgets.QLineEdit()
        oscilloscope_layout.addRow(osc_volts_per_div_label, self.osc_volts_per_div_input)

        oscilloscope_group.setLayout(oscilloscope_layout)
        config_layout.addWidget(oscilloscope_group)

        # Section for Function Generator Configuration
        function_gen_group = QtWidgets.QGroupBox("Function Generator Configuration")
        function_gen_layout = QtWidgets.QFormLayout()

        func_waveform_label = QtWidgets.QLabel("Waveform Type:")
        self.func_waveform_input = QtWidgets.QLineEdit()
        function_gen_layout.addRow(func_waveform_label, self.func_waveform_input)

        function_gen_group.setLayout(function_gen_layout)
        config_layout.addWidget(function_gen_group)

        # Section for Accelerometer Configuration
        accel_group = QtWidgets.QGroupBox("Accelerometer Configuration")
        accel_layout = QtWidgets.QFormLayout()

        accel_sensitivity_label = QtWidgets.QLabel("Sensitivity (mV/g):")
        self.accel_sensitivity_input = QtWidgets.QLineEdit()
        accel_layout.addRow(accel_sensitivity_label, self.accel_sensitivity_input)

        accel_range_label = QtWidgets.QLabel("Range (g):")
        self.accel_range_input = QtWidgets.QLineEdit()
        accel_layout.addRow(accel_range_label, self.accel_range_input)

        accel_group.setLayout(accel_layout)
        config_layout.addWidget(accel_group)

        # Apply and Reset buttons
        self.apply_button = QtWidgets.QPushButton("Apply")
        self.reset_button = QtWidgets.QPushButton("Reset")
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(self.apply_button)
        button_layout.addWidget(self.reset_button)

        config_layout.addLayout(button_layout)

        # Adding Configurations tab to the QTabWidget
        tab_widget.addTab(config_tab, "Configurations")

        # Tab 3: Data
        data_tab = QtWidgets.QWidget()
        data_layout = QtWidgets.QVBoxLayout(data_tab)

        # Accelerometer Data
        accel_data_group = QtWidgets.QGroupBox("Accelerometer Data")
        accel_data_layout = QtWidgets.QVBoxLayout()
        accel_data_label = QtWidgets.QLabel("Accelerometer readings will appear here")
        accel_data_layout.addWidget(accel_data_label)
        accel_data_group.setLayout(accel_data_layout)
        data_layout.addWidget(accel_data_group)

        # Function Generator
        func_gen_group = QtWidgets.QGroupBox("Function Generator")
        func_gen_layout = QtWidgets.QVBoxLayout()
        func_gen_button = QtWidgets.QPushButton("Generate Function")
        func_gen_layout.addWidget(func_gen_button)
        func_gen_group.setLayout(func_gen_layout)
        data_layout.addWidget(func_gen_group)

        # Oscilloscope Data
        osc_data_group = QtWidgets.QGroupBox("Oscilloscope Data")
        osc_data_layout = QtWidgets.QVBoxLayout()
        osc_data_label = QtWidgets.QLabel("Oscilloscope readings will appear here")
        osc_data_layout.addWidget(osc_data_label)
        osc_data_group.setLayout(osc_data_layout)
        data_layout.addWidget(osc_data_group)

        # TENG Output
        teng_group = QtWidgets.QGroupBox("TENG Output")
        teng_layout = QtWidgets.QVBoxLayout()
        teng_button = QtWidgets.QPushButton("Get TENG Output")
        teng_layout.addWidget(teng_button)
        teng_group.setLayout(teng_layout)
        data_layout.addWidget(teng_group)

        # Adding Data tab to the QTabWidget
        tab_widget.addTab(data_tab, "Data")

        # Adding the QTabWidget to the main layout
        main_layout.addWidget(tab_widget)

        self.setLayout(main_layout)

        # Connect button actions
        self.connect_button.clicked.connect(self.connect_oscilloscope)
        self.identify_button.clicked.connect(self.identify_resources)

    def connect_oscilloscope(self):
        com_port = self.com_port_input.text()
        print(f"Connecting to oscilloscope on {com_port}")

    def identify_resources(self):
        rm = pyvisa.ResourceManager()
        resources = rm.list_resources()
        # Limit the output to 10 lines
        resources_display_text = "\n".join(resources[:10])
        if len(resources) > 10:
            resources_display_text += "\n... (more resources available)"
        self.resources_display.setText(resources_display_text)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.showMaximized()  # Show the window maximized
    sys.exit(app.exec())
