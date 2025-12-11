import pandas as pd
import numpy as np

# Load dataset
file_path = r"C:\Users\Asus\Desktop\Data science\Online Retail.xlsx"
df = pd.read_excel(file_path)

# Show first 5 rows
print(df.head())

# Shape (rows, columns)
print("\nSHAPE:", df.shape)

# Column names
print("\nCOLUMNS:")
print(df.columns)

# Data types
print("\nDATA TYPES:")
print(df.dtypes)

# Missing values
print("\nMISSING VALUES:")
print(df.isnull().sum())

# Basic info summary
print("\nINFO:")
print(df.info())

# -----------------------------
# STEP 3: CLEAN MISSING VALUES
# -----------------------------

# Remove rows where Description is missing
df = df.dropna(subset=['Description'])

# CustomerID missing - keep them for now (useful for sales but not customer-level analysis)
# But mark how many remain
print("Remaining rows after dropping missing descriptions:", df.shape)

# -----------------------------
# STEP 4: REMOVE DUPLICATES
# -----------------------------
before = df.shape[0]
df = df.drop_duplicates()
after = df.shape[0]

print(f"Duplicates removed: {before - after}")

# -----------------------------
# STEP 5: REMOVE INVALID ROWS
# -----------------------------

# Remove rows with negative or zero quantity (these are returns)
invalid_qty = df[df['Quantity'] <= 0].shape[0]
print("Rows with invalid quantity:", invalid_qty)

df = df[df['Quantity'] > 0]

# Remove rows with zero or negative price
invalid_price = df[df['UnitPrice'] <= 0].shape[0]
print("Rows with invalid price:", invalid_price)

df = df[df['UnitPrice'] > 0]

print("Rows remaining after cleaning:", df.shape)

# -----------------------------
# STEP 7: CREATE NEW COLUMNS
# -----------------------------
# Create total price per line
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

# Create Year and Month columns and a Year-Month (period) column for grouping
df['Year'] = df['InvoiceDate'].dt.year
df['Month'] = df['InvoiceDate'].dt.month
df['InvoiceMonth'] = df['InvoiceDate'].dt.to_period('M').dt.to_timestamp()

print("\nNEW COLUMNS ADDED: TotalPrice, Year, Month, InvoiceMonth")
print(df[['InvoiceDate','InvoiceMonth','Year','Month','Quantity','UnitPrice','TotalPrice']].head())

# -----------------------------
# STEP 8: GROUP ANALYSIS
# -----------------------------
# 1) Monthly sales (total)
monthly_sales = df.groupby('InvoiceMonth')['TotalPrice'].sum().sort_index()
print("\nTOP 8 months by sales (head):")
print(monthly_sales.head(8))

# 2) Top 10 products by total sales
top_products = df.groupby('Description')['TotalPrice'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 products by sales:")
print(top_products)

# 3) Sales by country (top 10)
country_sales = df.groupby('Country')['TotalPrice'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 countries by sales:")
print(country_sales)

# 4) Number of unique customers (non-null CustomerID)
unique_customers = df['CustomerID'].nunique()
print(f"\nUnique customers (CustomerID non-null): {unique_customers}")

# -----------------------------
# STEP 9: EXPORT CLEANED DATASET
# -----------------------------
output_path = r"C:\Users\Asus\Desktop\Data science\online_retail_cleaned.csv"
df.to_csv(output_path, index=False)
print(f"\nCleaned dataset exported to: {output_path}")

# -----------------------------
# STEP 10: SHORT SUMMARY FOR CV
# -----------------------------
summary = f"""
CLEANING SUMMARY:
- Original rows: 541,909
- After dropping missing descriptions: {540455}
- After removing duplicates and invalid rows: {df.shape[0]}
- Time range: {df['InvoiceDate'].min().date()} to {df['InvoiceDate'].max().date()}
- Unique customers (non-null): {unique_customers}
- Top product by sales: '{top_products.index[0]}' with total sales {top_products.iloc[0]:.2f}
"""
print(summary)
