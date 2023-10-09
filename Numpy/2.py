#BASIC ARRAY OPERATIONS

import numpy as np

a=np.array([5,6,9]) #single dimension
b=np.array([[1,7],[7,1]]) #double dimension

print(a.ndim,b.ndim) # prints the dimension of the array
print(a.itemsize) # prints the individual item size of each element
print(a.dtype) # prints the data type of the array (int32) mostly

#incase you want to initialize an np array with a specified data type
c=np.array([[1,2],[3,4],[5,6]], dtype=np.float64)
print(c.itemsize)
print(c.size) # total number of elements
print(c.shape) # dimensions 3,2

#Data type can also be complex : dtype=complex

#-----------------------------------------------------------------------------

# Create a two dimesnional array with all zeroes
print(np.zeros((3,4)))
print(np.ones((4,4)))

# Creating a list starting from 0 to 4
l=range(5)
print(l[0],l[1])

#Create a np array of a given range
print(np.arange(1,5))

#incase you want to have a step of 2 numbers
print(np.arange(1,5,2))

#create 10 lineary spaced numbers between 1 and 5
print(np.linspace(1,5,10))
print(np.linspace(1,5,5))

# Reshape the array having two dimensions
a=np.array([[1,2],[3,4],[5,6]])
print(a.shape)
print(a.reshape(2,3))
print(a.reshape(6,1))

#Flatten your array : use raven function
print(a.ravel()) #mind it, it won't change the original array

# ---------------------------------------------------------------------------

# Few Mathematical Functions

# Axis : axis 0 is for the columns and axis 1 is for the rows
print(a.sum(axis=0))

#Square root
print(np.sqrt(a))

#Standard Deviation
print(np.std(a))

# You can add double dimensional arrays as matrix addition just by using a+b
# a/b for division of individual elemnts between 2 matrixes

# Remember : a*b is for matrix multiplicatino of individual elements
# and, a.dot(b) is for a proper matrix multiplication

