# Write a program to count and display the number of capital letters in a given string.


text = input("Enter a string: ")

count = 0
for char in text:
    if char.isupper():
        count += 1

print("Number of capital letters:", count)
