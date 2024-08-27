import sys
import serial
import pyvisa
import datetime
import pandas as pd
import numpy as np
import matplotlib
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QVBoxLayout, QWidget, QGraphicsScene, QGraphicsProxyWidget
from PySide6.QtCore import Qt, QTimer, Signal, Slot
from ui_form import Ui_main_widget  
from RsInstrument import RsInstrument
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

class MainWindow(QMainWindow, Ui_main_widget):
    def __init__(self):
        super(MainWindow, self).__init__()

        central_widget = QWidget()

        self.ui = Ui_main_widget()
        self.ui.setupUi(central_widget)
        self.setCentralWidget(central_widget)

        self.rm = pyvisa.ResourceManager()

        self.ui.output_message.setReadOnly(True) # setting the terminal to read only
        self.message_id = 1

        # Connect signals to your slots (functions) here
        self.ui.identify_res_button.clicked.connect(self.identify_and_print_devices) # resource identification button
        self.ui.fun_save_button.clicked.connect(self.save_function_generator_config) # function generator configuration save button
        self.ui.fun_config_send_button.clicked.connect(self.send_waveform_to_fun) # send waveform to function generator
        self.ui.scope_config_save_button.clicked.connect(self.save_scope_config) # oscilloscope config save button
        self.ui.accel_status_check_button.clicked.connect(self.accel_config_check_status) # accelerometer comport status check button
        self.ui.accel_config_save_button.clicked.connect(self.accel_save) # accelerometer configuration save button
        self.ui.scope_fetch_button.clicked.connect(self.fetch_and_update_data) # oscilloscope data fetch button
        self.ui.scope_data_save_button.clicked.connect(self.scope_save_data)  # oscilloscope data save button


    def set_main_widget(self, widget):
        self.setCentralWidget(widget)

    def print_message_to_output(self, message):
        self.ui.output_message.clear()
        self.ui.output_message.append(f"{self.message_id}:{message}")
        self.message_id = self.message_id+1
        
    def identify_and_print_devices(self):
        resources = self.rm.list_resources()
        resources = list(set(resources))  # Eliminate duplicates
        
        # Clear the table before populating it
        self.ui.connected_devices_table.clearContents()
        self.ui.connected_devices_table.setRowCount(len(resources))
        self.ui.connected_devices_table.setColumnCount(2)
        self.ui.connected_devices_table.setHorizontalHeaderLabels(["Resource ID", "Resource Identification"])
        self.ui.connected_devices_table.setColumnWidth(0, 200)

        # Set the second column to take up the remaining space
        self.ui.connected_devices_table.horizontalHeader().setStretchLastSection(True)

        identified_resources = []

        for resource in resources:
            close_resource = True
            try:
                self.instrument = self.rm.open_resource(resource)
                idn_string = self.instrument.query("*IDN?")
                if idn_string.strip():  # Ensure IDN string is not empty
                    identified_resources.append((resource, idn_string))
                    close_resource = False
            
            except Exception as e:
                print(f"Error with resource {resource}: {str(e)}")
            
            finally:
                if close_resource:
                    try:
                        self.instrument.close()
                    except Exception as e:
                        self.print_message_to_output(f"Failed to close resource {resource}: {str(e)}")

        if not identified_resources:
            self.print_message_to_output("No identifiable devices connected")
            self.ui.connected_devices_table.setRowCount(1)
            item = QTableWidgetItem("No identifiable resources available")
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)
            self.ui.connected_devices_table.setItem(0, 0, item)
        else:
            self.ui.connected_devices_table.setRowCount(len(identified_resources))
            for row, (resource, idn_string) in enumerate(identified_resources):
                resource_item = QTableWidgetItem(resource)
                resource_item.setFlags(resource_item.flags() & ~Qt.ItemIsEditable)  # Make the item non-editable
                self.ui.connected_devices_table.setItem(row, 0, resource_item)

                idn_item = QTableWidgetItem(idn_string)
                idn_item.setFlags(idn_item.flags() & ~Qt.ItemIsEditable)  # Make the item non-editable
                self.ui.connected_devices_table.setItem(row, 1, idn_item)

        self.print_message_to_output("Resources identification completed!")

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
            'Sine': 'SIN',
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

    def save_scope_config(self):
        self.scope_id = self.ui.scope_config_id_input.text()
        self.scope_xrange = self.ui.scope_config_xrange_input.text()
        self.scope_yrange = self.ui.scope_config_yrange_input.text()
        self.scope_trigger_pos = self.ui.scope_config_trigger_input.text()

        if not self.scope_id:
            self.print_message_to_output("Missing Scope ID!")
            return False
        elif not self.scope_xrange:
            self.print_message_to_output("Missing X range!")
            return False
        elif not self.scope_yrange:
            self.print_message_to_output("Missing Y range!")
            return False
        elif not self.scope_trigger_pos:
            self.print_message_to_output("Missing Trigger value!")
            return False
        else:
            self.print_message_to_output("Scope parameters saved!")
            return True

    def accel_config_check_status(self):
        self.accel_com_text = self.ui.accel_config_com_input.text()
        self.accel_com_baud_rate = self.ui.com_baud_rate_input.currentText()

        if not self.accel_com_text:
            self.ui.accel_com_status_label.setText("Error!!!")
            self.print_message_to_output("Entered valid COM port number!")
        elif not self.accel_com_baud_rate:
            self.ui.accel_com_status_label.setText("Error!!!")
            self.print_message_to_output("Entered valid BAUD Rate for communication!")
        else:
            self.print_message_to_output("COM port parameters saved!")

        try:
            accel_com = int(self.accel_com_text)
        except ValueError:
            self.ui.accel_com_status_label.setText("Error!!!")
            self.print_message_to_output("Entered valid COM port number!")
            return
        
        # Check the COM port status
        self.accel_com_status = self.get_com_status(f"COM{accel_com}")

        if self.accel_com_status == "Active and readable":
            self.ui.accel_com_status_label.setText(f"COM{accel_com} Available!")
        else:
            self.ui.accel_com_status_label.setText("Error!!!")
            self.print_message_to_output(f"Port{self.accel_com_text} is open but no data available")

    def get_com_status(self, com_port):
        try:
            with serial.Serial(com_port, timeout=1) as ser:
                if ser.in_waiting > 0:
                    return "Active and readable"
                else:
                    return "Port is open but no data available"
        except serial.SerialException:
            self.print_message_to_output("COM Port is not accessible") 
            return "Error!!! COM Port is not accessible"

    def accel_save(self):
        self.accel_config_check_status()

    def fetch_and_update_data(self):
        if not self.save_scope_config():
            return
        else:
            self.save_scope_config()
        
            # Step 1: Set up the QGraphicsScene and QGraphicsView
            self.scope_scene = QGraphicsScene()
            self.ui.scope_graphics_view.setScene(self.scope_scene)

            # Step 2: Get the current size of the QGraphicsView
            size = self.ui.scope_graphics_view.size()
            dpi = 300

            self.scope_figure = Figure(figsize=(size.width()/dpi, size.height()/dpi), dpi=dpi)
            self.scope_figure.subplots_adjust(left=0, right=1, top=1, bottom=0)
            self.ax = self.scope_figure.add_subplot(111)

            # Create the canvas and add it to the scene
            self.scope_canvas = FigureCanvas(self.scope_figure)
            self.scope_canvas.setFixedSize(size.width(), size.height())
            self.scope_scene.addWidget(self.scope_canvas)
            # self.scope_canvas.setGeometry(0, 0, size.width(), size.height())

            # step 4: Check selected channels and fetch waveform data
            channels = [
                    self.ui.scope_channel1.isChecked(),
                    self.ui.scope_channel2.isChecked(),
                    self.ui.scope_channel3.isChecked(),
                    self.ui.scope_channel4.isChecked()
                ]
            
            if sum(channels) > 0:
                # Step 5: Connect to oscilloscope
                rtb = RsInstrument(self.scope_id, True, True)
                rtb.write_str(f"TIM:ACQT {self.scope_xrange}")

                # step 6: fetch selected data
                scope_data = {}
                colors = ['blue', 'green', 'red', 'purple']
                for i, ch in enumerate(channels, start=1):
                    if ch:
                        rtb.write_str(f"CHAN{i}:DATA:SOURCE CHAN{i}")
                        waveform = rtb.query_bin_or_ascii_float_list(f'FORM ASC;:CHAN{i}:DATA?')
                        x_increment = float(rtb.query(f'CHAN{i}:DATA:XINC?'))
                        x_origin = float(rtb.query(f'CHAN{i}:DATA:XOR?'))
                        time_data = np.arange(0, len(waveform)) * x_increment + x_origin
                        scope_data[f'Channel_{i}'] = pd.DataFrame({
                            'time_data': time_data,
                            'waveform': waveform,
                            'color': colors[i-1]
                            })
                rtb.close()

                # Step 5: Plot the data from the selected channels
                for channel_name, data in scope_data.items():
                    self.ax.plot(data['time_data'], data['waveform'], label=channel_name, color=data['color'])

                self.ax.legend()

                # Step 7: Draw the plot
                self.scope_canvas.draw()

                # Step 8: Handle resizing within the same method
                size = self.ui.scope_graphics_view.size()
                width = size.width()
                height = size.height()

                # Update figure and canvas sizes based on the new size
                self.scope_figure.set_size_inches(width / dpi, height / dpi)
                self.scope_canvas.setFixedSize(width, height)
                self.scope_canvas.draw()  # Redraw to apply the new sizes
                self.print_message_to_output("Scope data plotted!")
            else:
                self.print_message_to_output("Error! No channels selected.")

    def scope_save_data(self):
        if self.scope_data:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"data_{timestamp}.xlsx"
            with pd.ExcelWriter(filename, engine='xlsxwriter') as writer:
                for channel, df in self.scope_data.items():
                    sheet_name = f"Channel_{channel[-1]}"
                    df.to_excel(writer, sheet_name=sheet_name, index=False)
            
            self.print_message_to_output("Data fetched and saved successfully.")
        else:
             self.print_message_to_output("No data available.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()  # Create an instance of your MainWindow class
    main_window.setGeometry(0, 0, 1800, 1800)
    main_window.show()  # Show the main window
    sys.exit(app.exec())  # Start the application loop
