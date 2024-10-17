import serial
import time
import live_plotting as lp

port = '/dev/cu.usbserial-AQ01PKSO'

def calc_capacitance(timeElapsed, resistorValue) -> float:
    # Calculate the capacitance from the data point
    capacitance = timeElapsed / resistorValue
    return capacitance

while True:
    # Read the data from the serial port
    line = .readline().decode('utf-8').strip()
    # Split the data into time and voltage
    timeElapsed, voltage = line.split(',')
    # Calculate the capacitance from the time and voltage
    capacitance = calc_capacitance(float(timeElapsed), 1000)
    # Print the capacitance
    print(f"Capacitance: {capacitance} F")
    time.sleep(0.15)