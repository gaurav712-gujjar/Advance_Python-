import pandas as pd
import numpy as np

s1=pd.Series([1,2,3,4,5,6,7,8,9,10])
print(s1[s1%2==0])
print("==================================")

#Odd number series
s2=pd.Series(np.arange(10,101))
a=s2[s2%2!=0]
print(a+5)
print("==================================")

data={
    'Name':['Akash','Naksh','Yash','Dhanjay'],
    'Age' :[21, 22, 17, 28],
    'City':['Kota','Jaipur','Dhaka','Iceland'],
    'Gender':['Male','Female','Male','Male'],
    'Math':[23,45,67,89],
    'Science':[34,56,23,67],
    'Sst':[45,65,76,34]
}
labels= ['A','B','C','D']
df=pd.DataFrame(data, index=labels)
print(df['Age'].mean())
#print(df['Age'].average())
print(df['Gender'].mode())
print(df['Age'].median())
print(df[['Name','Age']])
print("==================================")

print(df['Age'].max())
print(df['Age'].min())
print(df['Gender'].min())
print("==================================")

#For multiple column it passed it in list
print(df[['Age','Gender']])
print("==================================")

#.loc--> to access row by the help of index
#for accessing row, for integer indexing
#print(df.loc[0:2])
print("==================================")

#.iloc for accessing row and column
#for integer indexing
#print(df.iloc[0:2, 1:3])
print("==================================")

#label based indexing
print(df.loc['A'])
print(df.loc[['B'],['Age','Gender']])
print("==================================")

#operation in column
df["New"]= df["Age"]+5

#sum of the total subject
df['Total']= df['Math']+df['Science']+df['Sst']
print("==================================")

#calcuate the avg of the marks and add one new column ['Avrage']
df['Average']= (df['Total'] / 3)

def check(mark):
    if mark >= 114:
        return 'Pass'

    else:
        return 'Fail'


df['Pass/Fail']= df['Total'].map(check)
print(df)

'''def age_check(eligible):
    if eligible >= 18:
        return 'Adult'
    else:
        return 'Child'

df['Adult/Child']=df['Age'].map(age_check)
print(df)'''

#make it by lambda
df['Adult/Child'] = df['Age'].map(lambda age: 'Adult' if age >= 18 else 'Child')
print(df)





