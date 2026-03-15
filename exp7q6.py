''' Write a program to create a counter to show that how many times the program is executed.'''

# Program to count how many times it has been executed

import os

filename = "counter.txt"

# If file does not exist, create it with value 0
if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("0")

# Read the current count
with open(filename, "r") as f:
    count = int(f.read())

# Increase count
count += 1

# Write updated count back to file
with open(filename, "w") as f:
    f.write(str(count))

# Display execution count
print("This program has been executed", count, "times.")
