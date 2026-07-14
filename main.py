# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect("data.sqlite")

# Reference code provided by the lab to inspect employee data
employee_data = pd.read_sql("""SELECT * FROM employees""", conn)
print("---------------------Employee Data---------------------")
print(employee_data)
print("-------------------End Employee Data-------------------")


# STEP 2
# Select employeeNumber and lastName from all employees
df_first_five = pd.read_sql("""
    SELECT employeeNumber, lastName 
    FROM employees
""", conn)


# STEP 3
# Reverse the column selection: lastName comes before employeeNumber
df_five_reverse = pd.read_sql("""
    SELECT lastName, employeeNumber 
    FROM employees
""", conn)


# STEP 4
# Select lastName and employeeNumber, renaming employeeNumber as 'ID'
df_alias = pd.read_sql("""
    SELECT lastName, employeeNumber AS ID 
    FROM employees
""", conn)


# STEP 5
# Use a CASE statement to categorize executive roles
df_executive = pd.read_sql("""
    SELECT *,
        CASE 
            WHEN jobTitle = 'President' OR jobTitle = 'VP Sales' OR jobTitle = 'VP Marketing' THEN 'Executive'
            ELSE 'Not Executive'
        END AS role
    FROM employees
""", conn)


# STEP 6
# Calculate the length of the last name using the LENGTH() function
df_name_length = pd.read_sql("""
    SELECT LENGTH(lastName) AS name_length 
    FROM employees
""", conn)


# STEP 7
# Extract the first two characters of each job title using SUBSTR()
df_short_title = pd.read_sql("""
    SELECT SUBSTR(jobTitle, 1, 2) AS short_title 
    FROM employees
""", conn)


# Reference code provided by the lab to inspect order details data
order_details = pd.read_sql("""SELECT * FROM orderDetails;""", conn) 
print("------------------Order Details Data------------------")
print(order_details)
print("----------------End Order Details Data----------------")


# STEP 8
# Calculate the rounded total price row-by-row, then use pandas .sum()
# Note: SQLite's ROUND() handles the internal multiplication math perfectly.
df_sum_individual = pd.read_sql("""
    SELECT ROUND(priceEach * quantityOrdered) AS total_price 
    FROM orderDetails
""", conn)
sum_total_price = df_sum_individual['total_price'].sum()


# STEP 9
# Extract day, month, and year parts from the orderDate column
# SQLite stores dates as strings, so strftime formats them securely.
df_day_month_year = pd.read_sql("""
    SELECT 
        orderDate, 
        strftime('%d', orderDate) AS day, 
        strftime('%m', orderDate) AS month, 
        strftime('%Y', orderDate) AS year 
    FROM orderDetails
""", conn)


# Close the database connection safely at the end of the script
conn.close()
