from PySide6 import QtWidgets
from ui.connections_tab import ConnectionsTab
from ui.configurations_tab import ConfigurationsTab
from ui.data_tab import DataTab

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Main layout for the entire window
        main_layout = QtWidgets.QVBoxLayout(self)

        # Create a QTabWidget
        tab_widget = QtWidgets.QTabWidget()

        # Add the tabs
        self.connections_tab = ConnectionsTab()
        self.configurations_tab = ConfigurationsTab()
        self.data_tab = DataTab()

        tab_widget.addTab(self.connections_tab, "Connections")
        tab_widget.addTab(self.configurations_tab, "Configurations")
        tab_widget.addTab(self.data_tab, "Data")

        # Adding the QTabWidget to the main layout
        main_layout.addWidget(tab_widget)
