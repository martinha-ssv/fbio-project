import matplotlib.pyplot as plt
from data import vmin, vmax

class Display():
    UPDATE_INTERVAL = 0.5
    def __init__(self, data, n=3):
        self.fig, self.ax = plt.subplots(n, n)
        

        self.displaying = True
        self.data = data
        self.displayData = { (x,y): { 'time': [], 'voltage': [] } for x in range(n) for y in range(n) }
        self.config_axes()

    def config_ax(self, i, j):
        ax = self.ax[i, j]
        ax.set_title(f'electrode {i}, {j}')
        ax.set_ylim([vmin, vmax])

    def config_axes(self):
        for (x,y) in self.displayData:
            self.config_ax(x, y)

    def display(self, plot_interval=0.01):
        plt.ion()
        while self.displaying:
            for (x,y) in self.data.data:
                    ax = self.ax[x, y]
                    time, voltage = self.data.getTimeSeries(x, y, window=100) # TODO: it won't actually be 100
                    ax.cla()
                    self.config_ax(x,y)
                    ax.plot(time, voltage)
            plt.pause(plot_interval)