import pyvisa 
from time import sleep
class HMP4040():
    

    def __init__(self,resource: pyvisa.Resource) -> None:
        self.resource = resource
        pass

    def readDeviceName(self):
        self.resource.write(b"IDN?\n")
        deviceName = self.resource.read()
        print(deviceName)
        return deviceName

    def write(self, str):
        return self.resource.write(str) 

    def read(self, str):
        return self.resource.read(str)
        
        
    def powerON(self):
        self.resource.write(':OUTPut:STATe %d' % 1)
        return print("power supply is ON")

    def powerOFF(self):
        self.resource.write(':OUTPut:STATe %d' % 0)
        return print("power supply is OFF")

    delay = 1                   #1 sn delay
    print("delayed")
    sleep(delay)
    print("working")

    def setVoltage(self, voltage, channel):
        return self.resource.write(b"INST OUT" + str(channel).encode() + b"\nVOLT " + str(voltage).encode() + b"\n")

    def setCurrent(self, current, channel):
        return self.resource.write(b"INST OUT" + str(channel).encode() + b"\nCURR " + str(current).encode() + b"\n")

    def getVoltage(self, channel):
        self.resource.write(b"INST OUT" + str(channel).encode() + b"\nMEAS:VOLT?\n")
        voltage = self.read()
        return float(voltage)

    def getCurrent(self, channel):
        self.resource.write(b"INST OUT" + str(channel).encode() + b"\nMEAS:CURR?\n")
        current = self.read()
        return float(current)

    def getTargetVoltage(self, channel):
        self.resource.write(b"INST OUT" + str(channel).encode() + b"\nVOLT?\n")      #limit# ###min max ayrı veya değil bakk
        voltage = self.read()
        return float(voltage)

    def getTargetCurrent(self, channel):
        self.resource.write(b"INST OUT" + str(channel).encode() + b"\nCURR?\n")      #limit#
        current = self.read()
        return float(current)

    def outputOn(self, channel):
        self.resource.write(b"INST OUT" + str(channel).encode() + b"\nOUTP ON\n")    #channel on#
        return

    def outputOff(self, channel):
        self.resource.write(b"INST OUT" + str(channel).encode() + b"\nOUTP OFF\n")   #channel off#
        print("channel turned off")
        return
    
    



