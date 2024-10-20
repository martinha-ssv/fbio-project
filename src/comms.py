import serial
import logging
import serial.tools.list_ports

port = '/dev/cu.usbserial-AQ01PKSO'
baud_rate = 19200
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

class Comms():
    def __init__(self, data):

        port = self.getPortFromInput()
        self.ser = serial.Serial(port, baud_rate, timeout=0.1)
        self.data = data
        self.ser.flushInput()
        self.ser.flushOutput()

    def send(self, data):
        self.ser.write(data)

    def receive(self):
        if self.ser.in_waiting > 0:
            msg = self.ser.readline().decode('ascii').strip()
            logger.debug(f"Received serial data: {msg}")
            return msg
        return None

    def close(self):
        self.ser.close() 

    def serialStream(self):
        while True:
            data_line = self.receive()
            if not data_line is None: self.data.add(data_line)

    def getPortFromInput(self):
        available_ports = serial.tools.list_ports.comports()
        ports_str = '\n'.join([f"{i}: {port}" for i, port in enumerate(available_ports)])
        print(f"Available ports are:\n{ports_str}")
        port = None
        while port is None:
            try:
                port = available_ports[int(input("Enter the port number: "))].device
            except:
                logger.error(f"Invalid port number. Available ports are:\n{ports_str}")
        return port