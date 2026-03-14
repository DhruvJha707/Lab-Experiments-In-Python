'''Write a program to check whether all the values in a dictionary are same or not using lambda 
function. '''

data = {"a": 10, "b": 10, "c": 10, "d": 10}

# Lambda to check if all values are same
all_same = lambda d: len(set(d.values())) == 1

# Result
if all_same(data):
    print("All values are the same.")
else:
    print("Values are not the same.")
