'''Write a Python function that takes a positive integer and returns the sum of the cube of all 
the positive integers smaller than the specified number.'''

def sum_of_cubes(n):
    if n <= 1:
        return 0
    return sum(i**3 for i in range(1, n))

def main():
    num = int(input("Enter a positive integer: "))
    result = sum_of_cubes(num)
    print(f"The sum of cubes of all positive integers smaller than {num} is: {result}")

if __name__ == "__main__":
    main()
