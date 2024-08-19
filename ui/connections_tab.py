from PySide6 import QtWidgets, QtCore
import pyvisa
from utils.resource_manager import ResourceManager

class ConnectionsTab(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Main layout: Split screen vertically into two equal sections
        main_layout = QtWidgets.QHBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)  # Remove margins for a clean split

        # Left section: Identified Devices
        left_section = QtWidgets.QVBoxLayout()
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

        left_section.addWidget(identified_devices_group)
        left_section.addStretch(1)  # Add stretch to push content to the top

        # Right section: Instruments
        right_section = QtWidgets.QVBoxLayout()
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
            
            # Disconnect button
            disconnect_button = QtWidgets.QPushButton("Disconnect")
            self.instruments[instrument]['disconnect'] = disconnect_button
            disconnect_button.clicked.connect(lambda checked, inst=instrument: self.disconnect_device(inst))
            disconnect_button.setEnabled(False)
            group_layout.addWidget(disconnect_button)

            # Add the group box to the layout
            group_box.setLayout(group_layout)
            instruments_layout.addWidget(group_box)
        
        instruments_group.setLayout(instruments_layout)
        right_section.addWidget(instruments_group)
        right_section.addStretch(1)  # Add stretch to push content to the top

        # Add sections to the main layout
        main_layout.addLayout(left_section, stretch=1)
        main_layout.addLayout(right_section, stretch=1)

        # Connect button actions
        self.identify_button.clicked.connect(self.identify_resources)

        # Dictionary to store selected instruments
        self.selected_instruments = {
            "Function Generator": None,
            "Oscilloscope": None,
            "Accelerometer": None
        }

    def update_device_dropdowns(self):
        try:
            resources = ResourceManager().list_resources()
            unique_resources = list(set(resources))  # Remove duplicates
            for instrument, controls in self.instruments.items():
                dropdown = controls['dropdown']
                current_selection = dropdown.currentText()
                dropdown.clear()
                dropdown.addItem("Select a device")  # Default text
                dropdown.addItems(unique_resources)
                # Restore previous selection if still available
                if current_selection in unique_resources:
                    dropdown.setCurrentText(current_selection)
        except Exception as e:
            print(f"Error updating device dropdowns: {e}")

    def select_device(self, instrument):
        dropdown = self.instruments[instrument]['dropdown']
        selected_resource = dropdown.currentText()
        if selected_resource and selected_resource != "Select a device":
            self.selected_instruments[instrument] = selected_resource
            print(f"Selected {instrument}: {selected_resource}")  # Debugging line
            self.remove_resource_from_table(selected_resource)
            dropdown.setEnabled(False)
            self.instruments[instrument]['button'].setEnabled(False)
            self.instruments[instrument]['disconnect'].setEnabled(True)

    def disconnect_device(self, instrument):
        selected_resource = self.selected_instruments[instrument]
        if selected_resource:
            self.add_resource_to_table(selected_resource)
            self.selected_instruments[instrument] = None
            self.instruments[instrument]['dropdown'].setEnabled(True)
            self.instruments[instrument]['button'].setEnabled(True)
            self.instruments[instrument]['disconnect'].setEnabled(False)
            print(f"Disconnected {instrument}: {selected_resource}")  # Debugging line

    def identify_resources(self):
        try:
            resources = ResourceManager().list_resources()
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
            # Update dropdowns after identifying resources
            self.update_device_dropdowns()
        except Exception as e:
            print(f"Error identifying resources: {e}")  # Debugging line

    def get_idn(self, resource_address):
        try:
            rm = pyvisa.ResourceManager()
            instrument = rm.open_resource(resource_address)
            idn = instrument.query("*IDN?")
            return idn.strip()
        except Exception as e:
            return f"Error: {str(e)}"

    def remove_resource_from_table(self, resource_address):
        for row in range(self.resources_table.rowCount()):
            if self.resources_table.item(row, 0) and self.resources_table.item(row, 0).text() == resource_address:
                self.resources_table.removeRow(row)
                break

    def add_resource_to_table(self, resource_address):
        idn = self.get_idn(resource_address)
        row_position = self.resources_table.rowCount()
        self.resources_table.insertRow(row_position)
        self.resources_table.setItem(row_position, 0, QtWidgets.QTableWidgetItem(resource_address))
        self.resources_table.setItem(row_position, 1, QtWidgets.QTableWidgetItem(idn))
