import numpy as np

#3. Extract only the elements divisible by 3.

arr=np.array([10,20,30,40,50,60,70,80])
a=arr[arr%3==0]
print(a)