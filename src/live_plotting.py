import matplotlib.pyplot as plt

import numpy as np
import serial

def read_and_plot(preprocessing: function, port: str):
    # Set up the plot and axis
    serial = serial.Serial(port, 9600) # fix port
    plt.ion()
    fig = plt.figure ()
    ax = fig.add_subplots(111)
    plt.ylim ([0,1023])
    plt.xlim( [0,100])

    # Generate and plot the initial random data
    data = np.random.randint(0, 1023, size= (50,))
    line, = ax.plot (data)
    # Add legends to the plot
    ax.set_xlabel('Time (ms) ')
    ax.set_Ylabel('Data')
    ax.set_title('Real-time Data Plot')
    ax.legend(['Data'], loc='upper right')
    # Continuously update the plot with new random data
    while True:
        # Generate new random data
        data_point = serial.readline().decode('utf-8').strip()
        data_point = preprocessing(data_point)
        if not 'DISCHARGING' in data_point:
            data = np.append (data, data_point)
        # Keep only the last 100 data points to maintain the window size
        if len (data) > 100:
            data = data[-100:]
        # Update the plot with the new data
        line.set_ydata(data)
        line.set_data(np.arange(len(data)))
        plt.draw()
        plt.pause(0.01)