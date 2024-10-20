from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
from data import vmin, vmax, n
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

class AnyPlot(ABC):
    """
    AnyPlot is an abstract base class for creating and updating plots using Matplotlib.

    Methods:
        update_plot(data):
            Abstract method to update the plot with new data.
        config_ax():
            Abstract method to configure the axes of the plot.
    """

    description = 'AnyPlot is an abstract base class for creating and updating plots using Matplotlib.'

    def __init__(self, display):
        self.display = display
        plt.ion()


    def clean_plot(self):
        self.ax.cla()

    @abstractmethod
    def update_plot(self, data):
        pass

    @abstractmethod
    def config_axes(self):
        pass

    def pause(self, interval):
        plt.pause(interval)

class MultipleTimeseries(AnyPlot):

    description = 'Show a timeseries plot for each electrode.'

    def __init__(self, display):
        super().__init__(display)
        self.fig, self.ax = plt.subplots(n, n)
        self.config_axes()

    def update_plot(self, display):
        logger.debug("Updating timeseries plot")
        for (x,y) in self.display.data.data:
            ax = self.ax[x, y]
            ax.cla()
            self.config_ax(x,y)
            time, voltage = self.display.data.getTimeSeries(x, y, window=100)
            ax.plot(time, voltage)

    def config_ax(self, i, j):
        ax = self.ax[i, j]
        ax.set_title(f'electrode {i}, {j}')
        ax.set_ylim([vmin, vmax])

    def config_axes(self):
        for (x,y) in self.display.data.data:
            self.config_ax(x, y)

class Heatmap(AnyPlot):
    def update_plot(self, data):
        self.ax.bar(range(len(data)), data)

    def config_axes(self):
        self.ax.set_xlabel('Categories')
        self.ax.set_ylabel('Values')
