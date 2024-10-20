import matplotlib.pyplot as plt

import numpy as np
import serial

def preprocessing(data_point: str) -> int:
    line = data_point.split(',')
    voltage = float(line[-1])
    # Preprocess the data point
    return voltage

def read_and_plot(preprocessing, port: str):
    # Set up the plot and axis
    arduino = serial.Serial(port, 19200) # fix port
    plt.ion()
    fig, ax = plt.subplots()
    plt.ylim ([0,5])
    plt.xlim([0,100])

    # Generate and plot the initial random data
    data = np.random.randint(0, 1023, size= (50,))
    line, = ax.plot(data)
    # Add legends to the plot
    ax.set_xlabel('Time (ms) ')
    ax.set_ylabel('Data')
    ax.set_title('Real-time Data Plot')
    ax.legend(['Data'], loc='upper right')
    # Continuously update the plot with new random data
    while True:
        # Generate new random data
        data_point = arduino.readline().decode('utf-8').strip()
        data_point = preprocessing(data_point)
        #if not 'DISCHARGING' in data_point:
        data = np.append(data, data_point)
        # Keep only the last 100 data points to maintain the window size
        if len (data) > 100:
            data = data[-100:]
        # Update the plot with the new data
        line.set_ydata(data)
        line.set_xdata(np.arange(len(data)))
        plt.draw()
        plt.pause(0.01)

read_and_plot(preprocessing, '/dev/cu.usbserial-AQ01PKSO') # fix port