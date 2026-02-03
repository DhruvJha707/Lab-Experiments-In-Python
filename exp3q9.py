'''Print the table for a given number:  
             5 * 1 = 5 
             5 * 2 = 10……….. '''


num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "*", i, "=", num * i)
