import pandas as pd


#3. Count the number of students grouped by race/ethnicity.
df=pd.read_csv("StudentsPerformance.csv")
race = df.groupby('race/ethnicity').size()
print(race)