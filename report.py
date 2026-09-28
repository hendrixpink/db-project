import sqlite3
import pandas as pd

connections = sqlite3.connect("orders.db")
# calculates revenue
total_rev = pd.read_sql(""" 
SELECT COUNT (*) AS total_orders , ROUND(SUM(quantity * price), 2) AS total_revenue FROM orders
""", connections)
#the top 5 products
top_products = pd.read_sql("""
    SELECT product, SUM(quantity) AS total_quantity
    FROM orders
    GROUP BY product
    ORDER BY total_quantity DESC
    LIMIT 5
""", connections)

orders_by_month = pd.read_sql("""
    SELECT strftime('%Y-%m', date) AS month, COUNT(*) AS num_orders
    FROM orders
    GROUP BY month
    ORDER BY month
""", connections )

with open("summary_report.txt", "w") as f:
    f.write("=== Orders Summary Report ===\n\n")
    f.write(f"Total orders: {total_rev['total_orders'][0]}\n")
    f.write(f"Total revenue: ${total_rev['total_revenue'][0]}\n\n")
    f.write("Top products by quantity sold:\n")
    f.write(top_products.to_string(index=False))
    f.write("\n\nOrders by month:\n")
    f.write(orders_by_month.to_string(index=False))

print("Saved summary_report.txt")
print(orders_by_month)
print(total_rev)
print(top_products)

connections.close()

