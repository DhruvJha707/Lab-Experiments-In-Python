''' Write a lambda function to find volume of cone. '''

import math

volume_cone = lambda r, h: (1/3) * math.pi * r**2 * h

# Example
print(volume_cone(3, 5))  # radius = 3, height = 5
