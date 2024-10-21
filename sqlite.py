#import sqlite3
#
### connect to sqllite
#connection=sqlite3.connect("student.db")
#
###create a cursor object to insert record,create table
#cursor=connection.cursor()
#
### create the table
#table_info="""
#create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
#SECTION VARCHAR(25),MARKS INT)
#"""
#
#cursor.execute(table_info)
#
### Insert some more records
#cursor.execute('''Insert Into STUDENT values('Krish','Data Science','A',90)''')
#cursor.execute('''Insert Into STUDENT values('John','Data Science','B',100)''')
#cursor.execute('''Insert Into STUDENT values('Mukesh','Data Science','A',86)''')
#cursor.execute('''Insert Into STUDENT values('Jacob','DEVOPS','A',50)''')
#cursor.execute('''Insert Into STUDENT values('Dipesh','DEVOPS','A',35)''')
#
### Display all the records
#print("The inserted records are")
#data=cursor.execute('''Select * from STUDENT''')
#for row in data:
#    print(row)
#
### Commit your changes in the database
#connection.commit()
#connection.close()

import sqlite3

# Connect to SQLite database (it will create the database file if it doesn't exist)
conn = sqlite3.con
# Create Dimension Tables
# 1. Date Dimension
cursor.execute('''
    CREATE TABLE IF NOT EXISTS date_dim (
        date_id INTEGER PRIMARYnect('sales_data_warehouse.db')
cursor = conn.cursor()
 KEY,
        date TEXT,
        year INTEGER,
        quarter INTEGER,
        month INTEGER,
        day INTEGER,
        weekday TEXT
    )
''')

# 2. Product Dimension
cursor.execute('''
    CREATE TABLE IF NOT EXISTS product_dim (
        product_id INTEGER PRIMARY KEY,
        product_name TEXT,
        category TEXT,
        brand TEXT,
        price REAL
    )
''')

# 3. Store Dimension
cursor.execute('''
    CREATE TABLE IF NOT EXISTS store_dim (
        store_id INTEGER PRIMARY KEY,
        store_name TEXT,
        city TEXT,
        state TEXT,
        country TEXT,
        store_type TEXT
    )
''')

# 4. Customer Dimension
cursor.execute('''
    CREATE TABLE IF NOT EXISTS customer_dim (
        customer_id INTEGER PRIMARY KEY,
        customer_name TEXT,
        gender TEXT,
        age INTEGER,
        email TEXT,
        phone_number TEXT
    )
''')

# Create the Fact Table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales_fact (
        sales_id INTEGER PRIMARY KEY,
        date_id INTEGER,
        product_id INTEGER,
        store_id INTEGER,
        customer_id INTEGER,
        quantity_sold INTEGER,
        total_sales REAL,
        FOREIGN KEY (date_id) REFERENCES date_dim(date_id),
        FOREIGN KEY (product_id) REFERENCES product_dim(product_id),
        FOREIGN KEY (store_id) REFERENCES store_dim(store_id),
        FOREIGN KEY (customer_id) REFERENCES customer_dim(customer_id)
    )
''')

# Insert rows into date_dim table
date_dim_data = [
    (1, '2024-09-01', 2024, 3, 9, 1, 'Sunday'),
    (2, '2024-09-02', 2024, 3, 9, 2, 'Monday'),
    (3, '2024-09-03', 2024, 3, 9, 3, 'Tuesday'),
    (4, '2024-09-04', 2024, 3, 9, 4, 'Wednesday'),
    (5, '2024-09-05', 2024, 3, 9, 5, 'Thursday'),
]
cursor.executemany('''
    INSERT INTO date_dim (date_id, date, year, quarter, month, day, weekday)
    VALUES (?, ?, ?, ?, ?, ?, ?)
''', date_dim_data)

# Insert rows into product_dim table
product_dim_data = [
    (1, 'Laptop', 'Electronics', 'Dell', 800.00),
    (2, 'Smartphone', 'Electronics', 'Samsung', 500.00),
    (3, 'Headphones', 'Accessories', 'Sony', 150.00),
    (4, 'Tablet', 'Electronics', 'Apple', 600.00),
    (5, 'Smartwatch', 'Wearables', 'Fitbit', 200.00),
]
cursor.executemany('''
    INSERT INTO product_dim (product_id, product_name, category, brand, price)
    VALUES (?, ?, ?, ?, ?)
''', product_dim_data)

# Insert rows into store_dim table
store_dim_data = [
    (1, 'ElectroMart', 'New York', 'NY', 'USA', 'Retail'),
    (2, 'TechWorld', 'San Francisco', 'CA', 'USA', 'Retail'),
    (3, 'GadgetHub', 'Chicago', 'IL', 'USA', 'Retail'),
    (4, 'DigitalStore', 'Los Angeles', 'CA', 'USA', 'Retail'),
    (5, 'SmartShop', 'Miami', 'FL', 'USA', 'Retail'),
]
cursor.executemany('''
    INSERT INTO store_dim (store_id, store_name, city, state, country, store_type)
    VALUES (?, ?, ?, ?, ?, ?)
''', store_dim_data)

# Insert rows into customer_dim table
customer_dim_data = [
    (1, 'John Doe', 'Male', 30, 'johndoe@example.com', '123-456-7890'),
    (2, 'Jane Smith', 'Female', 28, 'janesmith@example.com', '234-567-8901'),
    (3, 'Robert Johnson', 'Male', 45, 'robertj@example.com', '345-678-9012'),
    (4, 'Emily Davis', 'Female', 35, 'emilyd@example.com', '456-789-0123'),
    (5, 'Michael Brown', 'Male', 40, 'michaelb@example.com', '567-890-1234'),
]
cursor.executemany('''
    INSERT INTO customer_dim (customer_id, customer_name, gender, age, email, phone_number)
    VALUES (?, ?, ?, ?, ?, ?)
''', customer_dim_data)

# Insert rows into sales_fact table
sales_fact_data = [
    (1, 1, 1, 1, 1, 2, 1600.00),  # John Doe bought 2 laptops from ElectroMart
    (2, 2, 2, 2, 2, 1, 500.00),   # Jane Smith bought 1 smartphone from TechWorld
    (3, 3, 3, 3, 3, 3, 450.00),   # Robert Johnson bought 3 headphones from GadgetHub
    (4, 4, 4, 4, 4, 1, 600.00),   # Emily Davis bought 1 tablet from DigitalStore
    (5, 5, 5, 5, 5, 2, 400.00),   # Michael Brown bought 2 smartwatches from SmartShop
]
cursor.executemany('''
    INSERT INTO sales_fact (sales_id, date_id, product_id, store_id, customer_id, quantity_sold, total_sales)
    VALUES (?, ?, ?, ?, ?, ?, ?)
''', sales_fact_data)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Sample data has been inserted successfully into the data warehouse!")




