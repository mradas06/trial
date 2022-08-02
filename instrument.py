import time
import pyvisa
from main import*


rm = pyvisa.ResourceManager() # List all connected resources
print("Resources detected\n{}\n".format(rm.list_resources()))
rID = rm.open_resource(rm.list_resources()[0])
print('Power supply detected=> ' + rID.query('*IDN?')) 
hmp4040 = HMP4040(resource=rID)

rID.write('*RST')
time.sleep(2)

rID.close()
