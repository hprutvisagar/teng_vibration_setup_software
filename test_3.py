import sys
import serial  # For serial communication
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QVBoxLayout, QWidget
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation

# Initialize the serial port
ser = serial.Serial('COM3', 115200)  # Replace 'COM3' with your serial port

def main():
    # Create a PySide6 application
    app = QApplication(sys.argv)
    window = QMainWindow()

    # Create central widget
    central_widget = QWidget(window)
    window.setCentralWidget(central_widget)

    # Create a vertical layout for the window
    layout = QVBoxLayout(central_widget)

    # Create a QGraphicsView to host the plot
    graphics_view = QGraphicsView()
    layout.addWidget(graphics_view)

    # Create a QGraphicsScene and add it to the QGraphicsView
    scene = QGraphicsScene()
    graphics_view.setScene(scene)

    # Create a matplotlib figure and canvas
    fig = Figure()
    ax = fig.add_subplot(111)
    line, = ax.plot([], [], lw=2)
    ax.grid(True)
    ax.set_ylim(-50, 50)  # Set y-axis limits

    # Create a FigureCanvas to hold the matplotlib figure
    canvas = FigureCanvas(fig)
    scene.addWidget(canvas)

    
    time_data = []
    g_value_data = []

    # Define the update function for animation
    def update(frame):
        if ser.in_waiting > 0:  # Check if data is available to read
            line_data = ser.readline().decode('utf-8').strip()
            print(line_data)

            try:
                # Assuming data format: "time, g_value"
                time_str, g_value_str = line_data.split(", ")
                time = float(time_str[1:])
                g_value = float(g_value_str[:-1])

                # Append new values to data lists
                time_data.append(time)
                g_value_data.append(g_value)

                # Keep the data within a fixed size (last 100 points)
                if len(time_data) > 100:
                    time_data.pop(0)
                    g_value_data.pop(0)

                # Update the plot data
                line.set_data(time_data, g_value_data)
                ax.relim()
                ax.autoscale_view(True, True, True)
            except ValueError:
                pass

        return line,

    # Set up the animation
    ani = FuncAnimation(fig, update, blit=False, interval=50, cache_frame_data=False)
    
    # Show the window
    window.show()
    sys.exit(app.exec_())

    

if __name__ == "__main__":
    main()
    
