import pandas as pd
#1: Create the DataFrame
#Create a DataFrame named employees 
print('='*40)
data = {'Name':['Alice','Brian','Cynthia','David','Esther'],
        'Age':[29,35,42,28,None],
        'Department':['HR','IT','Finance','Marketing','IT'],
        'Salary':[50000,70000,82000,None,68000],
        'Performance':['Good','Excellent','Fair','Excellent','Good']}
employees = pd.DataFrame(data)
print(employees)
print('='*40)

#2: Data Exploration
#View the first 3 rows using .head()
print('First Three Rows : ',employees.head(3)) # View the first 3 rows of the DataFrame
print('='*40)

#Use .info() and .describe() to understand the structure
print('Understanding The Structure')
print(employees.info()) # Shows Datatypes and Missing values
print(employees.describe()) # Provides Numerical Summaries
print('='*40)

#Count the number of unique departments
print('Number of Unique Departments : ',employees['Department'].nunique())
print('='*40)

#3: Data Cleaning
#Fill missing Age and Salary with the column mean
print('Filling Missing Age With Mean :\n ',employees['Age'].fillna(employees['Age'].mean))
print('Filling Missing Salary With Mean :\n ',employees['Salary'].fillna(employees['Salary'].mean))
print('='*40)

#Rename the column "Performance" to "Rating"
print('Renaming Performance to Rating : \n ')
employees = employees.rename(columns = {'Performance':'Rating'})
print('='*40)

#Remove duplicate rows (add one duplicate row intentionally to try it)
employees.loc[len(employees)] = employees.loc[0]
employees = pd.concat([employees,employees.iloc[[0]]])
print('Before Dropping Duplicates : \n',employees)
print('*'*20)
y = employees.drop_duplicates()
print('After Dropping Duplicates :\n ',y)
print('='*40)

#4: Filtering and Analysis
#Show all employees in the IT department
it_employees = y.loc[y['Department']=='IT']
print('Employees in IT Department :\n',it_employees)
print('='*40)

#Display employees with a salary > 60,000
salary_above_60K = y.loc[y['Salary']>60000]
print('Employees with a salary > 60,000\n',salary_above_60K)
print('='*40)

#Count how many employees have "Excellent" rating
excellent_rating = len(y.loc[y['Rating']=='Excellent'])
print('Number of Employees with Excellent Rating :',excellent_rating)
print('='*40)

#Discussion Prompts
#What are the risks of missing data? How did you handle it?


#Why would you choose to use a DataFrame here instead of individual Series?


#What insights can be drawn from this dataset?



# # DataFrame
# data = {'Name': ['Alice','Bob'], 'Age': [25,30]}
# df = pd.DataFrame(data)
# print(df)

# x = df['Name']
# print(x)
# y = df['Age']
# print(y)