''' Input two values from user where the first line contains N, the number of test cases. The 
next N lines contain the space separated values of a and b. Perform integer division and print 
a/b. Handle exception in case of ZeroDivisionError or ValueError.  
Sample input 
1 0 
2 $ 
3 1  
Sample Output : 
Error Code: integer division or modulo by zero  
Error Code: invalid literal for int() with base 10: '$' 3'''

# Program to perform integer division with exception handling

# Read number of test cases
N = int(input())

for i in range(N):
    try:
        # Read two values
        a, b = input().split()
        
        # Convert to integers and perform integer division
        result = int(a) // int(b)
        
        # Print result
        print(result)
        
    except ZeroDivisionError as e:
        print("Error Code:", e)
        
    except ValueError as e:
        print("Error Code:", e)
