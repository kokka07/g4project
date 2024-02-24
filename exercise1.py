import pandas as pd
import matplotlib.pyplot as plt

# File path to your CSV file
csv_file_path = 'C:/Users/Ahmed/Desktop/project/ex1.csv'

# Read the CSV file into a DataFrame
data = pd.read_csv(csv_file_path)

# Select only the 'name' and 'total sales' columns
selected_data = data[['Region', 'Total_Sales']]

# Plotting the data as a bar chart
plt.figure(figsize=(10, 6))  # Adjust figure size as needed
plt.bar(selected_data['Region'], selected_data['Total_Sales'], color='skyblue')
plt.xlabel('Region')  # Label for x-axis
plt.ylabel('Total_Sales')  # Label for y-axis
plt.title('Total Sales by Name')  # Title of the plot
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent overlapping labels
plt.show()