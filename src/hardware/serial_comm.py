import serial
import serial.tools.list_ports
import time
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from config import BAUD_RATE

class ArduinoSerial:
    def __init__(self, port: str = None):
        if port is None:
            ports = [p.device for p in serial.tools.list_ports.comports()]
            if not ports:
                raise RuntimeError("No serial port found")
            port = ports[0]
        self.ser = serial.Serial(port, BAUD_RATE, timeout=120)
        time.sleep(2.0)

    def send(self, lane: str, duration: int):
        self.ser.write(f"{lane},{duration}\n".encode())

    def wait_done(self):
        while True:
            if self.ser.readline().decode(errors="ignore").strip() == "DONE":
                return

    def close(self):
        self.ser.close()