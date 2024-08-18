from PySide6 import QtWidgets

class DataTab(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Main layout
        layout = QtWidgets.QVBoxLayout(self)

        # Accelerometer Data
        accel_data_group = QtWidgets.QGroupBox("Accelerometer Data")
        accel_data_layout = QtWidgets.QVBoxLayout()
        accel_data_label = QtWidgets.QLabel("Accelerometer readings will appear here")
        accel_data_layout.addWidget(accel_data_label)
        accel_data_group.setLayout(accel_data_layout)
        layout.addWidget(accel_data_group)

        # Function Generator Data
        func_gen_group = QtWidgets.QGroupBox("Function Generator")
        func_gen_layout = QtWidgets.QVBoxLayout()
        func_gen_button = QtWidgets.QPushButton("Generate Function")
        func_gen_layout.addWidget(func_gen_button)
        func_gen_group.setLayout(func_gen_layout)
        layout.addWidget(func_gen_group)

        # Oscilloscope Data
        osc_data_group = QtWidgets.QGroupBox("Oscilloscope Data")
        osc_data_layout = QtWidgets.QVBoxLayout()
        osc_data_label = QtWidgets.QLabel("Oscilloscope readings will appear here")
        osc_data_layout.addWidget(osc_data_label)
        osc_data_group.setLayout(osc_data_layout)
        layout.addWidget(osc_data_group)

        # TENG Output
        teng_group = QtWidgets.QGroupBox("TENG Output")
        teng_layout = QtWidgets.QVBoxLayout()
        teng_button = QtWidgets.QPushButton("Get TENG Output")
        teng_layout.addWidget(teng_button)
        teng_group.setLayout(teng_layout)
        layout.addWidget(teng_group)
