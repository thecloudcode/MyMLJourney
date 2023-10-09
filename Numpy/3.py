# SLICING/ STACKING ARRAYS, INDEXING WITH BOOLEAN ARRAYS

# slicing here is exactly same as you slice in lists
# even a[-1] will work the same

import numpy as np

a=np.array([[1,2,3],[3,4,5],[5,6,7]])
b=np.array([[1,3,5],[2,4,6],[7,8,9]])
print(a[1,2])
print(a[0:2,2]) #taking into consideration the first 2 rows and printing the second elements of both the rows in single row
print(a[-1]) #last element, the last element here is the last row

print(a[:,1:3]) #printing the last columns

# Creating a two dimensional array with arange and reshape
a=np.arange(6).reshape(3,2)
print(a)

a=np.array([[1,2,3],[3,4,5],[5,6,7]])
b=np.array([[1,3,5],[2,4,6],[7,8,9]])
# Stacking two two dimensional arrays one over the another
print(np.vstack((a,b)))
print(np.hstack((a,b))) #Horizontal Stack

# Vertically slicing a very big array into multiple arrays
c=np.arange(30).reshape(2,15)
print(c)

print(np.hsplit(c,3))
print(np.vsplit(c,2))

# This is Special

a = np.arange(12).reshape(3,4)
print(a)
b=a>4
print(b)
print(a[b])
# incase you want to make all the True values to be -1 or something
a[b]=-1
print(a)