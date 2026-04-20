'''1.Create a class of student (name, sap id, marks[phy,chem,maths] ). Create 3 objects by               
taking inputs from the user and display details of all students. '''

class Student:
    def __init__(self, name, sap_id, phy, chem, maths):
        self.name = name
        self.sap_id = sap_id
        self.marks = {
            "Physics": phy,
            "Chemistry": chem,
            "Mathematics": maths
        }

    def display(self):
        print("\nStudent Details:")
        print("Name:", self.name)
        print("SAP ID:", self.sap_id)
        print("Marks:")
        for subject, mark in self.marks.items():
            print(f"  {subject}: {mark}")


# Creating list to store 3 students
students = []

# Taking input for 3 students
for i in range(3):
    print(f"\nEnter details for Student {i+1}:")
    name = input("Enter name: ")
    sap_id = input("Enter SAP ID: ")
    phy = float(input("Enter Physics marks: "))
    chem = float(input("Enter Chemistry marks: "))
    maths = float(input("Enter Mathematics marks: "))

    student = Student(name, sap_id, phy, chem, maths)
    students.append(student)

# Displaying details of all students
print("\n--- All Student Details ---")
for s in students:
    s.display()
