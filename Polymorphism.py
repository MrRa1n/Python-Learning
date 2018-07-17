# Polymorphism is the idea that something can take many forms
class Bear(object):
    def sound(self):
        print("Groarrr")

class Dog(object):
    def sound(self):
        print("Woof")

def makeSound(animalType):
    animalType.sound()

bearObj = Bear()
dogObj = Dog()

makeSound(bearObj)
makeSound(dogObj)

# Polymorphism with abstract class
class Document:
    def __init__(self, name):
        self.name = name

    def show(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Pdf(Document):
    def show(self):
        return "Show PDF contents!"

class Word(Document):
    def show(self):
        return "Show Word contents!"

documents = [Pdf("Document1"),Pdf("Document2"),Word("Document3")]

for document in documents:
    print(document.name + ": " + document.show())
