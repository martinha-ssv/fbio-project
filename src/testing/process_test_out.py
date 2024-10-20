
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

n = 3 # number of electrodes
delay = 10 #ms
sampling_rate = 1000/delay #Hz

vmin = 0
vmax = 5

def parse_line(line):
    line = line.split(',')
    return {'x': int(line[0]), 'y': int(line[1]), 'voltage': float(line[2])}

def read_board_output(file='output.csv'):
    data = pd.read_csv(file)
    tss = [[data[data['x']==i][data['y']==j] for i in range(n)] for j in range(n)]
    maps = [create_heatmap_data(tss, i) for i in range(len(data)//n**2)]
    return data, tss, maps

def create_timeseries_plots(unique_id, tss, fig=None, ax=None, live=False):
    if fig is None or ax is None:    
        fig, ax = plt.subplots(n,n)

    for i in range(n):
        for j in range(n):
            ax[i,j].plot(tss[i][j]['Time'], tss[i][j]['voltage'])
            ax[i,j].set_ylim([0,5])
            ax[i,j].set_title(f'{i}, {j}')

    plt.tight_layout()

    if not live:
        plt.savefig(f'time_series_test{unique_id}.png')
    else:
        plt.show()

def create_heatmap_data(tss, ind):
    heatmap_data = np.zeros((n,n))  # Assuming the grid is always 3x3
    for i in range(n):
        for j in range(n):
            heatmap_data[i,j] = tss[i][j]['voltage'].iloc[ind]
    return heatmap_data

def create_heatmap_plot(heatmap_data, ax):
    ax.imshow(heatmap_data, cmap='gist_rainbow', vmin=vmin, vmax=vmax)
    ax.set_title("Heatmap")
    ax.set_xticks([])
    ax.set_yticks([])
    cbar = plt.colorbar(ax.images[0], ax=ax, orientation='vertical')
    cbar.set_label('Voltage')
    cbar.set_clim(vmin, vmax)

def animate_pressuremap(maps):
    
    fig, ax = plt.subplots()

    def animate(i):
        ax.clear()
        create_heatmap_plot(maps[i], ax)

    ani = animation.FuncAnimation(fig, animate, frames=len(maps), repeat=False, interval = delay*n**2)

    ani.save('heatmap_time.mp4')




read_board_output(file='out/tests/test20_out/output.csv')