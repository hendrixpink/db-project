import pandas as pd
# establish the data frame ( open the file and reads it )
df = pd.read_csv("order_messy.csv")

# print("Shape before cleaning", df.shape) # how many rows and columns 
# print(df.head(10)) #shows first 10 lines
# print(df.dtypes)

before = len(df)
df = df.drop_duplicates()
after = len(df)

# print(f"Removed {before - after} duplicates")

df['name'] = df['name'].str.strip().str.title()

df['date'] = df['date'].str.replace('.', '-')
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d', errors='coerce')

missing_email = (df['email'].isna()) | (df['email'].str.strip() == '')
missing_date = df['date'].isna()

# print(f"Rows with missing emails: {missing_date.sum()}")
# print(f"Rows with missing dates: {missing_date.sum()}")

df['email'] = df['email'].fillna('unknown email')
df['date'] = df['date'].fillna('unknowwn date')

# validating quantity

invalid_quantity = df['quantity'] <= 0 
# print(f"Rows with invalid quantity: {invalid_quantity.sum()}")

df.loc[invalid_quantity, 'quantity'] = 1

# manifesting

df.to_csv("orders_clean.csv", index=False)

print("\n--- Summary ---")
print(f"Original rows: {before}")
print(f"After removing duplicates: {after}")
print(f"Emails missing: {missing_email.sum()}")
print(f"Dates that failed to parse: {missing_date.sum()}")
print(f"Quantities corrected: {invalid_quantity.sum()}")
print("Saved cleaned data to orders_clean.csv")
