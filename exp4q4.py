''' WAP to enter a string and a substring. You have to print the number of times that the 
substring occurs in the given string. String traversal will take place from left to right, not 
from right to left. 
Sample Input 
ABCDCDC 
CDC 
Sample Output 
2 '''

string = input("Enter the string: ")
substring = input("Enter the substring: ")

count = 0
start = 0

while True:
    pos = string.find(substring, start)
    if pos == -1:
        break
    count += 1
    start = pos + 1   # Move one step to the right for overlapping matches

print(count)
