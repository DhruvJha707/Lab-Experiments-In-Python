'''Create a class to implement method Overriding. '''

class Parent:
    def show(self):
        print("This is Parent class method")

class Child(Parent):
    def show(self):   # Overriding parent method
        print("This is Child class method")

# Creating object of Child class
obj = Child()

# Calling overridden method
obj.show()
