from PySide6 import QtWidgets, QtCore
import pyvisa
from utils.resource_manager import ResourceManager

class ConnectionsTab(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Main layout with horizontal split
        main_layout = QtWidgets.QHBoxLayout(self)

        # Left Section
        left_section = QtWidgets.QWidget()
        left_layout = QtWidgets.QVBoxLayout(left_section)
        
        # Identified Devices
        self.identified_devices_group = QtWidgets.QGroupBox("Identified Devices")
        self.identified_devices_layout = QtWidgets.QVBoxLayout()

        self.refresh_button = QtWidgets.QPushButton("Refresh Available Resources")
        self.refresh_button.clicked.connect(self.refresh_resources)

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
        self.identified_devices_layout.addWidget(self.refresh_button)
        self.identified_devices_layout.addWidget(self.resources_table)
        self.identified_devices_group.setLayout(self.identified_devices_layout)

        left_layout.addWidget(self.identified_devices_group)
        left_section.setLayout(left_layout)
        
        # Right Section
        right_section = QtWidgets.QWidget()
        right_layout = QtWidgets.QVBoxLayout(right_section)

        self.instruments_group = QtWidgets.QGroupBox("Instruments")
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
            device_dropdown.addItem("Select a device")  # Placeholder text
            group_layout.addRow("Device:", device_dropdown)
            
            # Select button
            select_button = QtWidgets.QPushButton("Select")
            self.instruments[instrument]['select_button'] = select_button
            select_button.clicked.connect(lambda checked, inst=instrument: self.select_device(inst))
            group_layout.addWidget(select_button)

            # Disconnect button
            disconnect_button = QtWidgets.QPushButton("Disconnect")
            self.instruments[instrument]['disconnect_button'] = disconnect_button
            disconnect_button.clicked.connect(lambda checked, inst=instrument: self.disconnect_device(inst))
            disconnect_button.setEnabled(False)
            group_layout.addWidget(disconnect_button)

            # Add the group box to the layout
            group_box.setLayout(group_layout)
            instruments_layout.addWidget(group_box)
        
        self.instruments_group.setLayout(instruments_layout)
        right_section.setLayout(right_layout)

        # Add sections to main layout
        main_layout.addWidget(left_section, stretch=1)
        main_layout.addWidget(right_section, stretch=1)

        # Initialize selected_instruments dictionary
        self.selected_instruments = {
            "Function Generator": None,
            "Oscilloscope": None,
            "Accelerometer": None
        }

        # Handle app close event
        self.app = QtWidgets.QApplication.instance()
        self.app.aboutToQuit.connect(self.disconnect_all_instruments)

        # Refresh resources initially
        self.refresh_resources()

    def refresh_resources(self):
        try:
            # Get list of resources from ResourceManager
            resources = ResourceManager().list_resources()
            
            # Clear previous data
            self.resources_table.setRowCount(0)
            
            # Populate the table with available resources
            for index, resource in enumerate(resources):
                if index >= 15:
                    break
                row_position = self.resources_table.rowCount()
                self.resources_table.insertRow(row_position)
                
                resource_item = QtWidgets.QTableWidgetItem(resource)
                idn_item = QtWidgets.QTableWidgetItem(self.get_idn(resource))
                
                self.resources_table.setItem(row_position, 0, resource_item)
                self.resources_table.setItem(row_position, 1, idn_item)

            # Update instrument dropdowns
            self.update_device_dropdowns()
            
        except Exception as e:
            print(f"Error refreshing resources: {e}")  # Debugging line

    def update_device_dropdowns(self):
        # Get list of resources from ResourceManager
        resources = ResourceManager().list_resources()
        for instrument, controls in self.instruments.items():
            dropdown = controls['dropdown']
            current_selection = dropdown.currentText()
            
            dropdown.clear()
            dropdown.addItem("Select a device")  # Placeholder text
            dropdown.addItems(resources)
            
            # Remove currently selected item if it exists in the new list
            if current_selection in resources:
                dropdown.setCurrentText(current_selection)
            else:
                dropdown.setCurrentIndex(0)  # Set placeholder if previously selected item is not in the list

    def select_device(self, instrument):
        dropdown = self.instruments[instrument]['dropdown']
        selected_resource = dropdown.currentText()
        if selected_resource and selected_resource != "Select a device":
            self.selected_instruments[instrument] = selected_resource
            print(f"Selected {instrument}: {selected_resource}")  # Debugging line
            self.remove_resource_from_table(selected_resource)
            self.instruments[instrument]['dropdown'].setEnabled(False)
            self.instruments[instrument]['select_button'].setEnabled(False)
            self.instruments[instrument]['disconnect_button'].setEnabled(True)

    def disconnect_device(self, instrument):
        selected_resource = self.selected_instruments[instrument]
        if selected_resource:
            self.add_resource_to_table(selected_resource)
            self.selected_instruments[instrument] = None
            self.instruments[instrument]['dropdown'].setEnabled(True)
            self.instruments[instrument]['select_button'].setEnabled(True)
            self.instruments[instrument]['disconnect_button'].setEnabled(False)
            print(f"Disconnected {instrument}: {selected_resource}")  # Debugging line

    def get_idn(self, resource_address):
        try:
            rm = ResourceManager().get_instance()
            instrument = rm.open_resource(resource_address)

            # Try sending the *IDN? command
            try:
                idn = instrument.query("*IDN?")
                return idn.strip()
            except Exception as query_error:
                return f"IDN Query Failed: {str(query_error)}"

        except Exception as e:
            return f"Connection Failed: {str(e)}"

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

    def disconnect_all_instruments(self):
        for instrument, resource in self.selected_instruments.items():
            if resource:
                print(f"Disconnecting {instrument}: {resource}")  # Debugging line
                self.disconnect_device(instrument)
