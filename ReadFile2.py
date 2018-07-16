import os.path

# Define a filename
filename = "myfile.txt"

if not os.path.isfile(filename):
    print("File does not exist.")
else:
    # Open the file as f
    with open(filename) as f:
        content = f.read().splitlines()
    # Show the file contents line by line
    for line in content:
        print(line)
