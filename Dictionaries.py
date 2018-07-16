# Dictionaries can be thought of as unordered key:value pairs
words = {}
words["Hello"] = "Bonjour"
words["Yes"] = "Oui"
words["No"] = "Non"
words["Bye"] = "Au Revoir"

print(words["Hello"])
print(words["No"])

dict = {}
dict["Ford"] = "Car"
dict["Python"] = "The Python Programming Language"
dict[2] = "This sentence is stored here"

print(dict["Ford"])
print(dict["Python"])
print(dict[2])

# Manipulating the dictionary
del words["Yes"]
print(words)
words["Yes"] = "Oui!"
print(words)
