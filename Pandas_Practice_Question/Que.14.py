import pandas as pd

#4. Find and display the records of female students with a reading score greater
#than 70.
df=pd.read_csv("StudentsPerformance.csv")
a = (df['gender'] == 'female') & (df['reading score'] > 70)
print(df[a])
