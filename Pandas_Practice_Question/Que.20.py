import pandas as pd

#Sort the students by
# math score in descending order and display the top 10.
df=pd.read_csv("StudentsPerformance.csv")
top_10 = df.sort_values('math score', ascending=False).head()
print(top_10)