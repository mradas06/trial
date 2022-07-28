
import pyvisa


def readDeviceName(self):
    self.write(b"IDN?\n")
    deviceName = self.read()
    print(deviceName)
    return deviceName
class hmp4040():

    def __init__(self,resource) -> None:
        self.resource = resource
        pass

    def write(self):
        return self.resource.write(str)

    def read(self):
        return self.resource.read(str)

    def setVoltage(self, voltage, channel):
        return self.write(b"INST OUT" + str(channel).encode() + b"\nVOLT " + str(voltage).encode() + b"\n")

    def setCurrent(self, current, channel):
        return self.write(b"INST OUT" + str(channel).encode() + b"\nCURR " + str(current).encode() + b"\n")

    def getVoltage(self, channel):
        self.write(b"INST OUT" + str(channel).encode() + b"\nMEAS:VOLT?\n")
        voltage = self.read()
        return float(voltage)

    def getCurrent(self, channel):
        self.write(b"INST OUT" + str(channel).encode() + b"\nMEAS:CURR?\n")
        current = self.read()
        return float(current)

    def getTargetVoltage(self, channel):
        self.write(b"INST OUT" + str(channel).encode() + b"\nVOLT?\n")      #limit#
        voltage = self.read()
        return float(voltage)

    def getTargetCurrent(self, channel):
        self.write(b"INST OUT" + str(channel).encode() + b"\nCURR?\n")      #limit#
        current = self.read()
        return float(current)

    def outputOn(self, channel):
        self.write(b"INST OUT" + str(channel).encode() + b"\nOUTP ON\n")    #channel on#
        return

    def outputOff(self, channel):
        self.write(b"INST OUT" + str(channel).encode() + b"\nOUTP OFF\n")   #channel off#
        print("channel turned off")
        return

    
   

