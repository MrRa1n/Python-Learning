# Classes can inherit functionality of other classes
# Python supports inheritance from multiple classes

class User:
    name = ""

    def __init__(self, name):
        self.name = name

    def printName(self):
        print("Name = " + self.name)

class Programmer(User):
    def __init__(self, name):
        self.name = name

    def doPython(self):
        print("Programming Python")

# Brian is instance of User class
brian = User("Brian")
brian.printName()

# Diana is instance of Programmer class that inherits from User
diana = Programmer("Diana")
diana.printName()
diana.doPython()
