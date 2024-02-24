import pyodbc
import csv

# Establish a connection to your SQL Server database
conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=DESKTOP-AP96S8I;'
                      'Database=AdventureWorks2022;'
                      'Trusted_Connection=yes;')

# Define your SQL query
sql_query = """
SELECT  he.[JobTitle], sp.[Bonus]
       ,he.[VacationHours]*60 AS AnnualLeave
      FROM  [AdventureWorks2022].[Sales].[SalesPerson] AS sp
	  INNER JOIN [AdventureWorks2022].[HumanResources].[Employee] as he
	  ON sp.[BusinessEntityID]= he.[BusinessEntityID];
"""

# Execute the SQL query and fetch the results
cursor = conn.cursor()
cursor.execute(sql_query)
results = cursor.fetchall()

# Define the path to your CSV file
csv_file_path = 'C:/Users/Ahmed/Desktop/project/ex2.csv'

# Write the results into a CSV file
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    # Write the header
    csv_writer.writerow([column[0] for column in cursor.description])
    # Write the data
    csv_writer.writerows(results)

# Close the database connection
conn.close()