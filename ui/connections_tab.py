from PySide6 import QtWidgets, QtCore
from utils.resource_manager import ResourceManager

class ConnectionsTab(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Main layout
        layout = QtWidgets.QVBoxLayout(self)

        # Identified Devices
        identified_devices_group = QtWidgets.QGroupBox("Identified Devices")
        identified_devices_layout = QtWidgets.QVBoxLayout()

        self.identify_button = QtWidgets.QPushButton("Identify Connected Resources")

        # Create the QTableWidget for displaying resources
        self.resources_table = QtWidgets.QTableWidget()
        self.resources_table.setColumnCount(2)
        self.resources_table.setHorizontalHeaderLabels(["Resource Address", "IDN"])
        self.resources_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        
        # Set column widths
        self.resources_table.setColumnWidth(0, 50 * 10)  # 50 characters width, estimated at 10 pixels per character
        self.resources_table.setColumnWidth(1, 400)  # Adjust as needed for the second column

        # Set a maximum number of rows
        self.resources_table.setRowCount(15)
        self.resources_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.resources_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)

        # Hide row headers
        self.resources_table.verticalHeader().setVisible(False)

        # Add widgets to layout
        identified_devices_layout.addWidget(self.identify_button)
        identified_devices_layout.addWidget(self.resources_table)
        identified_devices_group.setLayout(identified_devices_layout)
        
        # Set the maximum height of the group box
        identified_devices_group.setMaximumHeight(300)  # Adjust this value as needed

        layout.addWidget(identified_devices_group)

        # Instruments Section
        instruments_group = QtWidgets.QGroupBox("Instruments")
        instruments_layout = QtWidgets.QVBoxLayout()

        self.instruments = {
            "Function Generator": {},
            "Oscilloscope": {},
            "Accelerometer": {}
        }

        for instrument in self.instruments.keys():
            group_box = QtWidgets.QGroupBox(instrument)
            group_layout = QtWidgets.QFormLayout()
            
            # Device dropdown
            device_dropdown = QtWidgets.QComboBox()
            self.instruments[instrument]['dropdown'] = device_dropdown
            group_layout.addRow("Device:", device_dropdown)
            
            # Select button
            select_button = QtWidgets.QPushButton("Select")
            self.instruments[instrument]['button'] = select_button
            select_button.clicked.connect(lambda checked, inst=instrument: self.select_device(inst))
            group_layout.addWidget(select_button)
            
            # Add the group box to the layout
            group_box.setLayout(group_layout)
            instruments_layout.addWidget(group_box)
        
        instruments_group.setLayout(instruments_layout)
        layout.addWidget(instruments_group)

        # Connect button actions
        self.identify_button.clicked.connect(self.identify_resources)
        self.update_device_dropdowns()

        # Dictionary to store selected instruments
        self.selected_instruments = {
            "Function Generator": None,
            "Oscilloscope": None,
            "Accelerometer": None
        }

    def update_device_dropdowns(self):
        resources = ResourceManager.list_resources()
        for instrument, controls in self.instruments.items():
            dropdown = controls['dropdown']
            dropdown.clear()
            dropdown.addItems(resources)

    def select_device(self, instrument):
        dropdown = self.instruments[instrument]['dropdown']
        selected_resource = dropdown.currentText()
        self.selected_instruments[instrument] = selected_resource
        print(f"Selected {instrument}: {selected_resource}")  # Debugging line

    def identify_resources(self):
        try:
            resources = ResourceManager.list_resources()
            print("Resources found:", resources)  # Debugging line
            
            self.resources_table.setRowCount(0)
            for index, resource in enumerate(resources):
                if index >= 15:
                    break
                row_position = self.resources_table.rowCount()
                self.resources_table.insertRow(row_position)
                
                resource_item = QtWidgets.QTableWidgetItem(resource)
                idn_item = QtWidgets.QTableWidgetItem(self.get_idn(resource))
                
                self.resources_table.setItem(row_position, 0, resource_item)
                self.resources_table.setItem(row_position, 1, idn_item)
        except Exception as e:
            print(f"Error identifying resources: {e}")  # Debugging line

    def get_idn(self, resource_address):
        try:
            rm = ResourceManager.get_instance()
            instrument = rm.open_resource(resource_address)
            idn = instrument.query("*IDN?")
            return idn.strip()
        except Exception as e:
            return f"Error: {str(e)}"
