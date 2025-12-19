import pandas as pd


#2. Find and display the records of students who scored less than 50 in writing
#score.
df= pd.read_csv("StudentsPerformance.csv")
print(df[(df['writing score']<50)])