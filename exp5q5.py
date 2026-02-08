''' Store details of n movies in a dictionary by taking input from the user. Each movie must 
store details like name,  year, director name, production cost, collection made (earning) & 
perform the following :- 
a) print all movie details 
b) display name of movies released before 2015 
c) print movies that made a profit. 
'''
n = int(input("Enter number of movies: "))

movies = {}

for _ in range(n):
    name = input("Movie name: ")
    year = int(input("Year: "))
    director = input("Director name: ")
    cost = float(input("Production cost: "))
    earning = float(input("Collection made: "))

    movies[name] = {
        "year": year,
        "director": director,
        "cost": cost,
        "earning": earning
    }

print("\n--- All Movie Details ---")
for name, details in movies.items():
    print(name, ":", details)

print("\n--- Movies Released Before 2015 ---")
for name, details in movies.items():
    if details["year"] < 2015:
        print(name)

print("\n--- Movies That Made a Profit ---")
for name, details in movies.items():
    if details["earning"] > details["cost"]:
        print(name)
