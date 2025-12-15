import numpy as np

#Perform matrix multiplication of two compatible matrices.

mat=np.arange(1,10).reshape(3,3)
mat1=np.arange(1,10).reshape(3,3)
mul=mat*mat1
print(mul)