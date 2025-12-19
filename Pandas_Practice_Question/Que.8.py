import pandas as pd

#8. Select and display only the math score and reading score columns.
df=pd.read_csv("StudentsPerformance.csv")
print(df['math score'],['reading score'])
