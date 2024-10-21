import threading
from comms import Comms
from data import Data
from display import Display
import logging
#from game.game import Game

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

plot_interval = 0.02
port = '/dev/cu.usbserial-AQ01PKSO'
data = Data()
comms = Comms(data)

runtime_options = ['See data', 'Play game']
runtime_options_str = '\n'.join([f"[{i}]   {opt}" for i, opt in enumerate(runtime_options)])
runtime_opt = None
while runtime_opt is None:
    try:
        runtime_opt = int(input(f"Choose an option:\n{runtime_options_str}\n"))
    except:
        logger.info("Invalid option. Options are:\n{runtime_options_str}")

reading = threading.Thread(name='SERIAL', target=comms.serialStream, daemon=True)
reading.start()

if runtime_opt == 0:
    display = Display(data)
    display.display(plot_interval)
elif runtime_opt == 1:
    #game = Game()#data)
    #game.run()
    pass



#processing = threading.Thread(name='FILTER', target=data.processData, args=(data,), daemon=True)



#processing.start()


#processing.join()

#df = data.saveData()

reading.join()
comms.close()