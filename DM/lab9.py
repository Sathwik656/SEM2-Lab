#perform all the join operations on the above two data frames. (use merge())
import pandas as pd

data1 = {
    "RollNo": [1, 2, 3],
    "Name": ["Bob", "Charlie", "David"],
    "Age": [20, 21, 22],
    "Course": ["CS", "IT", "CS"]
}
df1 = pd.DataFrame(data1)

data2 = {
    "RollNo": [4, 5, 6],
    "Name": ["Charlie", "David", "Eve"],
    "Age": [22, 23, 24],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df2 = pd.DataFrame(data2)
print(df1)
print(df2)

#Inner Join
inner_join = pd.merge(df1, df2, on="RollNo", how="inner")
print("Inner Join:\n", inner_join)

#Left Join (All records from df1)
left_join = pd.merge(df1, df2, on="RollNo", how="left")
print("Left Join:\n", left_join)

#Right join (All records from df2)
right_join = pd.merge(df1, df2, on="RollNo", how="right")
print("Right Join:\n", right_join)

#Outer join (All records from both df1 and df2)
outer_join = pd.merge(df1, df2, on="RollNo", how="outer")
print("Outer Join:\n", outer_join)