import numpy as np

a=np.array([1,2,3])                             #1d array
b=np.array([[1,2,3],[4,5,6]])                   #2d array
c=np.array([[[7,8,9],[10,11,12],[13,14,15]]])   #3d array
print(a.ndim)                   #to know dimention
print(b.ndim)
print(c.ndim)

#(3,4) tuple-> row and column
#((3,4),dtype=int to convert its in integer
d=np.zeros((3,4))               #to print matrix
print(d.ndim)

#similer to np.zeros
e=np.ones((5,6))
print(e.ndim)

#it gives value in digonal
f=np.eye(3)
print(f)
