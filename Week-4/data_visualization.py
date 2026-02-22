import pandas as pd
import matplotlib.pyplot as plt
import os

# ------------------------------
# 1. File Validation
# ------------------------------
csv_file = "weather_data.csv"

if not os.path.exists(csv_file):
    print("Error: weather_data.csv file not found in the current folder.")
    print("Please make sure weather_data.csv is placed inside the Week-4 folder.")
    exit()

# ------------------------------
# 2. Load Data
# ------------------------------
data = pd.read_csv(csv_file)

print("Dataset Loaded Successfully")
print(data.head())

# ------------------------------
# 3. Basic Cleaning & Validation
# ------------------------------
data.dropna(inplace=True)

if "Month" not in data.columns or "Temperature" not in data.columns:
    print("Error: Dataset must contain 'Month' and 'Temperature' columns.")
    exit()

# ------------------------------
# 4. Analysis
# ------------------------------
highest_month = data.loc[data["Temperature"].idxmax(), "Month"]
lowest_month = data.loc[data["Temperature"].idxmin(), "Month"]
average_temp = round(data["Temperature"].mean(), 2)

# ------------------------------
# 5. Visualization
# ------------------------------

# Line Chart - Monthly Temperature Trend
plt.figure()
plt.plot(data["Month"], data["Temperature"], marker='o')
plt.title("Monthly Temperature Trend")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.tight_layout()
plt.savefig("monthly_temperature_trend.png")
plt.show()

# Bar Chart - Temperature by Month
plt.figure()
plt.bar(data["Month"], data["Temperature"])
plt.title("Temperature by Month")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.tight_layout()
plt.savefig("temperature_bar_chart.png")
plt.show()

# Pie Chart - Temperature Distribution
plt.figure()
plt.pie(data["Temperature"], labels=data["Month"], autopct="%1.1f%%")
plt.title("Temperature Distribution by Month")
plt.tight_layout()
plt.savefig("temperature_pie_chart.png")
plt.show()

# ------------------------------
# 6. Insights
# ------------------------------
summary = f"""
Week 4 - Data Visualization Summary Report
-----------------------------------------
Highest Temperature Month : {highest_month}
Lowest Temperature Month  : {lowest_month}
Average Temperature       : {average_temp} °C
"""

print(summary)

# ------------------------------
# 7. Auto Report Generation
# ------------------------------
with open("auto_summary.txt", "w") as file:
    file.write(summary)

print("Auto summary report generated successfully: auto_summary.txt")
print("All charts saved as image files in the Week-4 folder.")
print("Week 4 task completed successfully.")