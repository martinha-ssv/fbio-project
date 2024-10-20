import serial
import logging

port = '/dev/cu.usbserial-AQ01PKSO'
baud_rate = 19200
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

class Comms():
    def __init__(self, port, data):
        self.port = port
        self.ser = serial.Serial(port, baud_rate, timeout=0.1)
        self.data = data
        self.ser.flushInput()
        self.ser.flushOutput()

    def send(self, data):
        self.ser.write(data)

    def receive(self):
        if self.ser.in_waiting > 0:
            msg = self.ser.readline().decode('ascii').strip()
            logger.info(f"Received serial data: {msg}")
            return msg
        return None

    def close(self):
        self.ser.close() 

    def serialStream(self):
        while True:
            data_line = self.receive()
            if not data_line is None: self.data.add(data_line)