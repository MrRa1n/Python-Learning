# Private methods
class Car:

    def __init__(self):
        self.__updateSoftware()

    def drive(self):
        print("Driving")

    def __updateSoftware(self):
        print("Updating software")

redcar = Car()
redcar.drive()
# redcar.__updateSoftware() - Not accessible from object

# Private variables
class Bike:
    __maxspeed = 0
    __name = ""

    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Superbike"

    def drive(self):
        print("Driving. Max speed = " + str(self.__maxspeed))

    def setMaxSpeed(self, speed):
        self.__maxspeed = speed

redbike = Bike()
redbike.drive()
redbike.__maxspeed = 10     # Will not change variable
redbike.setMaxSpeed(320)
redbike.drive()
