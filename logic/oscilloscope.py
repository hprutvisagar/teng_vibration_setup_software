class Oscilloscope:
    def __init__(self, com_port):
        self.com_port = com_port

    def connect(self):
        print(f"Connecting to oscilloscope on {self.com_port}")
        # Connection logic here

    def disconnect(self):
        print(f"Disconnecting oscilloscope on {self.com_port}")
        # Disconnection logic here
