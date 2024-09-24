from PySide6.QtWidgets import QMainWindow, QApplication, QGraphicsScene, QGraphicsView, QVBoxLayout, QWidget
from PySide6.QtCore import Qt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Matplotlib in QGraphicsView")
        self.setGeometry(100, 100, 800, 600)

        # Main layout
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        self.setCentralWidget(central_widget)

        # Create a QGraphicsView
        self.graphics_view = QGraphicsView()
        layout.addWidget(self.graphics_view)

        # Create a QGraphicsScene and set it to the QGraphicsView
        self.scene = QGraphicsScene()
        self.graphics_view.setScene(self.scene)

        # Create the matplotlib figure and canvas
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        self.ax.plot([0, 1, 2, 3], [1, 3, 2, 4])  # Example plot

        # Remove padding around the plot
        self.fig.tight_layout(pad=0.0)

        # Create the FigureCanvas and add it to the QGraphicsScene
        self.canvas = FigureCanvas(self.fig)
        self.scene.addWidget(self.canvas)

        # Update the canvas size to fit the QGraphicsView
        self.update_canvas_size()

    def update_canvas_size(self):
        # Get the size of the QGraphicsView viewport
        view_size = self.graphics_view.viewport().size()
        print("View size: ", view_size.width(), view_size.height())

        # Calculate the DPI (Dots Per Inch) for the figure
        dpi = self.fig.get_dpi()

        # Set the figure size in inches based on the viewport size
        self.fig.set_size_inches(view_size.width() / dpi, view_size.height() / dpi)

        # Re-draw the canvas
        self.canvas.draw()

        # Fit the canvas in the view
        self.graphics_view.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
