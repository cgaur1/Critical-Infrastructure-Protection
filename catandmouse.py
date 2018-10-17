from random import *

systems = ["firewall1", "firewall2", "dmz", "byod", "ics"]
attacker = "Default Attacker"

class CatMouse:

    def __init__(self):
        self.state = 0
        self.days = 0
        self.choice = 0


    def verifychoice(self):
        if self.choice > 0 and self.choice < 11:
            return True
        else:
            return False

    def printerror(self):
        print("\nError: Please enter a valid input")
        self.generateresult()

    def calculation(self):
        security = randint(1,10)
        if self.choice == security:
            return True
        else:
            return False

    def daysintime(self):
        self.days = self.days + randint(1,10)

    def generateresult(self):
        if self.state == 0:
            print("\nWelcome")
            print("\nThis is the beginning of your attack. Are you prepared?")
            print("\nThe system we are trying to infiltrate has strong security in some places and some places, not so strong.")
            print("\nLet's begin. Shall we?")
            self.choice = input("Press a number between 1 - 10 to attack the firewall system")
            check = self.verifychoice()
            if check == True:
                result = self.calculation()
                if result == True:
                    print("\nCONGRATULATIONS!!")
                    print("\nYou have passed. Proceed to the next obstacle.")
                    self.daysintime()
                    print("\nTime in days ", self.days)
                    self.state = 1
                    self.generateresult()
                else:
                    print("\nOoops. Looks like you weren't good enough.")
                    print("\nLet's try again?")
                    self.state = 0
                    self.daysintime()
                    print("\nTime in days ", self.days)
                    self.generateresult()
            else:
                self.state = 0
                self.printerror()

        if self.state == 1:
            print("\nLooks like they have another firewall in place.")
            print("\nHmm... Let's try to get through, shall we?")
            self.choice = input("Press a number between 1 - 10 to attack the firewall system")
            if self.verifychoice() == True:
                result = self.calculation()
                if result == True:
                    print("\nCONGRATULATIONS!!")
                    print("\nYou have passed. Proceed to the next obstacle.")
                    self.state = 2
                    self.daysintime()
                    print("\nTime in days ", self.days)
                    self.generateresult()
                else:
                    print("\nOoops. Looks like you weren't good enough.")
                    print("\nLet's try again?")
                    self.state = 1
                    self.daysintime()
                    print("\nTime in days ", self.days)
                    self.generateresult()
            else:
                self.state = 1
                self.printerror()
        if self.state == 2:
            print("\nYou have entered into what appears to be a De-militarised zone (DMZ).")
            print("\nLet's look around.")
            self.daysintime()
            print("\nTime in days ", self.days)
            print("\nThis seems pretty obsolete. Let's go back to the firewall and see if we find something unusual.")
            print("\nHmm, I might have missed a couple of other node points. Let's check them out.")
            self.choice = input("Press a number between 1 - 10 to discover more zones")
            if self.verifychoice() == True:
                result = self.calculation()
                if result == True:
                    print("\nCONGRATULATIONS!!")
                    print("\nYou have passed. Proceed to the next obstacle.")
                    self.state = 3
                    self.daysintime()
                    print("\nTime in days ", self.days)
                    self.generateresult()
                else:
                    print("\nOoops. Looks like you weren't good enough.")
                    print("\nLet's try again?")
                    self.state = 2
                    self.daysintime()
                    print("\nTime in days ", self.days)
                    self.generateresult()
            else:
                self.state = 2
                self.printerror()
        if self.state == 3:
            print("\nThis is interesting. I see a lot of devices in this network.")
            print("\nHowever, the devices are all random and network traffic also is irregular for a company.")
            print("\nMust be a bring-your-own-device zone. Ahh! How do I verify though?")
            self.daysintime()
            print("\nTime in days ", self.days)
            print("\nLet me get back to it later. Let's check out the other nodes.")
            self.choice = input("Press a number between 1 - 10 to find another node")
            if self.verifychoice() == True:
                result = self.calculation()
                if result == True:
                    print("\nCONGRATULATIONS!!")
                    print("\nYou have passed. Proceed to the next obstacle.")
                    self.state = 4
                    self.daysintime()
                    print("\nTime in days ", self.days)
                    self.generateresult()
                else:
                    print("\nOoops. Looks like you weren't good enough.")
                    print("\nLet's try again?")
                    self.state = 3
                    self.daysintime()
                    print("\nTime in days ", self.days)
                    self.generateresult()
            else:
                self.state = 3
                self.printerror()
        if self.state == 4:
            print("\nLooks like this is the ICS zone.")
            print("\nAbsolute GOLD! Now I can do some real harm!")
            self.daysintime()
            print("\nTime in days ", self.days)
            print("\nHow will I get into it though?")
            print("\nLet me try some known vulnerabilities. These guys never patch!!!")
            self.choice = input("Press a number between 1 - 10 to attack the ICS zone")
            if self.verifychoice() == True:
                result = self.calculation()
                if result == True:
                    print("\nCONGRATULATIONS!!")
                    print("\nYou successfully entered the ICS zone. Now prepare to bring down the MAN")
                    self.state = 6
                    self.daysintime()
                    print("\nTime in days ", self.days)
                    self.generateresult()
                else:
                    print("\nOoops. Looks like you weren't good enough.")
                    print("\nLet's try again?")
                    self.state = 0
                    self.daysintime()
                    print("\nTime in days ", self.days)
                    self.generateresult()
            else:
                self.state = 0
                self.printerror()

obj = CatMouse()
obj.generateresult()
