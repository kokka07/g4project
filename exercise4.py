import pandas as pd
import pyodbc
import numpy as np
import matplotlib.pyplot as plt
# Create a cursor to execute SQL queries
# Establish a connection to your SQL Server database
conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=DESKTOP-AP96S8I;'
                      'Database=AdventureWorks2022;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()
# Define your SQL query
sql_query6 = '''
SELECT OrganizationLevel, AVG(SickLeaveHours) AS AvgSickLeaveHours
FROM humanResources.Employee
WHERE SickLeaveHours > 0
GROUP BY OrganizationLevel
ORDER BY AvgSickLeaveHours DESC;
'''
# Execute the query and load data into a Pandas DataFrame
df = pd.read_sql_query(sql_query6, conn)
# Close the database connection
conn.close()
# Display the DataFrame
print(df)
plt.figure(figsize=(10, 6))
plt.bar(df['OrganizationLevel'], df['AvgSickLeaveHours'], color='skyblue')
plt.xlabel('Organization Level')
plt.ylabel('Sick Leave Hours')
plt.title('Sick Leave Hours by Organization Level')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
# Show the plot
plt.show()