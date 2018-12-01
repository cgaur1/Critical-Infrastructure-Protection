from random import *
import time
from threading import Timer

class MBAN:
    def __init__(self):
        self.acelLevel = 100
        self.hrmLevel = 100
        self.PulseLevel = 100
        self.sensorLevel = 100
        self.hubLevel = 100
        self.acelData = 0
        self.hrmData = 0
        self.PulseData = 0
        self.sensorData = 0
        self.hubData = 0
        self.attacker = 0

    def main(self):
        print("Hub Battery Level " + str(self.hubLevel))
        print("Heart Rate Monitor Battery Level " + str(self.hrmLevel))
        print("Pulse Battery Level " + str(self.PulseLevel)  )
        print("Sensor Battery Level " + str(self.sensorLevel)  )
        print("Accelerometer Battery Level " + str(self.acelLevel)  )
        if self.hubLevel <= 0:
            print ("Hub Shutting Down")
        else:
            luck = randint(1, 4)
            if luck == 3:
                self.Attacker(luck)
            self.SendData(self.acelLevel,1)
            self.SendData(self.sensorLevel, 2)
            self.SendData(self.PulseLevel, 3)
            self.SendData(self.hrmLevel, 4)

    def initialize(self, choice):
        if choice == 1:
            self.Accelerometer(0)
            self.acelData = 0
        if choice == 2:
            self.Sensor(2, 0)
            self.sensorData = 0
        if choice == 3:
            self.Pulse(2, 0)
            self.PulseData = 0
        if choice == 4:
            self.HRM(2, 0)
            self.hrmData = 0



    def SendData(self,level, node):
        if level <= 100 and level > 84:
            time.sleep(2)
            self.initialize(node)
        elif level > 68 and level <= 84:
            time.sleep(4)
            self.initialize(node)
        elif level > 68 and level <= 52:
            time.sleep(6)
            self.initialize(node)
        elif level > 52 and level <= 36:
            time.sleep(8)
            self.initialize(node)
        elif level > 36 and level <= 20:
            time.sleep(9)
            self.initialize(node)
        elif level < 20:
            time.sleep(10)
            self.initialize(node)
        elif level <=0:
            self.main()



    def Hub(self, choice, data):
        self_data = randint(1,5)
        if choice == 1:
            self.hubData += data
            print("Data received" + str(self.hubData))
            if self.hubData < 80:
                print("Normal Data Levels")
            elif self.hubData >= 80:
                print("$$$$$ ALERT: SUSPICIOUS MESSAGE RECEIVED $$$$$")
                if self.attacker == 0:
                    print("FALSE ALARM \n\n")
                else:
                    print("POSITIVE FOR ATTACK \n\n")
        self.hubData = 0
        self.main()

    def HRM(self, choice, data):
        self_data = randint(1,5)
        if choice == 1:
            self.hrmData += data
        elif choice == 2:
            self_data = randint(5,10)
            print("HRM Data = " + str(self_data))
            energy = randint(5,10) + self_data
            print("HRM Energy = " + str(energy))
            self.hrmLevel = self.hrmLevel - energy
            print("HRM Battery Level= " + str(self.hrmLevel))
            self.hrmData += self_data
            self.Hub(1, self.hrmData)

    def Pulse(self, choice, data):
        self_data = randint(1,5)
        if choice == 1:
            self.PulseData += data
        elif choice == 2:
            self_data = randint(5,10)
            print("Pulse Data = " + str(self_data))
            energy = randint(5,10) + self_data
            print("Pulse Energy = " + str(energy))
            self.PulseLevel = self.PulseLevel - energy
            print("Pulse Battery Level= " + str(self.PulseLevel))
            self.PulseData += self_data
            self.HRM(1, self.PulseData)

    def Sensor(self, choice, data):
        self_data = randint(1,5)
        if choice == 1:
            self.sensorData += data
        elif choice == 2:
            self_data = randint(5,10)
            print("Sensor Data = " + str(self_data))
            energy = randint(5,10) + self_data
            print("Sensor Energy = " + str(energy))
            self.sensorLevel = self.sensorLevel - energy
            print("Sensor Battery Level= " + str(self.sensorLevel))
            self.sensorData += self_data
            self.Pulse(1, self.sensorData)

    def Accelerometer(self, data):
        self_data = randint(5,10)
        print("Accelerometer Data = " + str(self_data))
        energy = randint(5,10) + self_data
        print("Accelerometer Energy = " + str(energy))
        self.acelLevel = self.acelLevel - energy
        print("Accelerometer Battery Level= " + str(self.acelLevel))
        self.acelData += self_data
        self.Sensor(1, self.acelData)

    def Attacker(self, choice):
        print("Attacker Invoked")
        self.attacker = 1
        self_data = randint(10,20)
        if choice == 1:
            self.Accelerometer(self_data)
        if choice == 2:
            self.Sensor(1, self_data)
        if choice == 3:
            self.Pulse(1, self_data)
        if choice == 4:
            self.HRM(1, self_data)

obj = MBAN()
obj.main()
