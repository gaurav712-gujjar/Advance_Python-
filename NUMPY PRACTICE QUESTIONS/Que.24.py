import numpy as np

#Add a 1D array of shape (3,) to a 2D array of shape (2, 3) using broadcasting.

arr=np.array([10,20,30])
mat=np.array([[1,2,3],
               [4,5,6]])
print(arr+mat)

