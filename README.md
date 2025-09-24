# SALES-DATA-ANALYSIS-USING-PYTHON
This mini-project analyzes sales data to uncover trends and insights using Pandas, Matplotlib, and Seaborn. It includes data cleaning, statistical summaries, and visualizations for better business understanding.

Step 1: Import Libraries
Imports essential Python libraries for data handling (pandas) and visualization (matplotlib, seaborn).

Step 2: Load Dataset
Reads the sales data from a CSV file (sales_data.csv) into a DataFrame.
Example columns: OrderID, Date, Product, Category, Quantity, Price.

Step 3: Data Cleaning
Converts the Date column to datetime format.
Creates a new column Total_Sales by multiplying Quantity * Price.
Checks for missing values in the dataset.

Step 4: Basic Sales Statistics
Calculates total revenue and average order value.
Identifies the top-selling product and best-performing category based on total sales.

Step 5: Monthly Sales Trend
Aggregates total sales by month.
Plots a line graph to show sales trends over time.

Step 6: Top 10 Products by Sales
Finds the top 10 products with the highest sales.
Visualizes them using a horizontal bar plot.

Step 7: Category-wise Sales Distribution
Groups data by product categories.
Shows category sales as a pie chart to visualize their share of total revenue.

Step 8: Daily Sales Trend (Optional)
Aggregates and plots total sales per day to identify daily fluctuations or patterns.

Final Output:
Displays plots and print statements to give meaningful insights into:
Revenue patterns

Product/category performance

Time-based trends
