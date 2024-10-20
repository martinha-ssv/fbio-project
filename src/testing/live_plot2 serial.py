import serial
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import Rbf

# Configuração da conexão serial (ajuste para a sua porta e taxa de baud)
ser = serial.Serial('/dev/cu.usbserial-AQ01PKSO', 19200)

def get_sensor_positions():
    """ Define as posições dos sensores de acordo com o layout da imagem. """
    return {
        8: (1, 1), 9: (2, 1), 10: (1, 2), 11: (2,2),  # Calcanhar
        1: (0.5, 4), 2: (1,4), 3: (1.5,4), 4: (2,4.5), 12: (2, 3.5), # Metatarso
        5: (1, 3), 6: (1.5, 3), 7: (2, 3),  # Arco
        13: (0.5, 5), 14: (0.75, 5), 15: (1.25, 5), 16: (1.75, 5)  # Dedos
    }

def read_sensor_data():
    """
    Lê uma linha de dados da porta serial, divide-a e converte os valores para float.
    Presume que os dados são enviados como uma string com valores separados por vírgula.
    """
    line = ser.readline().decode('utf-8').strip()
    data = list(map(float, line.split(',')))  # Converte os dados para uma lista de floats
    return data

def plot_live_data(sensor_positions):
    """ Plota os dados ao vivo dos sensores em tempo real. """
    plt.ion()  # Ativar modo interativo
    grid_x, grid_y = np.mgrid[0:2.5:100j, 1:5:200j]  # Grade de interpolação

    while True:
        

        # Lê os dados do sensor
        pressures = read_sensor_data()

        # Posições dos sensores
        x_coords = [sensor_positions[i+1][0] for i in range(len(sensor_positions))]
        y_coords = [sensor_positions[i+1][1] for i in range(len(sensor_positions))]

        # Interpolação RBF para criar um gradiente suave
        rbf_interpolator = Rbf(x_coords, y_coords, pressures, function='multiquadric', smooth=0.3)
        grid_z = rbf_interpolator(grid_x, grid_y)

        # Plotar o mapa de calor interpolado
        plt.imshow(grid_z.T, extent=(0, 2.5, 1, 5), origin='lower', cmap='jet', vmin=0, vmax=np.max(pressures))
        plt.colorbar(label='Pressão (N)')
        plt.scatter(x_coords, y_coords, c=pressures, s=100, cmap='jet', edgecolors='black')
        plt.title('Pressão Plantar - Dados ao Vivo')
        plt.xlabel('Largura do Pé (Medial para Lateral)')
        plt.ylabel('Comprimento do Pé (Calcanhar para Dedos)')
        
        # Ajustar os limites do gráfico
        plt.xlim(0, 2.5)
        plt.ylim(1, 5)

        plt.pause(0.1)  # Atualização rápida do gráfico para visualização ao vivo

    plt.ioff()  # Desativa o modo interativo
    plt.show()

# Inicializar o layout dos sensores e começar o gráfico ao vivo
sensor_positions = get_sensor_positions()
plot_live_data(sensor_positions)
