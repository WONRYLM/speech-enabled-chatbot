import pandas as pd
# # series
# s = pd.Series([10,20,30], index = ['a','b','c'])
# s['a'],s[0]
# #print(s['a'])

# # DataFrame
# data = {'Name': ['Alice','Bob'], 'Age': [25,30]}
# df = pd.DataFrame(data)
# print(df)

# x = df['Name']
# print(x)
# y = df['Age']
# print(y)
# # Dropping columns - df.drop
# df.drop(columns='Age')
# # dropping the age column
# print('Dropping the Age column :',df)





#Assignment
# 1
print('='*40)
weekly_sales = pd.Series([150000, 120000, 95000, None, 50000], index = ['Electronics','Clothing','Groceries','Furniture','Stationery'])
print('Weekly Sales :',weekly_sales)
print('='*40)

# 2
# Sales value for groceries
groceries_sales = weekly_sales.loc['Groceries']
print(f"Sales Value for Groceries : {groceries_sales}")
print('='*40)

#Use .loc[] and .iloc[] to retrieve values for:
#Clothing (by label)
clothing_sales = weekly_sales.loc['Clothing']
print(f"Sales value for Clothing : {clothing_sales}")
print('='*40)

#The third item (by position)
third_item_sales = weekly_sales.iloc[2]
print(f"Sales value for the third item : {third_item_sales}")
print(f"(The third item by position is: {weekly_sales.index[2]})") 
print('='*40)

#no.3: Data Cleaning
#Identify any missing values using .isnull()
missing_values = weekly_sales.isnull()
print(missing_values)
print('='*40)
#Replace missing values with weekly_sales.mean()
weekly_sales.mean()
replaced_missing_values = weekly_sales.mean()
print("Replaced missing values :",replaced_missing_values)
print('='*40)

#4: Analysis
#Calculate the total sales using .sum()
total_sales = weekly_sales.sum()
print("Total Sales :",total_sales)
print('='*40)

#Calculate the average sales using .mean()
average_sales = weekly_sales.mean()
print("Average Sales :", average_sales)
print('='*40)

#Find departments with sales greater than 100,000
sales_above_100k = weekly_sales > 100000
print("Departments with sales greater than 100,000 :\n",sales_above_100k)
print('='*40)