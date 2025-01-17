import pandas as pd

# Load the CSV files from the data folder
file1 = pd.read_csv('data/daily_sales_data_0.csv')
file2 = pd.read_csv('data/daily_sales_data_1.csv')
file3 = pd.read_csv('data/daily_sales_data_2.csv')

# Combine the data into a single DataFrame
data = pd.concat([file1, file2, file3])

# Filter for only Pink Morsels
pink_morsels = data[data['product'] == 'Pink Morsels']

# Create the 'sales' column by multiplying 'quantity' and 'price'
pink_morsels['sales'] = pink_morsels['quantity'] * pink_morsels['price']

# Select the required columns: 'sales', 'date', and 'region'
output_data = pink_morsels[['sales', 'date', 'region']]

# Save the result to a new CSV file
output_data.to_csv('processed_sales_data.csv', index=False)

print("Data processing complete. The output is saved as 'processed_sales_data.csv'.")

