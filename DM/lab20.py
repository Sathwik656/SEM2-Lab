#Create df and perform following operations:
import pandas as pd
import numpy as np
data = {
    'EmpId': [101,102,103,104,105,106,107,108],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi'],
    'Age': [25, 30, 35, 40, 45, 50, 55, 60],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR', 'Finance', 'IT', 'HR'],
    'City': ['Mysore', 'Bangalore', 'Mysore', 'Bangalore', 'Mysore', 'Bangalore', 'Mysore', 'Bangalore'],
    'Salary': [50000, 60000, 55000, 70000, 52000, 58000, 62000, 48000],
    'No.Depen': [2, 3, 1, 4, 2, 3, 1, np.nan]
}
df = pd.DataFrame(data)
print(df)

#Rename any two columns
df.rename(columns={'Name':'EmpName','Salary':'EmpSal'}, inplace=True)
print("\nAfter replacing Columns: ",df)

#Replace name of department from Finance to Accounts
df['Department'] = df['Department'].replace('Finance', 'Accounts')
print("\nAfter replacing Department: ",df)

#Sort the data frame city in Ascending order and Salary in Descending order
sorted_df = df.sort_values(by=['City', 'EmpSal'], ascending=[True, False])
print("\nSorted DataFrame:\n", sorted_df)

#Display the average and total salary grouping on department name
grouped = df.groupby('Department')['EmpSal'].agg(['mean', 'sum'])
print("\nAverage and Total Salary by Department:\n", grouped)

#Display city-wise & Department-wise max, min, avg salary
group1 = df.groupby(['City', 'Department'])['EmpSal'].agg(['max', 'min', 'mean'])
print("\nCity-wise & Department-wise Max, Min, Avg Salary:\n", group1)

#Create department groups and display the grouped data for all departments
print("\nDepartment Groups:")
for name, group in df.groupby('Department'):
    print(f"\nDepartment: {name}\n", group)

#Display the average and total salary grouping on Department name for all city except Mangalore
df_no_mng = df[df['City'] != 'Mangalore']
print("Department wise salary excluding Mangalore: ")
print(df_no_mng.groupby('Department')['EmpSal'].agg(['mean', 'sum']))

#Display the names of employees whose name contains string 'Raj'
emp_raj = df[df['EmpName'].str.contains('Raj', case=False, na=False)]
print("Employees whose name contains 'Raj':\n", emp_raj)

#Display the rows containing missing values
mis_val = df[df.isnull().any(axis=1)]
print("Rows containing missing values:\n", mis_val)

#Count of total no of duplicat and Null values in df
print("Duplicate values: ",df.duplicated().sum())
print("Null values: ",df.isnull().sum())

#Drop the columns Age and Number of Dependents
print(df.drop(columns=['Age', 'No.Depen']))