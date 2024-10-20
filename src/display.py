import matplotlib.pyplot as plt
from data import Data

class Display():
    UPDATE_INTERVAL = 50
    def __init__(self, data, n=3):
        self.fig, self.ax = plt.subplots(n, n)

        self.displaying = True
        self.data = data
        self.displayData = { (x,y): { 'time': [], 'voltage': [] } for x in range(n) for y in range(n) }

    def config_ax(ax):
        ax.set_xlim([0, 2])
        ax.set_ylim([Data.vmin, Data.vmax])

    def display(self):
        count = 0
        while self.displaying:
            count += 1
            if count == Display.UPDATE_INTERVAL:   
                count = 0 
                for (x,y) in self.displayData:
                        time, voltage = self.displayData.getTimeSeries(x, y, window=100)
                        self.ax[x, y].plot(time, voltage)
                        self.config_ax(self.ax[x, y])

        plt.show()