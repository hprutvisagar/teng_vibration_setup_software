from PySide6 import QtWidgets, QtCore
import pyvisa
from utils.resource_manager import ResourceManager

class ConnectionsTab(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Main layout: Use QSplitter to create two equal sections
        main_layout = QtWidgets.QHBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)  # Remove margins for a clean layout

        # Create QSplitter
        splitter = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        
        # Left section: Identified Devices
        left_widget = QtWidgets.QWidget()
        left_section = QtWidgets.QVBoxLayout(left_widget)
        
        identified_devices_group = QtWidgets.QGroupBox("Identified Devices")
        identified_devices_layout = QtWidgets.QVBoxLayout()

        self.identify_button = QtWidgets.QPushButton("Identify Connected Resources")

        # Create the QTableWidget for displaying resources
        self.resources_table = QtWidgets.QTableWidget()
        self.resources_table.setColumnCount(2)
        self.resources_table.setHorizontalHeaderLabels(["Resource Address", "IDN"])
        self.resources_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        # Set column widths
        self.resources_table.setColumnWidth(0, 25 * 10)  # 50 characters width, estimated at 10 pixels per character
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

        left_widget.setLayout(left_section)

        # Right section: Instruments
        right_widget = QtWidgets.QWidget()
        right_section = QtWidgets.QVBoxLayout(right_widget)
        
        instruments_group = QtWidgets.QGroupBox("Instruments")
        instruments_layout = QtWidgets.QVBoxLayout()

        self.instruments = {
            "Function Generator": {},
            "Oscilloscope": {},
            "Accelerometer": {}
        }

        for instrument in self.instruments.keys():
            group_box = QtWidgets.QGroupBox(instrument)
            group_layout = QtWidgets.QVBoxLayout()
            
            # Editable line edit for device address
            device_edit = QtWidgets.QLineEdit()
            self.instruments[instrument]['line_edit'] = device_edit
            group_layout.addWidget(QtWidgets.QLabel("Device Address:"))
            group_layout.addWidget(device_edit)
            
            # Button layout
            button_layout = QtWidgets.QHBoxLayout()

            # Select button
            select_button = QtWidgets.QPushButton("Select")
            select_button.setFixedSize(80, 30)  # Set fixed size
            self.instruments[instrument]['button'] = select_button
            select_button.clicked.connect(lambda checked, inst=instrument: self.select_device(inst))
            button_layout.addWidget(select_button)
            
            # Disconnect button
            disconnect_button = QtWidgets.QPushButton("Disconnect")
            disconnect_button.setFixedSize(100, 30)  # Set fixed size
            self.instruments[instrument]['disconnect'] = disconnect_button
            disconnect_button.clicked.connect(lambda checked, inst=instrument: self.disconnect_device(inst))
            disconnect_button.setEnabled(False)
            button_layout.addWidget(disconnect_button)

            # Add button layout to a container
            button_container = QtWidgets.QWidget()
            button_container.setLayout(button_layout)

            # Add button container to group layout with stretch factor
            group_layout.addStretch(1)  # Stretch before the buttons to push them to the bottom
            group_layout.addWidget(button_container)

            # Add the group box to the layout
            group_box.setLayout(group_layout)
            instruments_layout.addWidget(group_box)
        
        instruments_group.setLayout(instruments_layout)
        right_section.addWidget(instruments_group)
        right_section.addStretch(1)  # Add stretch to push content to the top

        right_widget.setLayout(right_section)

        # Add widgets to the splitter
        splitter.addWidget(left_widget)
        splitter.addWidget(right_widget)
        splitter.setSizes([1, 1])  # Make both sections equal size initially

        # Add splitter to the main layout
        main_layout.addWidget(splitter)

        # Connect button actions
        self.identify_button.clicked.connect(self.identify_resources)

        # Dictionary to store selected instruments
        self.selected_instruments = {
            "Function Generator": None,
            "Oscilloscope": None,
            "Accelerometer": None
        }

    def update_device_line_edits(self):
        try:
            resources = ResourceManager().list_resources()
            unique_resources = list(set(resources))  # Remove duplicates
            for instrument, controls in self.instruments.items():
                line_edit = controls['line_edit']
                current_text = line_edit.text()
                line_edit.clear()
                line_edit.setPlaceholderText("Enter device address...")
                if current_text in unique_resources:
                    line_edit.setText(current_text)
        except Exception as e:
            print(f"Error updating device line edits: {e}")

    def select_device(self, instrument):
        line_edit = self.instruments[instrument]['line_edit']
        selected_resource = line_edit.text()
        if selected_resource:
            self.selected_instruments[instrument] = selected_resource
            print(f"Selected {instrument}: {selected_resource}")  # Debugging line
            self.remove_resource_from_table(selected_resource)
            line_edit.setEnabled(False)
            self.instruments[instrument]['button'].setEnabled(False)
            self.instruments[instrument]['disconnect'].setEnabled(True)

    def disconnect_device(self, instrument):
        selected_resource = self.selected_instruments[instrument]
        if selected_resource:
            self.add_resource_to_table(selected_resource)
            self.selected_instruments[instrument] = None
            self.instruments[instrument]['line_edit'].setEnabled(True)
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
            # Update line edits after identifying resources
            self.update_device_line_edits()
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
