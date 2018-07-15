# By default all variables in Python are local unless defined as global

# This code will not run as z cannot be reached
def f(x,y):
    print("You called f(x,y) with the value x = " + str(x) + " and y = " + str(y))
    print("x * y = " + str(x*y))
    z = 4

z = 3
f(3,2)

# This code will run
def f(x,y):
    z = 3
    print("You called f(x,y) with the value x = " + str(x) + " and y = " + str(y))
    print("x * y = " + str(x*y))
    print(z)

f(3,2)

# Further examination
def f(x,y,z):
    return x+y+z        # returns sum as all parameters defined

sum = f(3,2,1)
print(sum)

# Calling functions within functions
def highFive():
    return 5

def f(x,y):
    z = highFive()      # value returned from highFive() stored
    return x+y+z        # sums values as z is reachable

result = f(3,2)
print(result)
