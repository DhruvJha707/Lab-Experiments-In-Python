'''Take two sets and apply various set operations on them : 
S1 = {Red ,yellow, orange , blue } 
S2 = {violet, blue , purple}'''

S1 = {"Red", "yellow", "orange", "blue"}
S2 = {"violet", "blue", "purple"}

print("Union:", S1.union(S2))
print("Intersection:", S1.intersection(S2))
print("S1 - S2:", S1.difference(S2))
print("S2 - S1:", S2.difference(S1))
print("Symmetric Difference:", S1.symmetric_difference(S2))
