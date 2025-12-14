import numpy as np

#scaler operation(*,+,-)
#we can add signal no: and two array
a=np.array([1,2,3,4])
b=np.array([5,6,7,8])
print(a+b)
print("______________________________")

#Add every element of array in the row and column of matrix
a1=np.arange(1,13).reshape(3,4)
a2=np.array([1,2,3,4])
print(a1+a2)
print("______________________________")

#broadcasting rules
#--> they are equal in size
#--> one of them has a size of 0
a3=np.array([1,2,3]).reshape(3,1)
print(a1+a3)
print("______________________________")

#Rule.1-->According to the rule no.1 of the boardcasting, the dimensions
#of both matrices have same dimensions.
mat1=np.arange(1,10).reshape(3,3)
mat2=np.arange(10,19).reshape(3,3)
print(mat1+mat2)
print("______________________________")

#Rule.2-->Equal in size.
#One of them has a size of 1
mat=mat1=np.arange(1,13).reshape(3,4)
arr=np.array([1,2,3]).reshape(3,1)
print(mat+arr)


