# Initialize an empty list to store lines of input
lines = []

# Read lines of input from the user
while True:
    line = input("Enter a line (leave empty to finish):\n")
    if line == "":
        break
    lines.append(line)

# Print all the lines entered
print("Lines entered:")
for line in lines:
    print(line)
