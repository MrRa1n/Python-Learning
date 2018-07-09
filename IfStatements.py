x = 3
if x < 10:
    print("x is smaller than 10")
else:
    print("x is bigger than 10 or equal")

# Age guessing game
age = 21

print("What is my age?")
guess = int(input("Guess: "))

if guess != age:
    print("Wrong!")
else:
    print("Correct!")

# Nested if statements
a = 12
b = 33

if a > 10:
    if b > 20:
        print("Good")

# Using the 'and' keyword
guess = 19
if guess > 10 and guess < 20:
    print("In range")
else:
    print("Out of range")
