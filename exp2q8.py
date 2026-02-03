'''Print the grade sheet of a student for the given range of cgpa. Scan marks of five subjects 
and calculate the percentage. 
CGPA=percentage/10 
CGPA range: 
0 to 3.4 -> F 
3.5 to 5.0->C+ 
5.1 to 6->B 
6.1 to 7-> B+ 
7.1 to 8-> A 
8.1 to 9->A+ 
9.1 to 10-> O (Outstanding) 
Sample Gradesheet 
Name: Rohit Sharma 
Roll Number: R17234512   SAPID: 50005673 
Sem: 1      Course: B.Tech. CSE AI&ML 
 
Subject name: Marks 
PDS:   70 
Python:  80 
Chemistry:  90 
English:  60 
Physics:  50 
Percentage: 70% 
CGPA:7.0 
Grade:  '''


# student details
name = input("Enter Name: ")
roll = input("Enter Roll Number: ")
sapid = input("Enter SAPID: ")
sem = input("Enter Semester: ")
course = input("Enter Course: ")

# marks of five subjects
pds = int(input("Enter marks in PDS: "))
python = int(input("Enter marks in Python: "))
chemistry = int(input("Enter marks in Chemistry: "))
english = int(input("Enter marks in English: "))
physics = int(input("Enter marks in Physics: "))

# total and percentage
total = pds + python + chemistry + english + physics
percentage = total / 5

# CGPA calculation
cgpa = percentage / 10

# grade calculation
if cgpa >= 0 and cgpa <= 3.4:
    grade = "F"
elif cgpa >= 3.5 and cgpa <= 5.0:
    grade = "C+"
elif cgpa >= 5.1 and cgpa <= 6.0:
    grade = "B"
elif cgpa >= 6.1 and cgpa <= 7.0:
    grade = "B+"
elif cgpa >= 7.1 and cgpa <= 8.0:
    grade = "A"
elif cgpa >= 8.1 and cgpa <= 9.0:
    grade = "A+"
else:
    grade = "O (Outstanding)"

# printing grade sheet
print("\n      GRADE SHEET      ")
print("Name:", name)
print("Roll Number:", roll, " SAPID:", sapid)
print("Sem:", sem, " Course:", course)

print("\nSubject Name : Marks")
print("PDS :", pds)
print("Python :", python)
print("Chemistry :", chemistry)
print("English :", english)
print("Physics :", physics)

print("\nPercentage:", percentage, "%")
print("CGPA:", round(cgpa, 1))
print("Grade:", grade)
