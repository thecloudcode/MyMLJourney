#NUMPY ARRAY VS PYTHON LIST

#array over list: better memory, speed and more convinient

a=np.array([12,7])
print(a)

# a.size : size of the array
# a.itemsize : size of each item in the array

# numpy array : data, dimensions, strides
# python list : length and items, it has pointers which point to various locations (Contigous)

# checking which is faster python list or numpy array

import time
import sys

SIZE = 1000000

l1 = range(SIZE)
l2 = range(SIZE)

a1=np.array(SIZE)
a2=np.array(SIZE)

start = time.time()
result = [(x+y) for x,y in zip(l1,l2)]
print("Python List took: ", (time.time()-start)*1000)

start = time.time()
result = a1+a2
print("Numpy took : ", (time.time()-start)*1000)

# clearly you will see that numpy array is much faster


