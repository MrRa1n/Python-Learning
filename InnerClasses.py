# An inner class is defined entirely within the body of another class
# A class can have more than one inner class, but in general inner
# classes are avoided

class Human:
    def __init__(self):
        self.name = "Guido"
        self.head = self.Head()

    class Head:
        def talk(self):
            return "Talking..."

if __name__ == "__main__":
    guido = Human()
    print(guido.name)
    print(guido.head.talk())
