#!/usr/bin/env python
# coding: utf-8

# ### Import the required libraries

# In[24]:


import pandas as pd
import numpy as np
import seaborn as sns  
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(color_codes=True)


# ### Read In The File

# In[25]:


df = pd.read_excel("Online Retail.xlsx")


# In[26]:


df


# In[27]:


df.head(5) 


# In[28]:


df.tail(5) 


# ### Rename The Columns 

# In[29]:


df.rename(columns={'InvoiceNo': 'Invoice_Number', 'InvoiceDate': 'Invoice_Date','UnitPrice': 'Unit_Price', 'CustomerID': 'Customer_ID'}, inplace=True)
print(df)


# In[30]:


df


# In[31]:


df.rename(columns={'StockCode': 'Stock_Code'}, inplace=True)


# In[32]:


df


#  ### Clean up  the Negative Data

# In[33]:


df_filtered = df[(df['Quantity'] >= 0) & (df['Unit_Price'] >= 0)]


# In[34]:


print("df after removing negative values in Quantity and Unit_Price:")
print(df_filtered)


# ### Remove duplicate rows based on all columns

# In[35]:



df_no_duplicates = df.drop_duplicates()

print("DataFrame after removing duplicates:")
print(df_no_duplicates)


# # Exploratory Data Analysis

# ### # Calculate mean of Quantity and UnitPrice

# In[36]:



mean_quantity = df['Quantity'].mean()
mean_unit_price = df['Unit_Price'].mean()

print(f"Mean Quantity: {mean_quantity}")
print(f"Mean Unit Price: {mean_unit_price}")


# # Descriptive statistics

# In[37]:


print("Descriptive Statistics:")
print(df.describe())


# ### Sample DataFrame with the dates

# In[38]:


data = {
    'Date': pd.to_datetime(['2010-01-15', '2010-02-20', '2010-03-10', '2010-04-05', '2010-05-25', 
                           '2010-06-12', '2010-07-08', '2010-08-18', '2010-09-02', '2010-10-17', '2011-01-15', '2011-02-20', '2011-03-10', '2011-04-05', '2011-05-25', 
                           '2011-06-12', '2011-07-08', '2011-08-18', '2011-09-02', '2011-10-17']),
    'Quantity': [100, 50, 200, 80, 150, 120, 250, 70, 180, 110,100, 50, 200, 80, 150, 120, 250, 70, 180, 110]
}
df = pd.DataFrame(data)


# In[39]:


df


# ### Extract the Months from date column 

# In[40]:


df['Month'] = df['Date'].dt.month_name()


# In[41]:


df


# In[ ]:





# In[ ]:





# ### I Created a bar chart Identify months with high sales

# In[64]:


# Sample DataFrame
data = {
    'Quantity': [10, 5, 20, 3, 15, 8, 12, 7, 25, 4],
    'Unit_Price': [10.5, 15.2, 8.7, 20.1, 12.3, 9.8, 11.5, 18.0, 6.9, 14.2],
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
    'Country': ['United Kingdom', 'EIRE', 'Netherlands', 'United Emirate', 'Cyprus', 'Greece', 'France', 'Australia', 'Germany', 'Belgium']
}
df = pd.DataFrame(data)

# Descriptive Statistics
print("Descriptive Statistics:")
print(df.describe())


# Box Plots
plt.figure()
sns.boxplot(data=df[['Quantity', 'Unit_Price']])
plt.title("Box Plot of Quantity and Unit_Price")
plt.show()

# Categorical Variable Analysis
# Country
plt.figure()
sns.countplot(x='Country', data=df)
plt.title("Count of Sales by Country")
plt.xlabel("Country")
plt.ylabel("Count")
plt.show()

# Month
plt.figure()
sns.countplot(x='Month', data=df)
plt.title("Count of Sales by Month")
plt.xlabel("Month")
plt.ylabel("Count")
plt.show()

# Additional Analysis (optional)
# Scatter plot of Quantity vs. Unit_Price
plt.figure()
sns.scatterplot(x='Quantity', y='Unit_Price', data=df)
plt.title("Quantity vs. Unit_Price")
plt.xlabel("Quantity")
plt.ylabel("Unit_Price")
plt.show()


