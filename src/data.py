import time
import pandas as pd
import numpy as np

n = 3 # number of electrodes
delay = 10 #ms
sampling_rate = 1000/delay #Hz

class Data():
    vmin = 0
    vmax = 5

    def __init__(self):
        self.full_data = pd.DataFrame(columns=['x', 'y', 'time', 'voltage'])
        self.data = {(x,y): {   'time': [], \
                                        'voltage': []   } \
                                                            for x in range(n) for y in range(n)}
        self.startTime = time.perf_counter()

    def add(self, line):
            line_dict = self.parseLine(line)
            self.addDataLine(line_dict)

    def getTimeSeries(self, x, y, window=None):
        window = len(self.data[(x,y)]['time']) if window is None else window
        return self.data[(x,y)]['time'][window:], self.data[(x,y)]['voltage'][window:]
    
    def parseLine(self, line):
        line = line.split(',')
        x = int(line[0])
        y = int(line[1])
        voltage = float(line[2])
        dt = time.perf_counter() - self.startTime
        line_dict = {'x': x, 'y': y, 'voltage': voltage, 'time': dt}

        return line_dict
    
    def addDataLine(self, line_dict):
        self.data[(line_dict['x'], line_dict['y'])]['time'].append(line_dict['time'])
        self.data[(line_dict['x'], line_dict['y'])]['voltage'].append(line_dict['voltage'])


    def createFullData(self):
        for key in self.data:
            x, y = key
            sub_df = pd.DataFrame([np.full(len(self.data[key]['time']), x), \
                                    np.full(len(self.data[key]['time']), y), \
                                    self.data[key]['time'], \
                                    self.data[key]['voltage']], columns=['x', 'y', 'time', 'voltage'])
            self.full_data = pd.concat([self.full_data, sub_df], ignore_index=True)
        return self.full_data
                
    def getDFs(self):
        grouped_df = self.full_data.groupby(['x', 'y'])
        for (x, y), group in grouped_df:
            print(group) #TODO