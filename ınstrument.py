import time
import pyvisa
from main import hmp4040
def main():
    rm = pyvisa.ResourceManager()
    hmp4040_ps = rm.open_resource('ASRL6::INSTR')
    hmp4040 = hmp4040(pyvisa_instr=hmp4040_ps)
    hmp4040_ps.write('*RST')
    time.sleep(3)
    hmp4040_ps.close()
    print ("closed inst connection")

    
if __name__=='__main__':
    main()

