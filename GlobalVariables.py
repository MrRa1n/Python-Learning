# Local variables
def sum(x,y):
    sum = x + y
    return sum

print(sum(8,6))

# Global variables
z = 10
def afunction():
    global z
    z = 9

afunction()
print(z)

# Exercise
z = 10

def func1():
    global z
    z = 3

def func2(x,y):
    global z
    return x+y+z

func1()
total = func2(4,5)
print(total)
