import numpy as np

#To create array in a range (start,end,step)
#In reshape give factor of n*n which is equal to total number of element
#reshape => n*n -> total no of element
a=np.arange(1,13).reshape(2,6)
print(a)

#it include start and end
b=np.linspace(10,30,5)
print(b)

x=np.linspace(10,20,12).reshape(3,4)
y=np.linspace(30,40,12).reshape(3,4)
add=x+y
print(add)