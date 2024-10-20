import threading
from comms import Comms
from data import Data
from display import Display

port = '/dev/cu.usbserial-AQ01PKSO'
data = Data()
comms = Comms(port, data)
display = Display(data)

reading = threading.Thread(name='SERIAL', target=comms.serialStream, daemon=False)
#processing = threading.Thread(name='FILTER', target=data.processData, args=(data,), daemon=True)
#displaying = threading.Thread(name='PLOT', target=display.display, args=(data,), daemon=True)

reading.start()
#processing.start()
#displaying.start()

reading.join()
#processing.join()
#displaying.join()

df = data.createFullData()
df.to_csv('output.csv', index=False)

comms.close()