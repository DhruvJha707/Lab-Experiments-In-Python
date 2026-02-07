'''Scan n values in range 0-3 and print the number of times each value has occurred.'''

n = int(input())

count = [0] * 4

for _ in range(n):
    v = int(input())
    if 0 <= v <= 3:
        count[v] += 1

for i in range(4):
    print(f"Value {i} occurred {count[i]} times.")
