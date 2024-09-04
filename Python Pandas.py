

import pandas as pd
def get_employees_df():


  return pd.read_csv(
      "https://gist.githubusercontent.com/kevin336/acbb2271e66c10a5b73aacf82"
        "ca82784/raw/e38afe62e088394d61ed30884dd50a6826eee0a8/employees.csv"
  )
def get_departments_df():
  dep_df = pd.read_csv(
      "https://gist.githubusercontent.com/kevin336/5ea0e96813aa88871c20d315b5"
        "bf445c/raw/d8fcf5c2630ba12dd8802a2cdd5480621b6a0ea6/departments.csv"
  )
  dep_df = dep_df.rename(columns={"DEPARTMENT_ID": "DEPARTMENT_IDENTIFIER"})


  return dep_df


employees = get_employees_df()
departments = get_departments_df()



employees.head()
departments.head()



# 1. Please calculate the average, median, lower and upper quartiles of an employees' salaries.
salaries = employees['SALARY']
average_salary = salaries.mean()
median_salary = salaries.median()
lower_quartile = salaries.quantile(0.25)
upper_quartile = salaries.quantile(0.75)
print(f"Average Salary: {average_salary}")
print(f"Median Salary: {median_salary}")
print(f"Lower Quartile (25th percentile): {lower_quartile}")
print(f"Upper Quartile (75th percentile): {upper_quartile}")



# 2. Please calculate the average salary per department. Please include the department name in the results.
merged_df = pd.merge(employees, departments, left_on='DEPARTMENT_ID', right_on='DEPARTMENT_IDENTIFIER')
average_salary_per_dept = merged_df.groupby('DEPARTMENT_NAME')['SALARY'].mean().reset_index()
print(average_salary_per_dept)




# 3. Please create a new column named `SALARY_CATEGORY` with value "low" when the salary is lower than average and "high" if is it higher or equal
average_salary = employees['SALARY'].mean()
employees['SALARY_CATEGORY'] = employees['SALARY'].apply(
    lambda salary: 'low' if salary < average_salary else 'high'
)
employees.head()




# 4. Please create another column named `SALARY_CATEGORY_AMONG_DEPARTMENT`
#with value &quot;low&quot; when the employee salary is lower than average in his /
#her department and &quot;high&quot; in the other case.
average_salary_per_dept = merged_df.groupby('DEPARTMENT_ID')['SALARY'].mean().reset_index()
employees = pd.merge(employees, average_salary_per_dept,on='DEPARTMENT_ID')
employees['SALARY_CATEGORY_AMONG_DEPARTMENT'] = employees.apply(
    lambda row: 'low' if row['SALARY_x'] < row['SALARY_y'] else 'high', axis=1
)
employees = employees.drop(columns=['SALARY_y'])
employees.head()




# 5. Please filter the dataframe `employees` to include only the rows
#where `DEPARTMENT_ID` equals to 20. Assign the result to new variable.
employees_dept_20 = employees[employees['DEPARTMENT_ID'] == 20]
employees_dept_20.head()


#Please increase the salary by 10% for all employees working at the
#department 20.
employees_dept_20['SALARY_x']= employees_dept_20['SALARY_x'] * 1.10
employees_dept_20.head()



# 7. Please check if any of the `PHONE_NUMBER` column values are empty.
empty_phone_numbers = employees[employees['PHONE_NUMBER'].isna()]
empty_phone_numbers.head()

