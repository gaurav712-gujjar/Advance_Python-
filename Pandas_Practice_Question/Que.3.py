import pandas as pd

#3. Display the last 5 rows of the dataset.
df=pd.read_csv("StudentsPerformance.csv")
print(df.tail())