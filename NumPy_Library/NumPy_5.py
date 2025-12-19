import numpy as np

#Using list
li=[[1,2,3],[4,5,6],[7,8,9]]
a=np.array(li)
print("using list -> array",a)

# Using Linspace
#(20-10) / 6-1 -> 10/5 = 2
#(max-min) / n-1 -> space
a=np.linspace(10,20,6,).reshape(3,2)
print("linspace and convert to array",a)

#Using a range
a=np.arange(1,13).reshape(2,6)
print(a)

#Access element in numpy array using indexing
#Using negative indexing we access last element of array
b=np.array([1,2,3,4,5])
print("Access element using indexing :",b[1])
print("___________________________")

#print the numbers of array using nrgative indexing [1,2,3,4,5]
lst=np.array([1,2,3,4,5,6])
for i in range(1,len(lst)+1):
    print(lst[-i])

print("__________________________")

#Slicing is used to find or extract the subarray from the given array
#array_name(start,end,steps]
#start value by default [0] and end is [-1], steps [1]
print(lst[0:5:2])
print("__________________________")

#generate a array array 1 to 100
ar=np.arange(1,101)
print(ar[::-1])





