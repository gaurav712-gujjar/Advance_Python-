import pandas as pd

#5. Find and display the records of students who got free/reduced lunch.
df=pd.read_csv("StudentsPerformance.csv")
result=df['lunch'] == 'free/reduced'
print(df[result])