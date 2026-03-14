''' Write functions to explain mentioned concepts: 
a. Keyword argument 
b. Default argument 
c. Variable length argument '''

# a. Keyword Argument
def keyword_example(name, age):
    print("Keyword Argument Example:")
    print(f"Name: {name}, Age: {age}\n")

# b. Default Argument
def default_example(name, city="Delhi"):
    print("Default Argument Example:")
    print(f"Name: {name}, City: {city}\n")

# c. Variable Length Argument
def variable_length_example(*numbers):
    print("Variable Length Argument Example:")
    print("Numbers received:", numbers)
    print("Sum =", sum(numbers), "\n")

# ---------- Calling the functions ----------

# Keyword argument
keyword_example(name="Alice", age=21)

# Default argument
default_example("Bob")
default_example("Bob", "Mumbai")

# Variable length argument
variable_length_example(10, 20, 30, 40)
