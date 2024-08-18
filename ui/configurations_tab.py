from PySide6 import QtWidgets

class ConfigurationsTab(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Main layout
        layout = QtWidgets.QVBoxLayout(self)

        # Oscilloscope Configuration
        oscilloscope_group = QtWidgets.QGroupBox("Oscilloscope Configuration")
        oscilloscope_layout = QtWidgets.QFormLayout()

        osc_timebase_label = QtWidgets.QLabel("Timebase (ms/div):")
        self.osc_timebase_input = QtWidgets.QLineEdit()
        oscilloscope_layout.addRow(osc_timebase_label, self.osc_timebase_input)

        osc_volts_per_div_label = QtWidgets.QLabel("Volts/Div:")
        self.osc_volts_per_div_input = QtWidgets.QLineEdit()
        oscilloscope_layout.addRow(osc_volts_per_div_label, self.osc_volts_per_div_input)

        oscilloscope_group.setLayout(oscilloscope_layout)
        layout.addWidget(oscilloscope_group)

        # Function Generator Configuration
        function_gen_group = QtWidgets.QGroupBox("Function Generator Configuration")
        function_gen_layout = QtWidgets.QFormLayout()

        func_waveform_label = QtWidgets.QLabel("Waveform Type:")
        self.func_waveform_input = QtWidgets.QLineEdit()
        function_gen_layout.addRow(func_waveform_label, self.func_waveform_input)

        function_gen_group.setLayout(function_gen_layout)
        layout.addWidget(function_gen_group)

        # Accelerometer Configuration
        accel_group = QtWidgets.QGroupBox("Accelerometer Configuration")
        accel_layout = QtWidgets.QFormLayout()

        accel_sensitivity_label = QtWidgets.QLabel("Sensitivity (mV/g):")
        self.accel_sensitivity_input = QtWidgets.QLineEdit()
        accel_layout.addRow(accel_sensitivity_label, self.accel_sensitivity_input)

        accel_range_label = QtWidgets.QLabel("Range (g):")
        self.accel_range_input = QtWidgets.QLineEdit()
        accel_layout.addRow(accel_range_label, self.accel_range_input)

        accel_group.setLayout(accel_layout)
        layout.addWidget(accel_group)

        # Apply and Reset buttons
        self.apply_button = QtWidgets.QPushButton("Apply")
        self.reset_button = QtWidgets.QPushButton("Reset")
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(self.apply_button)
        button_layout.addWidget(self.reset_button)

        layout.addLayout(button_layout)
