import pandas as pd

#9. Find the number of male and female students (count of each gender).
df=pd.read_csv("StudentsPerformance.csv")
print(df['gender'].value_counts())