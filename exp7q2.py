''' Store integers in a file. 
a. Find the max number 
b. Find average of all numbers 
c. Count number of numbers greater than 100 '''


# --- Creating the file and writing integers ---
with open("numbers.txt", "w") as f:
    f.write("10\n")
    f.write("250\n")
    f.write("85\n")
    f.write("190\n")
    f.write("45\n")
    f.write("300\n")

# --- Reading numbers from the file ---
with open("numbers.txt", "r") as f:
    nums = [int(line.strip()) for line in f.readlines()]

# a. Find max number
max_num = max(nums)

# b. Find average of numbers
average = sum(nums) / len(nums)

# c. Count numbers greater than 100
count_greater_100 = sum(1 for n in nums if n > 100)

# --- Output ---
print("Numbers:", nums)
print("Maximum number:", max_num)
print("Average:", average)
print("Numbers greater than 100:", count_greater_100)
