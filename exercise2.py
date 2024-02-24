import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# File path to your CSV file
csv_file_path = 'C:/Users/Ahmed/Desktop/project/ex2.csv'

# Read the CSV file into a DataFrame
data = pd.read_csv(csv_file_path)

# Extract JobTitle, Bonus, and VacationHours columns
job_titles = data['JobTitle']
bonuses = data['Bonus']
annual_leave = data['AnnualLeave']

# Set the width of the bars
bar_width = 0.35

# Set the x locations for the groups
index = np.arange(len(job_titles))

# Create the figure and axes objects
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the bars for Bonus and Vacation Hours
bar1 = ax.bar(index, bonuses, bar_width, label='Bonus', color='skyblue')
bar2 = ax.bar(index + bar_width, annual_leave, bar_width, label='Annual Leave', color='orange')

# Add labels, title, and legend
ax.set_xlabel('Job Title')
ax.set_ylabel('Amount')
ax.set_title('Bonus and Annual Leave by Job Title')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(job_titles, rotation=45, ha='right')
ax.legend()

# Show the plot
plt.tight_layout()
plt.show()
