'''Write a program to print the sum of the following series 
1+ ½ + 1/3 + ¼ +….+1/n '''

n = int(input("Enter the value of n: "))

sum_series = 0

for i in range(1, n + 1):
    sum_series += 1 / i

print("Sum of the series =", sum_series)

