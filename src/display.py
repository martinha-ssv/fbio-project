import matplotlib.pyplot as plt
from data import vmin, vmax, n
import logging
from anyplot import AnyPlot, MultipleTimeseries, HeatmapDots, Heatmap

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

class Display():
    PLOT_CLASSES = [MultipleTimeseries, Heatmap, HeatmapDots]
    UPDATE_INTERVAL = 0.5

    def __init__(self, data):
        self.displaying = True
        self.data = data
        self.plotType = self.getPlotTypeFromUserInput()

    def display(self, plot_interval=0.01):
        #plt.ion()
        logger.info(f"Displaying data with plot type: {self.plotType}")
        self.plot = self.plotType(self)
        while self.displaying: # TODO change visualization
            self.plot.update_plot(self)
            self.plot.pause(plot_interval)


    def getPlotTypeFromUserInput(self):
        plot_fs_str = '\n'.join([f"[{i}]   {plot.description}" for i, plot in enumerate(Display.PLOT_CLASSES)])
        print(f"Available plot types are:\n{plot_fs_str}")
        
        plot_option = None
        while plot_option is None:
                    try:
                        plot_option = Display.PLOT_CLASSES[int(input("Enter the plot type number: "))]
                    except:
                        logger.error(f"Invalid plot type number. Available plots are:\n{plot_fs_str}")

        return plot_option
        


        