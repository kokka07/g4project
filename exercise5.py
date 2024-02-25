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
SELECT [AnnualRevenue], [YearOpened]
FROM [AdventureWorks2022].[Sales].[vStoreWithDemographics]
ORDER BY [YearOpened];
'''
# Execute the SQL query
cursor.execute(sql_query6)
# Fetch all rows from the result set
rows = cursor.fetchall()
# Display the fetched data
# for row in rows:
#     print(row)
# Close cursor and connection
cursor.close()
# Execute the SQL query and store the result in a pandas DataFrame
df = pd.read_sql(sql_query6, conn).fillna('Others')
# Close the database connection
conn.close()
# print DataFrame
print(df)
# Bar chart
plt.bar(df['YearOpened'], df['AnnualRevenue'])
plt.title('Bar Chart of Annual Revenue vs. Year Opened')
plt.xlabel('Year Opened')
plt.ylabel('Annual Revenue')
plt.show()
# # Plotting scatter plot (Correlation between Size Of Stores & Annual Revenue)
# plt.figure(figsize=(10, 6))
# plt.scatter(df['YearOpened'], df['AnnualRevenue'], alpha=0.5)
# plt.title('YearOpened vs. Annual Revenue')
# plt.xlabel('YearOpened')
# plt.ylabel('Annual Revenue')
# plt.grid(True)
# plt.legend()
# plt.show()
# conn.close()
conn.close()
# conn.close()