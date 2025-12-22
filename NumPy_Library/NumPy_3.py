import numpy as np

l1 = [ x for x in range(1,101)]
a=np.array(l1)
# for checking the dimenstion of the array (.ndim)
print(a.ndim)

#l2=[[1,2,3],[4,5,6],[7,8,9]]
b=np.array([[1,2,3],[4,5,6],[7,8,9]])
#checking the shape of array
print(b.shape)
#chaeckin no: of element in array
print(b.size)

c=np.arange(1,26).reshape(5,5)
print(c.shape,c.size,c.ndim)

'''[.ones] this function is responsible for creating 
an array nd array of ( 1 is instialised) to all the element or position to matrix'''
d=np.ones((5,5),dtype=int)
print(d)

'''this function responsible for insitilised the 0 to all 
the position into the matrix'''
e=np.zeros((5,5),dtype=int)
print(e)