# The 'random' module can generate pseudo-random numbers

from random import *

# Random floating point number between 0 and 1
print(random())

# Random whole number between 1 and 100
print(randint(1,100))

x = randint(1,100)
print(x)

# Random floating point number between 1 and 10
print(uniform(1,10))

# Fun with lists
items = [1,2,3,4,5,6,7,8,9,10]
shuffle(items)
print(items)

x = sample(items, 1)        # Pick a random item from list
print(x[0])

y = sample(items, 4)        # Pick 4 random items from list
print(y)
