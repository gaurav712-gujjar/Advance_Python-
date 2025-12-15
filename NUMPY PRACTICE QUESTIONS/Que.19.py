import numpy as np

#4. Count how many elements are greater than the mean of the array.

arr=np.array([1,2,3,4,5,6])
a=np.mean(arr)
count=0
for i in arr:
    if i>a:
        count+=1

print(count)