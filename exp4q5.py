'''Given a string containing both upper and lower case alphabets. Write a Python program to 
count the number of occurrences of each alphabet (case insensitive) and display the same. 
Sample Input 
ABaBCbGc 
Sample Output 
2A 
3B 
2C 
1G'''

s = input("Enter the string: ")

s = s.upper()              # Make case insensitive
count = {}                 # Dictionary to store counts

for ch in s:
    if ch.isalpha():       # Consider only alphabets
        count[ch] = count.get(ch, 0) + 1

# Display in alphabetical order
for ch in sorted(count.keys()):
    print(str(count[ch]) + ch)
