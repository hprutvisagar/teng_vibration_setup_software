import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from ui_form import Ui_main_widget  # Import the generated class
import pyvisa

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_main_widget()  # Instantiate the UI class
        self.ui.setupUi(self)  # Set up the UI

        # Initialize PyVISA resource manager
        self.rm = pyvisa.ResourceManager()

        self.ui.output_message.setReadOnly(True)

        # Connect signals to your slots (functions) here
        self.ui.identify_res_button.clicked.connect(self.identify_and_print_devices)
        self.ui.fun_save_button.clicked.connect(self.save_function_generator_config)
        self.ui.fun_config_send_button.clicked.connect(self.send_waveform_to_fun)

    def print_message_to_output(self,message):
        self.ui.output_message.clear()
        self.ui.output_message.setPlainText(message)

    def identify_and_print_devices(self):
        # Get the list of connected devices
        resources = self.rm.list_resources()
        resources = [x for x in set(resources)]  # eliminates duplicates
        
        # Clear the table before populating it
        self.ui.connected_devices_table.clearContents()
        self.ui.connected_devices_table.setRowCount(len(resources))
        self.ui.connected_devices_table.setColumnCount(2)
        self.ui.connected_devices_table.setHorizontalHeaderLabels(["Resource ID", "Resource Identification"])
        self.ui.connected_devices_table.setColumnWidth(0,200)

        # Set the second column to take up the remaining space
        self.ui.connected_devices_table.horizontalHeader().setStretchLastSection(True)

        if len(resources) == 0:
            # If no resources are found, display a message in the first row
            print('no devices connected')
            self.ui.connected_devices_table.setRowCount(1)
            item = QTableWidgetItem("No resources available")
            self.ui.connected_devices_table.setItem(0, 0, item)
        else:
        # Populate the table with the list of resources        
            for row, resource in enumerate(resources):
                resource_item = QTableWidgetItem(resource)
                self.ui.connected_devices_table.setItem(row, 0, resource_item)

                try:
                    instrument = self.rm.open_resource(resource)
                    idn_string = instrument.query("*IDN?")
                except Exception as e:
                    idn_string = f"Error: {str(e)}"
                finally:
                    instrument.close()

                # Add the IDN string to the second column
                idn_item = QTableWidgetItem(idn_string)
                self.ui.connected_devices_table.setItem(row, 1, idn_item)     
        self.print_message_to_output("resources identification completed!")

    def save_function_generator_config(self):
        self.fun_id = self.ui.fun_id_input.text()
        self.fun_waveform = self.ui.fun_config_waveform_input.currentText()
        self.fun_freq = self.ui.fun_config_freq_input.text()
        self.fun_vpp = self.ui.fun_config_vpp_input.text()

        if not self.fun_id:
            self.print_message_to_output("Missing Function generator device ID.")
            return False
        elif not self.fun_waveform:
            self.print_message_to_output("Missing waveform type.")
            return False
        elif not self.fun_freq:
            self.print_message_to_output("Missing frequency value.")
            return False
        elif not self.fun_vpp:
            self.print_message_to_output("Missing Vpp value.")
            return False
        else:
            self.print_message_to_output("Function generator parameters saved!")
            return True
            
    def send_waveform_to_fun(self):
        if not self.save_function_generator_config():
            return

        self.waveform_dict = {
            'Sine' : 'SIN',
            'Square': 'SQU',
            'Triangular': 'TRI'
        }

        try:
            self.function_generator = self.rm.open_resource(self.fun_id)
            self.function_generator.write(f"APPL:{self.waveform_dict[self.fun_waveform]} {self.fun_freq}, {self.fun_vpp}, 0")
            self.function_generator.close()
            self.print_message_to_output(f"APPL:{self.waveform_dict[self.fun_waveform]} {self.fun_freq}, {self.fun_vpp}, 0")
        except Exception as e:
            self.print_message_to_output(f"Error: {str(e)}")
        finally:
            self.function_generator.close()

        
        
    #     self.save_function_generator_config() # trying to save the variables here

    #     if not (self.fun_id or self.fun_waveform or self.fun_freq or self.fun_vpp):
    #         print()


        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()  # Create an instance of your MainWindow class
    main_window.show()  # Show the main window
    sys.exit(app.exec())  # Start the application loop
