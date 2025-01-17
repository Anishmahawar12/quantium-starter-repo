import pandas as pd

# Load the CSV files from the data folder
file1 = pd.read_csv('data/daily_sales_data_0.csv')
file2 = pd.read_csv('data/daily_sales_data_1.csv')
file3 = pd.read_csv('data/daily_sales_data_2.csv')

# Inspect the first few rows of each file
print("File 1 Data:")
print(file1.head())

print("\nFile 2 Data:")
print(file2.head())

print("\nFile 3 Data:")
print(file3.head())

# Inspect column names and data types
print("\nFile 1 Info:")
print(file1.info())

print("\nFile 2 Info:")
print(file2.info())

print("\nFile 3 Info:")
print(file3.info())

