'''1. Write a Python function to find the maximum and minimum numbers from a sequence of 
number'''

def find_max_min(numbers):
    if len(numbers) == 0:
        return None   # sequence empty

    maximum = numbers[0]
    minimum = numbers[0]

    i = 1
    while i < len(numbers):
        if numbers[i] > maximum:
            maximum = numbers[i]
        if numbers[i] < minimum:
            minimum = numbers[i]
        i += 1

    return maximum, minimum


# Example
nums = [12, 45, 7, 23, 89, 3]
max_val, min_val = find_max_min(nums)

print("Maximum =", max_val)
print("Minimum =", min_val)
