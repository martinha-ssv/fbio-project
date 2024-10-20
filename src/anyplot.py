from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
from data import vmin, vmax, n
import logging
import numpy as np

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
        self.ax.cla()
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
            self.config_ax(x,y)
            time, voltage = self.display.data.getTimeSeries(x, y, window=100)
            ax.plot(time, voltage)

    def config_ax(self, i, j):
        ax = self.ax[i, j]
        ax.cla() # FIXME I changed this and unsure it is correct.
        ax.set_title(f'electrode {i}, {j}')
        ax.set_ylim([vmin, vmax])

    def config_axes(self):
        for (x,y) in self.display.data.data:
            self.config_ax(x, y)

class HeatmapDots(AnyPlot):
    description = 'Show a heatmap as dots of the pressure on each electrode.'
    def __init__(self, display):
        super().__init__(display)
        self.fig, self.ax = plt.subplots()
        sc = plt.scatter([], [], c=[], s=100, cmap='gist_rainbow', edgecolors='black', vmin=vmin, vmax=vmax)
        plt.colorbar(sc)

    def update_plot(self, data):
        self.config_axes()
        x_coords, y_coords, voltages = self.get_data()
        plt.scatter(x_coords, y_coords, c=voltages, s=500, cmap='gist_rainbow', edgecolors='black', vmin=vmin, vmax=vmax)
        plt.title('Pressure Distribution - Live Data')
        plt.xlabel('Width')
        plt.ylabel('Length')

    def get_data(self):
        x_coords = []
        y_coords = []
        voltages = []
        for (x,y) in self.display.data.data:
            x_coords.append(x)
            y_coords.append(y)
            _, voltages_in = self.display.data.getTimeSeries(x, y, window=10)
            voltage = np.mean(voltages_in)
            voltages.append(voltage)
        return x_coords, y_coords, voltages
    
    def config_axes(self):
        self.ax.cla()
        
class Heatmap(AnyPlot):
    description = 'Show a heatmap of the pressure on each electrode.'
    def __init__(self, display):
        super().__init__(display)
        self.fig, self.ax = plt.subplots()
        sc = plt.imshow(np.zeros((n,n)), cmap='gist_rainbow', vmin=vmin, vmax=vmax)
        plt.colorbar(sc)
    
    def update_plot(self, data):
        self.config_axes()
        heatmap_data = self.get_data()
        plt.imshow(heatmap_data, cmap='gist_rainbow', vmin=vmin, vmax=vmax)
        plt.title('Pressure Distribution - Live Data')

    def config_axes(self):
        return super().config_axes()

    def get_data(self):
        heatmap_data = np.zeros((n,n))
        for (x,y) in self.display.data.data:
            _, voltages_in = self.display.data.getTimeSeries(x, y, window=10)
            voltage = np.mean(voltages_in)
            heatmap_data[x, y] = voltage
        return heatmap_data