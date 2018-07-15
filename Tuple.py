# Tuples are used to store a group of data

# Empty tuple
tuple = ()

# One item
tuple = (3,)

# Multiple items
personInfo = ("Diana", 32, "New York")

# Data access
print(personInfo[0])
print(personInfo[1])

# Assign multiple variables at once
name,age,country,career = ("Diana", 32, "United States", "CompSci")
print(country)

# Append to a tuple
x = (3,4,5,6)
x = x + (1,2,3)
print(x)
