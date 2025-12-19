import pandas as pd

#4. Find the average writing score grouped by gender.
df=pd.read_csv("StudentsPerformance.csv")
avg_score = df.groupby('gender')['writing score'].mean()
print("average score =",avg_score)