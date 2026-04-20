''' Create a class for operator overloading which adds two Point Objects where Point has x & 
y values 
e.g. if 
P1(x=10,y=20) 
P2(x=12,y=15) 
P3=P1+P2 => P3(x=22,y=35) '''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading + operator
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Point(new_x, new_y)

    def display(self):
        print(f"Point(x={self.x}, y={self.y})")


# Creating objects
P1 = Point(10, 20)
P2 = Point(12, 15)

# Adding objects
P3 = P1 + P2

# Display results
print("P1:")
P1.display()

print("P2:")
P2.display()

print("P3 = P1 + P2:")
P3.display()
