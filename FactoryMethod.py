# We may not always know what objects we want to create in advance
# The factory method is the idea of having one function that takes
# an input and outputs an object

class Car:
    def factory(type):
        if type == "Racecar":
            return Racecar()
        if type == "Van":
            return Van()
        assert 0, "Bad car creation: " + type

    factory = staticmethod(factory)

class Racecar(Car):
    def drive(self): print("Racecar driving...")
class Van(Car):
    def drive(self): print("Van driving...")

# Create object using factory
obj = Car.factory("Racecar")
obj.drive()
