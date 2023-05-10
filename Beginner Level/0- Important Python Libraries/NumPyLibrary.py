'''
NumPy


NumPy is a library for numerical computing in Python. It provides support for large, 
multi-dimensional arrays and matrices, along with a collection of mathematical 
functions to operate on these arrays efficiently.

Example use case: Calculate the dot product of two vectors.
'''

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

dot_product = np.dot(a, b)

print(dot_product)
