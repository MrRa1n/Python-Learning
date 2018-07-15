# For loops
items = ["Abby","Brenda","Cindy","Diddy"]

for item in items:
    print(item)

for i in range(1,10):
    print(i)

# While loops
correctNumber = 5
guess = 0

while guess != correctNumber:
    guess = int(input("Guess the number: "))

    if guess != correctNumber:
        print("False guess")

print("You guessed the correct number")

# Nested loops
for x in range(1,10):
    for y in range(1,10):
        print("(" + str(x) + "," + str(y) + ")")
