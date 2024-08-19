from PySide6 import QtWidgets

class DataTab(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Layout for the DataTab
        layout = QtWidgets.QVBoxLayout(self)

        # Placeholder for data display
        self.data_display = QtWidgets.QTextEdit()
        self.data_display.setReadOnly(True)
        
        layout.addWidget(self.data_display)
