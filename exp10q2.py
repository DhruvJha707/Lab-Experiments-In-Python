''' Create numpy array of (3,3) dimension. Now find sum of all rows & columns individually. 
Also find 2nd maximum element in the array.'''

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

row_sum = np.sum(arr, axis=1)

col_sum = np.sum(arr, axis=0)

second_max = np.partition(arr.flatten(), -2)[-2]

print("Sum of each row:", row_sum)

print("Sum of each column:", col_sum)

print("The 2nd maximum element in the array is:", second_max)

