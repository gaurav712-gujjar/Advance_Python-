import pandas as pd

#1. Find and display the records of students who scored more than 80 in math score.
df=pd.read_csv("StudentsPerformance.csv")
print(df[(df['math score']>80)])
