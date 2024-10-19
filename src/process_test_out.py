
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

n = 3 # number of electrodes
delay = 10 #ms
sampling_rate = 1000/delay #Hz

def read_board_output():
    data = pd.read_csv('output.csv')
    tss = [[data[data['x']==i][data['y']==j] for i in range(n)] for j in range(n)]
    maps = [data.iloc[i-8:i].reset_index(drop=True) for i in range(8, len(data),8)] # porque é que eu pus 8???
    return data, tss, maps

def create_timeseries_plots(unique_id, tss):
    fig, ax = plt.subplots(n,n)

    for i in range(n):
        for j in range(n):
            ax[i,j].plot(tss[i][j]['Time'], tss[i][j]['voltage'])
            ax[i,j].set_ylim([0,5])
            ax[i,j].set_title(f'{i}, {j}')

    plt.tight_layout()
    plt.savefig(f'time_series_test{unique_id}.png')

def animate_pressuremap(maps):
    def create_heatmap(df, ax):
        heatmap_data = np.zeros((n,n))  # Assuming the grid is always 3x3
        for _, row in df.iterrows():
            heatmap_data[int(row['x']), int(row['y'])] = row['voltage']
        ax.imshow(heatmap_data, cmap='viridis', vmin=0, vmax=5)
        ax.set_title("Heatmap")
        ax.set_xticks([])
        ax.set_yticks([])

    fig, ax = plt.subplots()

    def animate(i):
        ax.clear()
        create_heatmap(maps[i], ax)

    ani = animation.FuncAnimation(fig, animate, frames=len(maps), repeat=False, interval = 1000/sampling_rate*8)
    cbar = fig.colorbar(animate(0), ax=ax, orientation='vertical')
    cbar.set_label('Voltage')

    ani.save('heatmap_time.mp4')




