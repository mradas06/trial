import pyvisa
class hmp4040():

    def __init__(self, pyvisa_instr):
        self.hmp4040 = pyvisa_instr


    def readDeviceName(self):
        self.write(b"IDN?\n")
        deviceName = self.read()
        print(deviceName)
        return deviceName

    def setVoltage(self, voltage, channel):
        return self.write(b"INST OUT" + str(channel).encode() + b"\nVOLT " + str(voltage).encode() + b"\n")

    def setCurrent(self, current, channel):
        return self.write(b"INST OUT" + str(channel).encode() + b"\nCURR " + str(current).encode() + b"\n")

    def getVoltage(self, channel):
        self.write(b"INST OUT" + str(channel).encode() + b"\nMEAS:VOLT?\n")
        voltage = self.read()
        return float(voltage.strip())

    def getCurrent(self, channel):
        self.write(b"INST OUT" + str(channel).encode() + b"\nMEAS:CURR?\n")
        current = self.read()
        return float(current.strip())

    def getTargetVoltage(self, channel):
        self.write(b"INST OUT" + str(channel).encode() + b"\nVOLT?\n")      #limit#
        voltage = self.read()
        return float(voltage.strip())

    def getTargetCurrent(self, channel):
        self.write(b"INST OUT" + str(channel).encode() + b"\nCURR?\n")      #limit#
        current = self.read()
        return float(current.strip())

    def outputOn(self, channel):
        self.write(b"INST OUT" + str(channel).encode() + b"\nOUTP ON\n")
        return

    def outputOff(self, channel):
        self.write(b"INST OUT" + str(channel).encode() + b"\nOUTP OFF\n")
        return
    print("channel turned off")

    exit()
    
