# ITERATE THROUGH NUMPY ARRAY USING NDITER
import numpy as np

a = np.arange(12).reshape(3,4)
for row in a:
    for cell in row:
        print(cell)

# all the commands above can be done using nditer
for x in np.nditer(a,order="C"): # C order
    print(x)
for x in np.nditer(a,order="F"): # Fortan order
    print(x)

# use of flags in nditer
for x in np.nditer(a,order="F",flags = ['external_loop']):
    print(x)

# modify the elemnts in the array while iterating
for x in np.nditer(a,op_flags=['readwrite']):
    x[...]=x*x
print(a)

#Iterate through 2 Numpy arrays at the same time
for i,j in np.nditer([a,a]):
    print(i*j)

#make sure the dimensions do not collide with each other