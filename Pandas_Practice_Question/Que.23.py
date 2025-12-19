import pandas as pd

#3. Add a column named result. A student passes if their average_score is 60 or
#above; otherwise, they fail. (Hint: Use a conditional function or lambda expression).
df=pd.read_csv("StudentsPerformance.csv")
df['average_score'] = (df['math score'] + df['reading score'] + df['writing score']) / 3
df['result'] = df['average_score'].apply(lambda x: 'Pass' if x >= 60 else 'Fail')
print(df.head())
