#Convert all lower cases to upper case in a string.

s = input("Enter a string: ")

result = ""

for ch in s:
    if 'a' <= ch <= 'z':          # check if lowercase
        result += chr(ord(ch) - 32)   # convert to uppercase
    else:
        result += ch

print("Uppercase string:", result)
