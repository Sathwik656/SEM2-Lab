#Remove outliers from salary column and darw boxplot before and after removing outliers
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi'],
    'Salary': [50000, 60000, 55000, 10000000, 52000, 58000, 62000, 48000]
}
df = pd.DataFrame(data)
print(df)

#Boxplot before removing outliers
plt.figure()
plt.boxplot(df['Salary'])
plt.title('Boxplot of Salary (Before Removing Outliers)')
plt.ylabel('Salary')
plt.show()

#Detect outliers using IQR
Q1 = df['Salary'].quantile(0.25)
Q3 = df['Salary'].quantile(0.75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

#Remove outliers
dfNew = df[(df['Salary']>=lower_limit) & (df['Salary']<=upper_limit)]
print("\nDataFrame after removing outliers:\n", dfNew)

plt.figure()
plt.boxplot(dfNew['Salary'])
plt.title('Boxplot of Salary (After Removing Outliers)')
plt.ylabel('Salary')
plt.show()