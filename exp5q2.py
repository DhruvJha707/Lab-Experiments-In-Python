#Create a tuple to store n numeric values and find average of all values.

n = int(input())

values = []

for _ in range(n):
    v = float(input())
    values.append(v)

values = tuple(values)

avg = sum(values) / n

print("Average =", avg)
