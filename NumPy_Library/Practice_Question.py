import numpy as np

#generate a matrix using the random module radint, last column
a=np.random.randint(1,10,12).reshape(3,4)
print(a)
print(a[:,2:])

#2d element--> mean --> flatter -- mean
print("___________________________________")
arr1=np.arange(10,35)
print(np.where(arr1<18))