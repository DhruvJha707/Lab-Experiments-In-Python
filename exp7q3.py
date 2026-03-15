'''Assume a file city.txt with details of 5 cities in given format (cityname population(in lakhs) 
area(in sq KM) ): 
Example: 
Dehradun 5.78 308.20 
Delhi 190 1484 
…………… 
Open file city.txt and read to: 
a. Display details of all cities 
b. Display city names with population more than 10Lakhs 
c. Display sum of areas of all cities'''


# --- Reading city.txt file ---
with open("city.txt", "r") as f:
    cities = f.readlines()

city_data = []

for line in cities:
    parts = line.split()

    if len(parts) < 3:
        continue

    try:
        city = parts[0]
        population = float(parts[1])
        area = float(parts[2])

        city_data.append((city, population, area))
    except ValueError:
        continue


# a. Display details of all cities
print("All City Details:")
for c, p, a in city_data:
    print("City:", c, "Population:", p, "Lakhs Area:", a, "sq km")

print()


# b. Cities with population > 10 lakhs
print("Cities with population more than 10 lakhs:")
for c, p, a in city_data:
    if p > 10:
        print(c)

print()


# c. Sum of all city areas
total_area = sum(a for c, p, a in city_data)

print("Total area of all cities:", total_area, "sq km")
