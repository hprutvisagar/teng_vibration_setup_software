import sys
import numpy as np
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QVBoxLayout, QWidget
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        # Create the central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Create a QGraphicsView and set it to the layout
        self.graphics_view = QGraphicsView()
        layout.addWidget(self.graphics_view)
        
        # Create a QGraphicsScene
        self.scene = QGraphicsScene()
        self.graphics_view.setScene(self.scene)
        
        # Create a Matplotlib Figure and FigureCanvas
        self.figure = Figure()
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self.figure)
        
        # Add FigureCanvas to the QGraphicsScene
        self.scene.addWidget(self.canvas)
        print(type(self.canvas))
        
        # Plot the data
        self.plot_data()

    def plot_data(self):
        # Generate data
        time_data = np.linspace(0, 1, 100)
        waveform_data = np.sin(2 * np.pi * 5 * time_data)
        
        # Plot the data
        self.ax.plot(time_data, waveform_data)
        self.ax.set_xlabel('Time (s)')
        self.ax.set_ylabel('Amplitude')
        self.ax.set_title('Sine Wave')
        self.ax.grid(True)
        
        # Draw the plot
        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
