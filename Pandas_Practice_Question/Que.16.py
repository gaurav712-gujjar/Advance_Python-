import pandas as pd

#1. Find the average of the math score.
df=pd.read_csv("StudentsPerformance.csv")
result = df['math score'].mean()
print("average score =",result)