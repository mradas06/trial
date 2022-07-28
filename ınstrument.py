import time
import pyvisa
from main import*


rm = pyvisa.ResourceManager() # List all connected resources
print("Resources detected\n{}\n".format(rm.list_resources()))
rID = rm.open_resource('ASRL6::INSTR')
hmp4040 = hmp4040(resource=rID)

rID.write('*RST')
time.sleep(2)
