'''Write a program to create two lists and generate a dictionary with keys from list1 and values 
from list2. '''

# Create two lists
list1 = ["a", "b", "c", "d"]
list2 = [10, 20, 30, 40]

# Create dictionary using list1 as keys and list2 as values
result_dict = dict(zip(list1, list2))

# Print the dictionary
print("Generated Dictionary:", result_dict)
