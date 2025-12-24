import numpy as np
import pandas as pd

df=pd.read_csv("Heart_Disease_Prediction.csv")
print(df.head())
print(df.tail())
print(df.columns)
print("=============================================")

print(df['Age'])

#(.astype) is use to covert datatype of the column
print(df["Age"].astype("float"))
df["Age"]=df["Age"].astype("float")
print(df["Age"].dtype)
print("=============================================")

#To add column at the end
df["Age_int"]=df["Age"].astype("int")
print(df.head())

print("=============================================")
print(df["FBS over 120"].value_counts())

print("=============================================")
#Identify the numerical columns and categorical column
print(df.info())

#categorical data
cat=df.select_dtypes(include="object").columns

#Numereical columns
num=df.select_dtypes(exclude="number").columns
print("=============================================")

print(df.describe())
