import pandas as pd

#4. Check the shape, size, and ndim attributes of the DataFrame.
df=pd.read_csv("StudentsPerformance.csv")
print(df.shape)
print(df.size)
print(df.ndim)