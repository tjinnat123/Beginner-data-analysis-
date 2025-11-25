# analyze_sales.py
# this program reads a csv sales file and calculates total and average sales
import pandas as pd # import the pandas library for data analysis 
# read the csv file
data = pd.read_csv("sales_dara.csv")
#print the first 5 rows
print( "sales data oreview:")
print(data.head())
# calculate total sales
total_sales = data["sales"].sum()
print("\ntotal sales:",total sales)
# calcukate average sales
average_sales = data["sales"].mean()
print("average sales:",average_sales)
# Add Growth column (monthly sales increase) data["Growth"] = data["Sales"].diff() 
# Difference between each month print("\nSales Data with Growth:) print (data)
