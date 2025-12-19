import pandas as pd


#2. Create a new column named average_score (total score divided by 3).
df=pd.read_csv("StudentsPerformance.csv")
df['average_score'] = (df['math score'] + df['reading score'] + df['writing score']) / 3
print(df.head())