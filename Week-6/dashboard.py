import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import os

# Create visualizations folder
os.makedirs("visualizations", exist_ok=True)

# Load data
df = pd.read_csv("sales_data.csv")

# Basic preprocessing
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Set seaborn theme
sns.set_theme(style="whitegrid", palette="viridis")

# -----------------------------
# 1. Box Plot – Price Distribution by Product
# -----------------------------
plt.figure(figsize=(8, 5))
sns.boxplot(x="Product", y="Price", data=df)
plt.title("Price Distribution by Product")
plt.tight_layout()
plt.savefig("visualizations/boxplot.png")
plt.close()

# -----------------------------
# 2. Violin Plot – Sales Distribution by Region
# -----------------------------
plt.figure(figsize=(8, 5))
sns.violinplot(x="Region", y="Total_Sales", data=df)
plt.title("Sales Distribution by Region")
plt.tight_layout()
plt.savefig("visualizations/violinplot.png")
plt.close()

# -----------------------------
# 3. Heatmap – Correlation Matrix
# -----------------------------
plt.figure(figsize=(8, 6))
corr = df[["Quantity", "Price", "Total_Sales"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("visualizations/heatmap.png")
plt.close()

# -----------------------------
# 4. Subplots – 2x2 Dashboard (Seaborn + Matplotlib)
# -----------------------------
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

sns.boxplot(x="Product", y="Price", data=df, ax=axes[0, 0])
axes[0, 0].set_title("Boxplot: Price by Product")

sns.violinplot(x="Region", y="Total_Sales", data=df, ax=axes[0, 1])
axes[0, 1].set_title("Violin: Sales by Region")

monthly = df.groupby(df["Date"].dt.month)["Total_Sales"].sum()
monthly.plot(kind="line", ax=axes[1, 0], title="Monthly Sales Trend")

sns.barplot(x="Product", y="Total_Sales", data=df, ax=axes[1, 1])
axes[1, 1].set_title("Total Sales by Product")

plt.tight_layout()
plt.savefig("visualizations/subplots.png")
plt.close()

# -----------------------------
# 5. Interactive Plot – Plotly
# -----------------------------
fig = px.line(df, x="Date", y="Total_Sales", color="Product",
              title="Interactive Sales Trend by Product")
fig.write_html("visualizations/interactive.html")

print("Dashboard generated successfully!")
print("All visualizations saved in 'visualizations/' folder.")