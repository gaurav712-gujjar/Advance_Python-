import pandas as pd

#7. Check for any missing values in the dataset.
df=pd.read_csv("StudentsPerformance.csv")
print(df.isna().sum())