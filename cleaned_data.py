#!/usr/bin/env python
# coding: utf-8

# In[1]:


# let's fisrt give you an overview of the data
# This is a bike share company's customer data
# we are gonna clean it to enhance the data quality
# And facilitate analysis


# In[2]:


# Let's import required libraries and dependecies
import pandas as pd
import numpy as np
import datetime


# In[3]:


# Now let's import the csv file that contains the data
df = pd.read_csv("data.csv")
df


# In[4]:


# Now that our primary objective is to clean and standardize the data for future analysis
# Here are few things we can do in order to clean the data
# 1) Remove duplicate values
# 2) we can standardize date format
# 3) delete unnecassary columns and rows that might play no roles in out analysis
# 4) We are gonna make sure if the columms have the correct data type or not
# 5) we are also gonna see if the data have any missing value or handle missing values
# 6) We need to rename the columns as necessary
# 7) change the data type or the format of the data where necassary for analysis
# Addional steps will be added as we go on


# In[5]:


# first of all , start with the basic , let's remove some rows with duplicate vlaues
df = df.drop_duplicates()
# did it worked
df
# it did


# In[6]:


# So no duplicates huh, let's remove rows with blanks in them shall we.
df = df.dropna()
# let's check it
df
# it too works


# In[7]:


# let's change the name of a column
df.rename(columns={"Customer_Age": "Age"}, inplace=True)
# let's check
df
# works huh


# In[8]:


# there isn't much to be desired here
# this dataset doesn't have much to do here
# soo let's move on to deleting use less columns


# In[9]:


# let's delete Day Month Year from the data set because it doesn't have much to desire
df.drop(columns=["Year", "Month", "Day"], inplace=True)
# This code snippet should take care of it.
# let's check the table if it worked
df
# it worked


# In[10]:


# now that the useless date columns are out, now let's also delete Age_Group column as we already have Age Column and category is pretty useless
df.drop(columns=["Age_Group"], inplace=True)
# Does this code work
df
# It works


# In[11]:


# Let's check data in a column , I wanna know if I should delete the column or not
df["Sub_Category"][1:88]
# let's check if all the values in this column is just mountain bikes.
for index, value in df["Sub_Category"].items():
    if value != "Mountain Bikes":
        print("Here is one")

# so this column has no other value other than Mountain Bikes
# so this column is particularly useless
df.drop(columns=["Sub_Category"], inplace=True)
# Let's check this out if the code worked
df


# In[12]:


# Why I did this is the that column was completly useless as it holds the same value, provides no explorative value
# As is the case with Sales_Order
df.drop(columns=["Sales_Order #"], inplace=True)
# this column as no value in our analysis so it's best to delete them
df
# it worked


# In[13]:


print(df.dtypes)


# In[14]:


# the product_category is also not particularly useful as it serves no purpose on our analysis
# so let's delete it completely
df.drop(columns=("Product_Category"), inplace=True)
# let's see if it worked
df


# In[15]:


# Now let's change the data type in all the columns that are objects to strings so that we can perform necassary analysis and remove the $ sings in all the columns.
# df['Unit_Cost'] = df['Cost'].astype(str)        # This code should do it
# let's check
# df

# I tried many different ways to do this and I think the main problem is in column name itself, let's see all the columns name
print(df.columns)


# In[16]:


# Let's see if it works, now it must work as we know how the columns are named.
df.rename(columns={" Unit_Cost ": "uc"}, inplace=True)
# let's see if it worked
df


# In[17]:


# okay now that it worked let's change the names of other columns too
df.rename(columns={" Unit_Price ": "up"}, inplace=True)
df.rename(columns={" Profit ": "profit"}, inplace=True)
df.rename(columns={" Cost ": "cost"}, inplace=True)
df.rename(columns={"Revenue": "revenue"}, inplace=True)
# These code should change the name of the columns as well as delete white spaces between then as well soo it should be perfect for our analysis
# let's check it out
df


# In[18]:


# As all of the columns about income and expenditures , they are all object data type and also they have '$' , let's first clear the '$' sign
# instead of repeating the same code again and again , we can first create a list with the names of the columns
columns = ["uc", "up", "profit", "cost", "revenue"]
# Now that we have a list with columns names.
# Let's run a loop to remove $ from the columns where necassary
for col in columns:
    df[col] = df[col].str.replace("$", "")
# let's see if hte loop worked
df


# In[19]:


# All the columns holding financial data have a object data type, maybe we should convert them first to int.
# as we already have the list that contains the name of the columns maybe we just use that.
# we should use Columns list to change the data types.
# df[columns] = df[columns].astype(int)  # this code chunck should change the data stype of all the columns to int.
# let's see if it works.
# print(df.dtypes)

# so it doesn't work like this as these column values has ',' where necessary , so maybe we need to take of that. soo a loop that will first remove comma
# second to changethe data types.
for col in columns:
    df[col] = df[col].str.replace(",", "").str.strip()  # Remove commas and whitespace
    df[col] = pd.to_numeric(df[col], errors="coerce")  # Convert to data type to int
# let's check if the loop worked
print(df.dtypes)


# In[20]:


# Looks like it worked. Okay now that basic data cleaning is done. Let's move on to creating other columns where necassary
# let's have a look at the data once
df


# let's create a new column to see how much comtribution margin the company makes after selling each product
df["Contribution_margin"] = ((df["up"] - df["uc"]) / df["up"]) * 100
# Let's see if it worked
df



# Now that we have contribution margin let's see how much profit did the company make per item. Before factoring in the
# We are gonna subract the individual cost with individual selling price to figure out the profit per item
df["profit_per_item"] = df["up"] - df["uc"]  # This code should do it
# let's check it out if it worked or not
df




# now let's see the final proft , for that we need to subtract the cost from revuenue and we will get final profit , As there ar no corperate taxes
# for companies with revenue below $10,000 a year in australia. So, no need to factor in the taxes
# let's find final profit
df["final_profit"] = (
    df["revenue"] - df["cost"]
)  # this will subtract cost from revenue and add it in final_profit
# let's see if it worked
df



# Now the final item we need for our analysis , we need to create a column for profit margin
df["profit_margin"] = (
    df["final_profit"] / df["revenue"]
) * 100  # this code should get final profit percentage from revenue and change it to percentage.
# let's see if it works
df



# Now that we are done with data cleanign and making data ready for analysis
# we can sincerly move on to analysis
# I am gonna upload this up to github repo now, then I will update it later with the code of explorative analysis later.
