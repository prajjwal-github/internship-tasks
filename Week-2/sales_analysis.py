import pandas as pd

# Load the dataset (CSV file should be in the same folder as this script)
df = pd.read_csv("sales_data.csv")

# Display first few rows
print("First 5 rows of the dataset:")
print(df.head(), "\n")

# Basic information about the dataset
print("Dataset Info:")
df.info()
print()

print("Shape of dataset (rows, columns):", df.shape, "\n")

# Check for missing values
print("Missing values in each column:")
print(df.isnull().sum(), "\n")

# Handle missing values
# Fill missing numeric values with 0
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
df[numeric_cols] = df[numeric_cols].fillna(0)

# Fill missing text values with 'Unknown'
text_cols = df.select_dtypes(include=["object"]).columns
df[text_cols] = df[text_cols].fillna("Unknown")

# Remove duplicate rows if any
df = df.drop_duplicates()

# Calculate metrics
total_sales = df["Total_Sales"].sum()
average_sales = df["Total_Sales"].mean()
max_sales = df["Total_Sales"].max()
min_sales = df["Total_Sales"].min()

# Best-selling product
product_sales = df.groupby("Product")["Total_Sales"].sum()
best_product = product_sales.idxmax()
best_product_sales = product_sales.max()

# Display results
print("Sales Analysis Report")
print("---------------------")
print(f"Total Sales: ₹{total_sales:,.2f}")
print(f"Average Sales: ₹{average_sales:,.2f}")
print(f"Highest Single Sale: ₹{max_sales:,.2f}")
print(f"Lowest Single Sale: ₹{min_sales:,.2f}")
print(f"Best-Selling Product: {best_product}")
print(f"Total Sales of Best-Selling Product: ₹{best_product_sales:,.2f}")

# Save report to a text file
report_text = f"""
Sales Analysis Report
---------------------
Total Sales: ₹{total_sales:,.2f}
Average Sales: ₹{average_sales:,.2f}
Highest Single Sale: ₹{max_sales:,.2f}
Lowest Single Sale: ₹{min_sales:,.2f}
Best-Selling Product: {best_product}
Total Sales of Best-Selling Product: ₹{best_product_sales:,.2f}
"""

with open("analysis_report.txt", "w", encoding="utf-8") as f:
    f.write(report_text)

print("\nReport saved as analysis_report.txt")