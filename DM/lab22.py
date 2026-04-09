#Draw a bar chart for total Salary by Department
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi'],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR', 'Finance', 'IT', 'HR'],
    'Salary': [50000, 60000, 55000, 70000, 52000, 58000, 62000, 48000]
}
df = pd.DataFrame(data)
print("Employee DataFrame:\n", df)

dept_salary = df.groupby('Department')['Salary'].sum()
dept_salary.plot(kind='bar')
plt.title('Total Salary by Department')
plt.xlabel('Department')
plt.ylabel('Total Salary')
plt.show()