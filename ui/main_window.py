from PySide6 import QtWidgets, QtCore
from ui.test_measurement_setup_tab import TestMeasurementSetupTab

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Main layout for the entire window
        main_layout = QtWidgets.QVBoxLayout(self)

        # Title Label
        title_label = QtWidgets.QLabel("Frequency Tunable Triboelectric Energy Harvester Project - Test and Measurement Setup")
        title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("font-size: 16px; font-weight: bold;")

        # Create the main content widget
        self.test_measurement_setup_tab = TestMeasurementSetupTab()

        # Adding widgets to the main layout
        main_layout.addWidget(title_label)
        main_layout.addWidget(self.test_measurement_setup_tab)

        # Set the main layout to the window
        self.setLayout(main_layout)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.resize(1200, 800)
    main_window.show()
    sys.exit(app.exec())
