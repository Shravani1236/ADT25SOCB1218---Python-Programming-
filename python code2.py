import pandas as pd
import matplotlib.pyplot as plt

# Read employee CSV file
df = pd.read_csv("employee.csv")

# Display employee details
print("Employee Details:")
print(df[['Name', 'Department', 'Salary']])

# Calculate average salary department-wise
avg_salary = df.groupby('Department')['Salary'].mean()

# Display average salary
print("\nAverage Salary of Each Department:")
print(avg_salary)