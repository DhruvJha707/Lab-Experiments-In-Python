'''Create a dictionary of n persons where key is name and value is city.  
a) Display all names 
b) Display all city names 
c) Display student name and city of all students. 
d) Count number of students in each city. '''

n = int(input("Enter number of persons: "))

people = {}

for _ in range(n):
    name = input("Enter name: ")
    city = input("Enter city: ")
    people[name] = city

print("\nAll Names:")
for name in people.keys():
    print(name)

print("\nAll City Names:")
for city in people.values():
    print(city)

print("\nName and City of All Students:")
for name, city in people.items():
    print(name, "->", city)

city_count = {}
for city in people.values():
    city_count[city] = city_count.get(city, 0) + 1

print("\nNumber of Students in Each City:")
for city, count in city_count.items():
    print(city, ":", count)
