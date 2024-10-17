import read_input4
import process_test_out as pto
import os

test_no = int(input('Which test are we on?'))
seconds = int(input('How many seconds do you want to record?'))

os.chdir('out/tests')
test_folder = f'test{test_no}_out'
os.mkdir(test_folder)
os.chdir(test_folder)

read_input4.read_board_data(seconds)

data, tss, maps = pto.read_board_output()
pto.create_timeseries_plots(test_no, tss)
pto.animate_pressuremap(maps)