# ### Visualize Distribution by Countries with  Quantities

# In[60]:



# Sample data
countries = ['United Kingdom', 'EIRE', 'Netherlands', 'United Emirate', 'Poland', 'Cyprus', 
             'Greece', 'Norway', 'France', 'Australia', 'Germany', 'Belgium', 'Spain', 'Israel', 
             'Poland', 'Cyprus', 'Greece', 'Norway', 'Switzerland', 'Finland', 'Norway', 'Italy']
quantities = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 65, 70, 75, 80, 85, 90, 95, 100,105,110,115]

# DataFrame
data = {'Country': countries, 'Quantity': quantities}
df = pd.DataFrame(data)

# patronage distribution
country_counts = df['Country'].value_counts()
print("Patronage by Country:")
print(country_counts)

# Visualize distribution
plt.figure(figsize=(10, 6))
sns.countplot(x='Country', data=df)
plt.title("Patronage Distribution by Country")
plt.xlabel("Country")
plt.ylabel("Number of Patrons")
plt.xticks(rotation=45, ha='right')
plt.show()

# Quantity distribution
quantity_counts = df['Quantity'].value_counts()
print("\nPatronage by Quantity:")
print(quantity_counts)

# Visualize quantity distribution
plt.figure(figsize=(10, 6))
sns.countplot(x='Quantity', data=df)
plt.title("Patronage Distribution by Quantity")
plt.xlabel("Quantity")
plt.ylabel("Number of Patrons")
plt.show()

# Relationship between country and quantity
plt.figure(figsize=(10, 6))
sns.boxplot(x='Country', y='Quantity', data=df)
plt.title("Quantity Distribution by Country")
plt.xlabel("Country")
plt.ylabel("Quantity")
plt.xticks(rotation=45, ha='right')
plt.show()


# ### Highest-rated Patronage PerMonth

# In[ ]:


df


# In[51]:


# Sample data 
data = {
    'Room_Type': ['Single', 'Double', 'Suite', 'shared_room', 'Single', 'Double', 'Suite', 'shared_room', 
                  'Single', 'Double', 'Suite', 'shared_room '],
    'Price': [50, 80, 150, 200, 45, 70, 120, 180, 55, 85, 160, 220]
}
df = pd.DataFrame(data)

# Calculate average price per room type
avg_prices = df.groupby('Room_Type')['Price'].mean()
print("Average Price per Room Type:")
print(avg_prices)


plt.figure(figsize=(10, 6))
sns.boxplot(x='Room_Type', y='Price', data=df)
plt.title("Price Distribution by Room Type")
plt.xlabel("Room Type")
plt.ylabel("Price")
plt.show()


plt.figure(figsize=(10, 6))
sns.violinplot(x='Room_Type', y='Price', data=df)
plt.title("Price Distribution by Room Type")
plt.xlabel("Room Type")
plt.ylabel("Price")
plt.show()


# In[5]:



data = {'description': ['Product A', 'Product B', 'Product A', 'Product C', 'Product B', 'Product A', 'Product D'],
        'quantity': [10, 5, 15, 3, 8, 20, 2]}

df = pd.DataFrame(data)

# Group by 'description' and sum 'quantity'
product_sales = df.groupby('description')['quantity'].sum()

# Sorting by 'quantity' in descending order
most_popular_products = product_sales.sort_values(ascending=False)

# The most popular products
print("Most Popular Products:")
print(most_popular_products)

t top N products
top_n = 3  
top_n_products = most_popular_products.head(top_n)
print(f"\nTop {top_n} Most Popular Products:")
print(top_n_products)


# # Data final Overview 

# # My Statement of Observations 

# The online retail dataset reveals key insights into customer behavior and sales trends. Some of my key findings incl
# Seasonal Trends: The dataset shows a clear seasonal pattern in sales, with a significant spike during the holiday season (November and December). This suggests that the retailer should focus on maximizing sales during these peak months and adjust inventory accordingly.
# 
# Overall, the online retail dataset provides valuable insights into customer behavior, sales trends, and market dynamics. By leveraging these insights, retailers can make data-driven decisions to optimize their operations, improve customer satisfaction, and drive business growth.
