'''Create 2 sets s1 and s2 of n fruits each by taking input from user and find: 
a) Fruits which are in both sets s1 and s2 
b) Fruits only in s1 but not in s2 
c) Count of all fruits from s1 and s2'''


# Input number of fruits in each set
n = int(input("Enter number of fruits in each set: "))

# Input fruits for set s1
print("Enter fruits for set s1:")
s1 = set()
for _ in range(n):
    s1.add(input().strip().lower())

# Input fruits for set s2
print("Enter fruits for set s2:")
s2 = set()
for _ in range(n):
    s2.add(input().strip().lower())

# a) Fruits in both sets
common = s1.intersection(s2)

# b) Fruits only in s1 but not in s2
only_s1 = s1.difference(s2)

# c) Count of all unique fruits from both sets
total_unique = len(s1.union(s2))

# Output results
print("a) Fruits in both sets:", common)
print("b) Fruits only in s1:", only_s1)
print("c) Count of all unique fruits:", total_unique)
