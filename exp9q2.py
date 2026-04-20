'''Add constructor in the above class to initialize student details of n students and implement 
following methods: 
a) Display() student details 
b) Find Marks_percentage() of each student 
c)  Display result() [Note: if marks in each subject >40% than Pass else Fail] 
d) Write a Function to find average of the class. '''

class Student:
    def __init__(self, name, sap_id, phy, chem, maths):
        self.name = name
        self.sap_id = sap_id
        self.phy = phy
        self.chem = chem
        self.maths = maths

    # a) Display student details
    def display(self):
        print("\nStudent Details:")
        print("Name:", self.name)
        print("SAP ID:", self.sap_id)
        print("Physics:", self.phy)
        print("Chemistry:", self.chem)
        print("Mathematics:", self.maths)

    # b) Find Marks Percentage
    def marks_percentage(self):
        total = self.phy + self.chem + self.maths
        percentage = total / 3
        return percentage

    # c) Display Result
    def result(self):
        if self.phy > 40 and self.chem > 40 and self.maths > 40:
            return "Pass"
        else:
            return "Fail"


# d) Function to find class average percentage
def class_average(students):
    total_percentage = 0
    for s in students:
        total_percentage += s.marks_percentage()
    return total_percentage / len(students)


# Main Program
students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print(f"\nEnter details for Student {i+1}:")
    name = input("Enter name: ")
    sap_id = input("Enter SAP ID: ")
    phy = float(input("Enter Physics marks: "))
    chem = float(input("Enter Chemistry marks: "))
    maths = float(input("Enter Mathematics marks: "))

    s = Student(name, sap_id, phy, chem, maths)
    students.append(s)

# Display all details
print("\n--- Student Records ---")
for s in students:
    s.display()
    print("Percentage:", s.marks_percentage())
    print("Result:", s.result())

# Display class average
avg = class_average(students)
print("\nClass Average Percentage:", avg)
