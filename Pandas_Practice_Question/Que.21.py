import pandas as pd


#1. Create a new column named total_score, which is the sum of math score,
#reading score, and writing score.
df=pd.read_csv("StudentsPerformance.csv")
df['total_score'] = (
    df['math score'] +
    df['reading score'] +
    df['writing score']
)

print(df.head())