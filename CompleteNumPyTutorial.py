# -*- coding: utf-8 -*-
"""
Created on Wed May 25 07:58:52 2022

@author: Naveen
"""

import numpy as np 

a = np.array([1, 2, 3])
# print(a)

b = np.array([[9.0,8.0,7.0], [6.0, 5.0, 4.0]])
# print(b)

# Get Dimension 
a.ndim
b.ndim

# Get shape 
a.shape
b.shape

# Get Type 
a.dtype

# Get size 
a.itemsize

# Get total size 
a.size * a.itemsize
a.nbytes

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])

# Get a specific element [r, c]
a[1, 5]

# Get a specific row 
a[0, :]

# Get a specific column 
a[:, 2]

# Getting a little more fancy [startindex:endindex:stepsize]
a[0, 1:6:2]

a[1,5] = 20
a[:, 2] = [1, 2]
# print(a)

b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# print(b)

b[:, 1, :] = [[9,99],[8,8]]

# initalizing different types of arrays 
# All 0s matrix 
np.zeros(5)

np.zeros((2,3,))
# All 1s matrix
np.ones((4, 2, 2), dtype='int32')

# Any other number 
np.full((2,2), 99, dtype='float32')

# Any other number (full_like)
np.full_like(a, 4)

# Random decimal numbers
np.random.rand(4,2)

# Random Integer values 
np.random.randint(-4,8, size=(3,3))

# The identity matrix 
np.identity(5)

# Repeat an array 
arr = np.array([[1,2,3]])
r1 = np.repeat(arr, 3, axis=0)
# print(r1)

# Example:
output = np.ones((5,5))
# print(output)

z = np.zeros((3,3))
z[1,1] = 9
# print(z)

output[1:4, 1:4] = z
# print(output)

# Be careful when copying arrays!!!
a = np.array([1,2,3])
b = a
# use b = a.copy() instead to avoid aliasing
b[0] = 100
# print(a)

a = np.array([1,2,3,4])
# print(a)

a + 2
a-2
a * 2
a /2

b = np.array([1,0,1,0])
a+b
a ** 2

# Take the sin 
np.sin(a)

# Linear Algebra 
a = np.ones((2,3))
b = np.full((3,2), 2)





