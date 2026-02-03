#Find whether the given number is Armstrong number.

num = int(input("Enter a number: "))


digits = str(num)
power = len(digits)


sum_of_powers = sum(int(d)**power for d in digits)

if sum_of_powers == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
