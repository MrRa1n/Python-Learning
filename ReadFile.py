# Define a filename
filename = "myfile.txt"

# Open the file as f and read lines
with open(filename) as f:
    # readlines()
    content = f.read().splitlines()

# Show file contents line by line
for line in content:
    print(line),
