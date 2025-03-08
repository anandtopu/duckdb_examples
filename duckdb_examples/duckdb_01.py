import duckdb

# Create an in-memory database (or use a file for persistence)
conn = duckdb.connect(database=':memory:')  # Use ':memory:' for in-memory or 'my_database.db' for a file

# Create a table
conn.execute("CREATE TABLE employees (id INTEGER, name VARCHAR, salary INTEGER)")

# Insert data into the table
conn.execute("INSERT INTO employees VALUES (1, 'Alice', 50000), (2, 'Bob', 60000), (3, 'Charlie', 70000)")

# Query the table
result = conn.execute("SELECT * FROM employees").fetchall()
print("All Employees:")
for row in result:
    print(row)

# Query with a condition
result = conn.execute("SELECT name, salary FROM employees WHERE salary > 55000").fetchall()
print("\nEmployees with salary > 55000:")
for row in result:
    print(row)

# Load data from a CSV file
conn.execute("CREATE TABLE sales AS SELECT * FROM read_csv_auto('sales_data.csv')")

# Query the CSV data
result = conn.execute("SELECT * FROM sales WHERE amount > 1000").fetchall()
print("\nSales with amount > 1000:")
for row in result:
    print(row)

# Export query results to a CSV file
conn.execute("COPY (SELECT * FROM employees) TO 'employees_export.csv' (HEADER, DELIMITER ',')")

# Close the connection
conn.close()