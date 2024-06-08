


import pandas as pd 
import numpy as np 
from tabulate import tabulate


df = pd.read_csv('data.csv')




df.head()




#let's see some basic descriptions for the data 
df.describe()




#Let's see the name of the columns in the dataframe 
print(df.columns)




#Let's see the some more basic info of the dataset
df.info()




#Now let's also see the data types of each columns 
df.dtypes




#First let's clear unnecassary columns that aren't necassary. 
df.drop(columns=['Sales_Order #', 'Day', 'Month', 'Year', 'Customer_Age'], inplace=True)
df.head()




#Now that the product_category , Sub_category , Product_description seems to have the same data so we can remove that also 
df.drop(columns=['Product_Category', 'Sub_Category', 'Product_Description'], inplace=True)
df.head()




#Now that we have deleted all the unecassary data give , let's see how many null values are there in each columns 
# Calculate the percentage of null values in each column
null_percentages = (df.isnull().sum() / len(df)) * 100
null_percentages = round(null_percentages, 2)

# Print the percentage of null values for each column
for column, percentage in null_percentages.items():
    print(f"Percentage of null values in {column}: {percentage}%")    




#Now that that's done we can move on to important stuff 
#First let's remove the dollar sign from the Unit_Cost , Unit_price , Profit, Cost , Revenue columns 
# Remove the dollar sign '$' from the columns
for col in [' Unit_Cost ', ' Unit_Price ', ' Profit ', ' Cost ', 'Revenue']:
    df[col] = df[col].astype(str).str.replace('$', '', regex=False)

df.head()




#Now that we have successfully removed the dollarsign from the data, let's also clear the ',' from the data from same columns 
for col in [' Unit_Cost ', ' Unit_Price ', ' Profit ', ' Cost ', 'Revenue']:
    df[col] = df[col].astype(str).str.replace(',', '', regex=False)
df.head()




#Now now that I think basic data cleanign is done , let's create some columns That will better help us understanding the data 
#Frist let's create a new column that holds the data for profit per unit, for that we need to subtract Unit_Cost from Unit_price columns 
#Before that I need to convert the columns to numeric data types 
df[' Unit_Cost '] = pd.to_numeric(df[' Unit_Cost '])
df[' Unit_Price '] = pd.to_numeric(df[' Unit_Price '])

#Now we can create a new column 
df['Profit_Per_Unit'] = df[' Unit_Price '] - df[' Unit_Cost ']

df.head()




#Now that we can find out what percentage of revenue is profit and what percentage of revenue is cost , usign this we can get profir margin
# First we need to change profit and Revenue columns to numeric 
#Also remove leading and trailing spaces in the name of the columns 

# Remove leading and trailing spaces from column names
df.columns = df.columns.str.strip()

# Convert 'Profit' and 'Revenue' columns to numeric
df['Profit'] = pd.to_numeric(df['Profit'])
df['Revenue'] = pd.to_numeric(df['Revenue'])

# Create the 'Profit_Margin' column
df['Profit_Margin'] = (df['Profit'] / df['Revenue']) * 100

# Round the 'Profit_Margin' to 2 decimal places
df['Profit_Margin'] = round(df['Profit_Margin'], 2)

# Display the first few rows of the dataframe
df.head()




# Define bins and labels for `Order_Quantity`
bins = [0, 2, 5, float('inf')]
labels = ['1-2', '3-5', '6+']

# Create `Order_Quantity_Group` column by binning `Order_Quantity`
df['Order_Quantity'] = pd.cut(df['Order_Quantity'], bins=bins, labels=labels, right=False)

# Print the first 5 rows
print(df.head().to_markdown(index=False, numalign="left", stralign="left"))




#Now let's write code to create a new dataframe that holds the data of agegroup segmentation nad it's count 
age_group_counts = df['Age_Group'].value_counts().reset_index()

# Rename the columns
age_group_counts.columns = ['Age_Group', 'Count']

# Save the result in the segmentation DataFrame
segmentation = age_group_counts
segmentation 






