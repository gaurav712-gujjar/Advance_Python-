import pandas as pd

#3. Filter and display the students
# who completed the test preparation course.
df=pd.read_csv("StudentsPerformance.csv")
print(df[df['test preparation course']=='completed'])