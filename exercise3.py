# Question3: What is the relationship between Country and Revenue?

# Importing required libraries
import pyodbc
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
# Connection details
conn = pyodbc.connect(
 r'DRIVER={ODBC Driver 17 for SQL Server};'
 r'Server=DESKTOP-AP96S8I;'
 r'DATABASE=AdventureWorks2022;'
 r'Trusted_Connection=yes;'
)

# Define the SQL query
sql_query3 = """
SELECT
    CountryRegionCode,
    ROUND((SUM(SalesLastYear)/1000000), 2) AS RevenueLastYear,
    ROUND((SUM(SalesYTD)/1000000), 2) AS RevenueYTD
FROM Sales.SalesTerritory
GROUP BY CountryRegionCode;
"""
# Execute the SQL query and store the result in a pandas DataFrame
country_revenues = pd.read_sql(sql_query3, conn).fillna('Others')
# Close the database connection
conn.close()
# print DataFrame
print(country_revenues)


# Showing data in chart format to visualise relationship
X = country_revenues['CountryRegionCode']
val1 = country_revenues['RevenueLastYear']
val2 = country_revenues['RevenueYTD']
 
X_axis = np.arange(len(X))
 
plt.bar(X_axis - 0.2, val1, 0.4, label = 'RevenueLastYear', color = 'darkturquoise')
plt.bar(X_axis + 0.2, val2, 0.4, label = 'RevenueYTD', color = 'orange')


plt.xticks(X_axis, X)
plt.xlabel('Countries')
plt.ylabel('Revenue (in millions, USD$)')
plt.title('Relationship between Country and Revenue')
plt.legend()


plt.show()
