# Statements - commands only
# Functions - reusable group of statements
# Classes - used to create objects which have functions and variables

class User:
    name = ""

    # Constructor
    def __init__(self, name):
        self.name = name

    def sayHello(self):
        print("Hello, my name is " + self.name)

# Create virtual objects
james = User("James")
david = User("David")
eric = User("Eric")

# Call methods owned by virtual objects
james.sayHello()
david.sayHello()
