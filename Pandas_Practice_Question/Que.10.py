import pandas as pd

#10. Find the unique values present in the lunch column.
df=pd.read_csv("StudentsPerformance.csv")
print(df['lunch'].unique())
