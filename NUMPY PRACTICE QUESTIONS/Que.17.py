import numpy as np

#2. Replace all negative values in an array with 0.

arr=np.array([1,2,3,-4,-5,6,7,-1,-2])
arr[arr<0]=0
print(arr)