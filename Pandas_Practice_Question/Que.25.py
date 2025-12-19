import pandas as pd


#Find the bottom 5 students based on their math score.
df=pd.read_csv("StudentsPerformance.csv")
bottom5_math = df.sort_values(by='math score', ascending=True).head(5)
print(bottom5_math)