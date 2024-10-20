import threading
from comms import Comms
from data import Data
from display import Display

port = '/dev/cu.usbserial-AQ01PKSO'
data = Data()
comms = Comms(data)
display = Display(data)

plot_interval = 0.05

reading = threading.Thread(name='SERIAL', target=comms.serialStream, daemon=False)
reading.start()
#processing = threading.Thread(name='FILTER', target=data.processData, args=(data,), daemon=True)
display.display(plot_interval)


#processing.start()

reading.join()
#processing.join()

df = data.createFullData()
df.to_csv('output.csv', index=False)

comms.close()