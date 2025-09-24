# Mini Project: Sales Data Analysis

# Step 1: Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load dataset (replace 'sales_data.csv' with your file)
# Example dataset columns: ['OrderID', 'Date', 'Product', 'Category','Quantity', 'Price']
data = pd.read_csv("sales_data.csv")

# Step 3: Data cleaning
# Convert Date column to datetime
data['Date'] = pd.to_datetime(data['Date'])
# Create new column for Total Sales (Quantity * Price)
data['Total_Sales'] = data['Quantity'] * data['Price']
# Check for missing values
print("Missing values:\n", data.isnull().sum())

# Step 4: Basic statistics
print("\n--- Basic Sales Insights ---")
print("Total Revenue: ", data['Total_Sales'].sum())
print("Average Order Value: ", data['Total_Sales'].mean())
print("Top Selling Product:\n",
data.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False).head(1))
print("Top Category:\n",
data.groupby('Category')['Total_Sales'].sum().sort_values(ascending=False).head(1))

# Step 5: Sales trends over time
monthly_sales=data.groupby(data['Date'].dt.to_period("M"))['Total_Sales'].sum()
plt.figure(figsize=(10,6))
monthly_sales.plot(kind='line', marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True)
plt.show()

# Step 6: Top 10 Products by Sales
top_products=data.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,6))
sns.barplot(x=top_products.values, y=top_products.index, palette="viridis")
plt.title("Top 10 Products by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Product")
plt.show()

# Step 7: Category-wise Sales
category_sales = data.groupby('Category')['Total_Sales'].sum()
plt.figure(figsize=(8,6))
category_sales.plot(kind='pie', autopct='%1.1f%%', startangle=90,
colormap='Set3')
plt.title("Sales Distribution by Category")
plt.ylabel("")
plt.show()

# Step 8: Daily sales trend (optional
daily_sales = data.groupby('Date')['Total_Sales'].sum()
plt.figure(figsize=(12,6))
daily_sales.plot(color='teal')
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.show()
print("\n--- Analysis Completed ---")