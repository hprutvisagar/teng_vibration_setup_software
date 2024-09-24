import sys
import serial
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer, QThread, pyqtSignal
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from scipy.fft import fft, fftfreq
from collections import deque

class SerialWorker(QThread):
    data_received = pyqtSignal(float)


    def __init__(self, port, baudrate, timeout=1):
        super().__init__()
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.running = False

    def run(self):
        try:
            self.ser = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
            self.running = True
            while self.running:
                if self.ser.in_waiting > 0:
                    line_data = self.ser.readline().decode('utf-8').strip()
                    try:
                        value = float(line_data)
                        self.data_received.emit(value)
                    except ValueError:
                        continue
        except serial.SerialException as e:
            print(f"Error opening the serial port: {e}")

    def stop(self):
        self.running = False
        if hasattr(self, 'ser') and self.ser.is_open:
            self.ser.close()

class ResizableFigureCanvas(FigureCanvas):

    dpi = 600

    def __init__(self, figure, parent=None):
        super().__init__(figure)
        self.setParent(parent)
        self.figure.tight_layout()  # Adjust layout initially

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.figure.set_size_inches(self.width() / self.dpi, self.height() / self.dpi, forward=True)
        self.draw()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Serial Data Plotter with FFT")
        self.setGeometry(0, 0, 800, 600)

        self.data_queue = deque(maxlen=100)
        self.time_data = []
        self.fft_data = []

        self.setup_ui()

        self.update_interval = 100  # Update every 100 ms
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plots)

        self.worker = None

    def setup_ui(self):
        central_widget = QWidget()
        layout = QVBoxLayout()

        self.time_series_scene = QGraphicsScene()
        self.time_series_fig = Figure()
        self.ax1 = self.time_series_fig.add_subplot(111)
        self.time_series_canvas = ResizableFigureCanvas(self.time_series_fig)
        self.time_series_scene.addWidget(self.time_series_canvas)

        self.fft_scene = QGraphicsScene()
        self.fft_fig = Figure()
        self.ax2 = self.fft_fig.add_subplot(111)
        self.fft_canvas = ResizableFigureCanvas(self.fft_fig)
        self.fft_scene.addWidget(self.fft_canvas)

        layout.addWidget(self.time_series_canvas)
        layout.addWidget(self.fft_canvas)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def start_acquisition(self, port='COM3', baudrate=115200):
        if self.worker is None:
            self.worker = SerialWorker(port, baudrate)
            self.worker.data_received.connect(self.add_data)
            self.worker.start()
            self.timer.start(self.update_interval)
            print(f"Started acquisition on {port} at {baudrate} baud.")

    def add_data(self, value):
        self.data_queue.append(value)
        self.time_data.append(value)

    def update_plots(self):
        self.ax1.clear()
        self.ax1.plot(range(len(self.data_queue)), list(self.data_queue))
        self.ax1.set_ylim(-50, 50)
        self.ax1.set_xlim(0, len(self.data_queue))
        self.time_series_canvas.draw()

        self.compute_and_plot_fft()

    def compute_and_plot_fft(self):
        n = len(self.data_queue)
        if n < 2:
            return

        T = 1.0
        yf = fft(list(self.data_queue))
        xf = fftfreq(n, T)[:n // 2]
        magnitudes = 2.0 / n * np.abs(yf[:n // 2])

        self.ax2.clear()
        self.ax2.plot(xf, magnitudes, lw=2)
        self.ax2.set_xlim(0, xf[-1])
        self.ax2.set_ylim(0, np.max(magnitudes) * 1.1)
        self.ax2.set_title(f'FFT - Dominant Frequency: {xf[np.argmax(magnitudes)]:.2f} Hz')
        self.fft_canvas.draw()

    def stop_acquisition(self):
        if self.worker is not None:
            self.worker.stop()
            self.worker.wait()
            self.worker = None
            self.timer.stop()
            print("Stopped data acquisition.")

    def closeEvent(self, event):
        self.stop_acquisition()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    window.start_acquisition(port='COM3', baudrate=115200)

    sys.exit(app.exec_())
