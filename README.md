# Order Data Cleaning & Automation Pipeline

## What this does
Simulates a common workflow problem: messy order data (duplicates, missing
values, inconsistent formatting) gets cleaned, loaded into a SQL database,
and turned into a short summary report — all automatically.

## Why I built this
To practice python skills and work with data cleaning and automating processes 
related to data tables and databases. 
Learn new libraries such as pandas, csv, etc. 
## How it works
1. `generate_data.py` — creates a sample dataset of orders, deliberately
   including duplicates, blank fields, inconsistent dates, and invalid values
2. `clean_data.py` — loads the data with pandas, removes duplicates, fixes
   formatting, validates values, and reports what was fixed
3. `db_load.py` — loads the cleaned data into a SQLite database (`orders.db`)
4. `report.py` — queries the database and writes a summary to
   `summary_report.txt`

## How to run it

python generate_data.py
python clean_data.py
db_load.py
report.py

## Tech used
Python, pandas, SQLite

## Example output
=== Orders Summary Report ===

Total orders: 99
Total revenue: $16970.69

Top products by quantity sold:
       product  total_quantity
     Desk Lamp              62
Wireless Mouse              57
    Headphones              57

Orders by month:
  month  num_orders
    NaN           2
2026-01           8
2026-02          10
2026-03          17
