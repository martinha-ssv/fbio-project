import serial
import time

port = '/dev/cu.usbserial-AQ01PKSO'
ser = serial.Serial(port, 19200)  # Update COM_PORT to your Arduino's port

def read_board_data(seconds):
    with open("output.csv", "w") as file:
        file.write("Time,x,y,voltage\n")
        start_time = time.time()
        dt = 0
        while dt<seconds:
            dt = time.time() - start_time
            line = ser.readline()
            line = line.decode('ascii')
            line = line.strip()  # Read from serial
            str_to_write = str(dt)+','+line
            print(str_to_write)
            file.write(str_to_write+"\n")
            time.sleep(0.15)

read_board_data(20)