import pandas as pd


#2. Find the maximum and minimum values in the reading score column.
df=pd.read_csv("StudentsPerformance.csv")
max = df['reading score'].max()
min = df['reading score'].min()
print("Maximum score =",max)
print("Minimum score =",min)