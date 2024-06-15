import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read data from CSV file into a DataFrame
df = pd.read_csv('Group1_Torres.CSV')

# Convert time columns to datetime format
df["Time start"] = pd.to_datetime(df["Time start"])
df["Time end"] = pd.to_datetime(df["Time end"])

# Calculate the time interval of orders
df["Order Time Interval"] = (df["Time start"] - df["Time start"].shift()).dt.total_seconds().div(60)

# Fill NaN values with 0 for easier handling
df["Order Time Interval"] = df["Order Time Interval"].fillna(0)

# Convert Order Time Interval to integer
df["Order Time Interval"] = df["Order Time Interval"].astype(int)

# Filter data for 11am to 12pm and 12pm to 1pm
sales_11_to_12 = df[(df["Time start"].dt.hour >= 11) & (df["Time start"].dt.hour < 12)]
sales_12_to_1 = df[(df["Time start"].dt.hour >= 12) & (df["Time start"].dt.hour < 13)]

# Sales per hour
sales_per_hour_11_to_12 = sales_11_to_12["Price"].sum()
sales_per_hour_12_to_1 = sales_12_to_1["Price"].sum()

# Total sales per hour
total_sales_per_hour = {
    'Time (H)': ['11:00:00 AM - 12:00 PM', '12:00 PM - 1:00 PM'],
    'Sales': [sales_per_hour_11_to_12, sales_per_hour_12_to_1]
}
total_sales_per_hour_df = pd.DataFrame(total_sales_per_hour)

# Quantity of products
quantity_of_products = df.groupby("Products")["Quantity"].sum()

# Product order comparison
product_order_comparison = df.groupby("Products")["Orders"].sum()

# Profit by product
profit_by_product = df.groupby("Products")["Price"].sum()

# Time Interval of Orders
order_time_intervals = df["Order Time Interval"]

# Create a figure for all graphs
plt.figure(figsize=(16, 14))

# Plotting bar graphs
plt.subplot(3, 2, 1)
sns.barplot(x='Time (H)', y='Sales', data=total_sales_per_hour_df, palette='Set2')
plt.title('Total Sales per Hour')
plt.xlabel('Time')
plt.ylabel('Sales (₱)')
for index, value in enumerate(total_sales_per_hour_df['Sales']):
    plt.text(index, value, f'₱{value}', ha='center', va='bottom')

plt.subplot(3, 2, 2)
quantity_of_products.plot(kind="bar", color='lightgreen')
plt.title("Quantity of Products")
plt.xlabel("Product")
plt.ylabel("Quantity")
plt.xticks(rotation=45)
for index, value in enumerate(quantity_of_products):
    if value != 0:  
        plt.text(index, value, str(value), ha='center', va='bottom')
    else:
        plt.text(index, -1, '', ha='center', va='bottom')  

plt.subplot(3, 2, 3)
product_order_comparison.plot(kind="bar", color='orange')
plt.title("Product Order Comparison")
plt.xlabel("Product")
plt.ylabel("Orders")
plt.xticks(rotation=45)
for index, value in enumerate(product_order_comparison):
    if value != 0:  
        plt.text(index, value, str(value), ha='center', va='bottom')
    else:
        plt.text(index, -1, '', ha='center', va='bottom')  

plt.subplot(3, 2, 4)
profit_by_product.plot(kind="bar", color='lightcoral')
plt.title("Profit by Product")
plt.xlabel("Product")
plt.ylabel("Profit (₱)")
plt.xticks(rotation=45)
for index, value in enumerate(profit_by_product):
    if value != 0:  
        plt.text(index, value, f'₱{value}', ha='center', va='bottom')
    else:
        plt.text(index, -1, '', ha='center', va='bottom')  

plt.subplot(3, 2, 5)
order_time_intervals.value_counts().sort_index().plot(kind='bar', color='lightblue')
plt.title("Order Interval")
plt.xlabel("Minute")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
for index, value in enumerate(order_time_intervals.value_counts().sort_index()):
    plt.text(index, value, str(int(value)), ha='center', va='bottom', fontsize=8)

plt.tight_layout()

# Create a separate figure for pie charts
plt.figure(figsize=(12, 10))

# Quantity of Products
plt.subplot(221)
quantity_of_products.plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title("Quantity of Products Sold")
plt.ylabel('')

# Product Order Comparison
plt.subplot(222)
product_order_comparison.plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title("Product Order Comparison")
plt.ylabel('')

# Profit by Product
plt.subplot(223)
profit_by_product.plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title("Profit by Product")
plt.ylabel('')

# Sales per Hour
plt.subplot(224)
total_sales_per_hour_df['Sales'].plot(kind='pie', labels=['11:00:00 AM - 12:00 PM', '12:00 PM - 1:00 PM'], autopct='%1.1f%%', startangle=140)
plt.title("Sales per Hour")
plt.ylabel('')  
plt.tight_layout()
plt.show()
