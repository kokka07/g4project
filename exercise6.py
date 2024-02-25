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
SELECT [Name]
      ,[AnnualRevenue]
      ,[SquareFeet] AS SizeOfStores
      ,[NumberEmployees]
FROM [Sales].[vStoreWithDemographics]
'''
# Execute the SQL query and store the result in a pandas DataFrame
vStoreWithDemographics = pd.read_sql(sql_query6, conn).fillna('Others')
# Close the database connection
conn.close()
# Plotting scatter plots (Correlation between Size Of Stores & Annual Revenue, and Number Of Employee & Annual Revenue)
fig, axs = plt.subplots(1, 2, figsize=(15, 6))
# Plot Store Size vs. Annual Revenue
axs[0].scatter(vStoreWithDemographics['SizeOfStores'], vStoreWithDemographics['AnnualRevenue'], s=vStoreWithDemographics['NumberEmployees']*10, alpha=0.5)
axs[0].set_title('Store Size vs. Annual Revenue')
axs[0].set_xlabel('Size of Stores (Square Feet)')
axs[0].set_ylabel('Annual Revenue(in US$)')
axs[0].grid(True)
# Plot Number of Employees vs. Annual Revenue
axs[1].scatter(vStoreWithDemographics['NumberEmployees'], vStoreWithDemographics['AnnualRevenue'], s=vStoreWithDemographics['NumberEmployees']*10, alpha=0.5)
axs[1].set_title('Number of Employees vs. Annual Revenue')
axs[1].set_xlabel('Number of Employees')
axs[1].set_ylabel('Annual Revenue(in US$)')
axs[1].grid(True)
plt.tight_layout()
plt.show()