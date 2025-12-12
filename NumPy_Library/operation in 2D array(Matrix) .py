import numpy as np
from numpy.testing.print_coercion_tables import print_new_cast_table

matrix=np.arange(1,13).reshape(3,4)
#print(matrix[0])        To access row in matrix
#print(matrix[0][3])     To access row's element

# 0 for row and 1 for column
#to access the row
print(matrix[0,:])
print(matrix[0,0:3])

print("_______________________________")

#In matrix slicing we use the slicing the extract the sub matrix
#matrix_name[slicing_row, slicing_column]
print(matrix[:,3])

print("_________________________________")

#Finding the first two column of the matrix
#Matrix[:]--> it will be access whole rows
#Matrix[:, 0:2]--> this will give the first two columns
print(matrix[:, 0:2])

print("__________________________________")

#Extract the sub matrix of 2*2
print(matrix[1:,2:])

print("___________________________________")

'''In numpy the random module is used to generate the random numbers
randiant--> It generates an array in given range, into which we can give number of elements
into this the start is inclusive'''
a=np.random.randint(1,11,10)
np.random.seed(32)
print(a)

print("____________________________________")
#np.random.rand is used to generate the values b/w 0 to 1
#into this function or method we pass the or elements which we want to generate
c=np.random.rand(20)
print(c)

print("____________________________________")
#to find average
s=np.array([1,2,3,4])
print(np.mean(s))

#np.median

#Flatten_matrix is used to put all the elements into one array
n=np.random.randint(1,10,12).reshape(3,4)
flatten_matrix=n.flatten()
print(flatten_matrix)
print("____________________________________")
ra=n.ravel()
n[0]=100
print(ra)

print("_____________________________________")
#Fancing indexing

a = np.array([10,20,30,40,50,60,70,80])
indices=[1,4,7]
arr = []
for i in indices:
    arr.append(a[i])

print(np.array(arr))
