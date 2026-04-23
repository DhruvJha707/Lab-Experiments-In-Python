''' Perform Matrix multiplication of any 2 n*n matrices. '''

import numpy as np

matrix_a = np.array([[1, 2], [3, 4]])

matrix_b = np.array([[5, 6], [7, 8]])

result = np.dot(matrix_a, matrix_b)

print("Result of matrix multiplication:\n", result)

