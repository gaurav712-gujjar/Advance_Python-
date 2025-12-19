import pandas as pd

#4. Find the top 5 students based on their total_score.
df=pd.read_csv("StudentsPerformance.csv")

df['total_score'] = df['math score'] + df['reading score'] + df['writing score']
top5_students=df.sort_values(by='total_score', ascending=False).head(5)

print(top5_students)