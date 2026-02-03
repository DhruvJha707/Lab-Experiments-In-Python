#Check whether the given number is divisible by 3 and 5 both.

num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("The number is divisible by both 3 and 5")
else:
    print("The number is NOT divisible by both 3 and 5")

