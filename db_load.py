import sqlite3 
import pandas as pd

df = pd.read_csv('orders_clean.csv')
print(df.columns.tolist())
connection  = sqlite3.connect('orders.db')

connection.execute(""" 
CREATE TABLE IF NOT EXISTS orders(
    order_id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    product TEXT,
    quantity INTEGER,
    price REAL, 
    date TEXT
)
""")

connection.execute("DELETE FROM ORDERS")

df.to_sql("orders", connection, if_exists="append" , index=False)

connection.commit()

#confirm/preview 

preview = pd.read_sql("SELECT * FROM orders LIMIT 5", connection)
print(preview)

count = pd.read_sql("SELECT COUNT (*) AS total_rows FROM orders", connection)
print(count)

connection.close()