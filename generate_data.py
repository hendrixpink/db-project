import csv 
import random as rd 

first_names = ["Anna", "Mihai", "Elena", "Cristian", "Ioana", "Andrei", "Maria", "Victor"]
last_names = ["Popescu", "Ionescu", "Rusu", "Stan", "Munteanu", "Cojocaru"]
products = ["Wireless Mouse", "USB-C Cable", "Notebook", "Desk Lamp", "Headphones", "Water Bottle"]

# Generate a clean row of data
def generate_clean_row(order_id):
    first = rd.choice(first_names)
    last = rd.choice(last_names)
    name = f"{first} {last}"
    email = f"{first.lower()}.{last.lower()}@example.com"
    product = rd.choice(products)
    quantity = rd.randint(1, 5)
    price = round(rd.uniform(10, 100), 2)
    date = f"2026-0{rd.randint(1, 9)}-{rd.randint(10, 28)}"
    return [order_id, name, email, product, quantity, price, date]

def bubblesort(mylist):
    n = len(mylist)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if mylist[j] > mylist[j+1]:
                mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
                swapped = True
        if not swapped:
            break

rows = []

for i in range (1, 100): 
    row = generate_clean_row(i)
    rows.append(row)

# Duplicate some rows to simulate dirty data
for _ in range(5):
    duplicate = rd.choice(rows)
    rows.append(duplicate)

# Mess up formating or leave gaps on 8 random rows

for _ in range(8): 
    row = rd.choice(rows)
    problem = rd.choice(['blank_email', 'extra_spaces', 'wrong_date', 'wrong_quantity'])
    if problem == 'blank_email':
        row[2] = ''
    elif problem == 'extra_spaces':
        row[1] = ' ' + row[1].upper() + ' '
    elif problem == 'wrong_date': 
        # row[6] = row[6].replace("-" , ".")
        row[6] = ' asfjfkasj '
    elif problem == 'wrong_quantity':
        row[4] = -1

header = ['order_id', 'name', 'email', 'product', 'quantity', 'price', 'date']

bubblesort(rows)

with open("order_messy.csv", 'w', newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for i in range(len(rows)):
        writer.writerow(rows[i])

print(f"Generated {len(rows)} rows in order_messy.csv")
