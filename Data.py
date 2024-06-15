import pandas as pd

# Create a list of data
data = [
    ["11:00:00 AM", "11:07:00 AM", 7, 1, "Cheese Burger", 4, 2, 100],
    ["11:07:00 AM", "11:09:00 AM", 2, 2, "Cheese Burger", 2, 1, 50],
    ["11:09:00 AM", "11:11:00 AM", 2, 3, "Cheese Burger", 2, 1, 50],
    ["11:11:00 AM", "11:18:00 AM", 7, 4, "Hamburger", 6, 3, 120],
    ["11:18:00 AM", "11:24:00 AM", 6, 5, "Cheese Burger", 8, 4, 200],
    ["11:24:00 AM", "11:30:00 AM", 6, 6, "Hotdog Sandwich", 4, 2, 80],
    ["11:30:00 AM", "11:36:00 AM", 6, 7, "Cheese Burger", 2, 1, 50],
    ["11:36:00 AM", "11:43:00 AM", 7, 8, "Cheese Burger", 12, 6, 300],
    ["11:43:00 AM", "11:58:00 AM", 15, 9, "Hotdog Sandwich", 8, 4, 160],
    ["11:58:00 AM", "11:59:00 AM", 1, 10, "Cheese Burger", 6, 3, 150],
    ["11:59:00 AM", "12:01:00 PM", 2, 11, "Coñotics Ham and Cheese", 1, 1, 45],
    ["12:01:00 PM", "12:02:00 PM", 1, 12, "Cheese Burger", 8, 4, 200],
    ["12:02:00 PM", "12:03:00 PM", 1, 13, "Hamburger", 4, 2, 80],
    ["12:03:00 PM", "12:04:00 PM", 1, 14, "Cheese Burger", 4, 2, 100],
    ["12:04:00 PM", "12:09:00 PM", 5, 15, "Yakuza Teriyaki", 2, 2, 39],
    ["12:09:00 PM", "12:09:00 PM", 0, 16, "Cheese Burger", 2, 1, 50],
    ["12:09:00 PM", "12:11:00 PM", 2, 17, "Tiger Burger", 2, 2, 108],
    ["12:11:00 PM", "12:15:00 PM", 4, 18, "Cheese Burger", 2, 1, 50],
    ["12:15:00 PM", "12:18:00 PM", 3, 19, "Cheese Burger", 2, 1, 50],
    ["12:18:00 PM", "12:21:00 PM", 3, 20, "Cheese Burger", 2, 1, 50],
    ["12:21:00 PM", "12:21:00 PM", 0, 21, "Cheese Burger", 2, 1, 50],
    ["12:21:00 PM", "12:24:00 PM", 3, 22, "Cheese Burger", 2, 1, 50],
    ["12:24:00 PM", "12:24:00 PM", 0, 23, "Chicano Chili Con Carne", 1, 1, 40],
    ["12:24:00 PM", "12:24:00 PM", 0, 24, "Cheese Burger", 2, 1, 50],
    ["12:24:00 PM", "12:28:00 PM", 4, 25, "Hamburger", 2, 1, 40],
    ["12:28:00 PM", "12:30:00 PM", 2, 26, "Tiger Burger", 1, 1, 54],
    ["12:30:00 PM", "12:32:00 PM", 2, 27, "Hamburger", 2, 1, 40],
    ["12:32:00 PM", "12:33:00 PM", 1, 28, "Cheese Burger", 2, 1, 50],
    ["12:33:00 PM", "12:34:00 PM", 1, 29, "Cheese Burger", 2, 1, 50],
    ["12:34:00 PM", "12:34:00 PM", 0, 30, "Cheese Burger", 2, 1, 50],
    ["12:34:00 PM", "12:34:00 PM", 0, 31, "Cheese Burger", 2, 1, 50],
    ["12:34:00 PM", "12:35:00 PM", 1, 32, "Cheese Burger", 2, 1, 50],
    ["12:35:00 PM", "12:42:00 PM", 7, 33, "Hamburger", 2, 1, 40],
    ["12:42:00 PM", "12:45:00 PM", 3, 34, "Hamburger", 2, 1, 40],
    ["12:45:00 PM", "12:47:00 PM", 2, 35, "Cheese Burger", 2, 1, 50],
    ["12:47:00 PM", "12:49:00 PM", 2, 36, "Cheese Burger", 2, 1, 50],
    ["12:49:00 PM", "12:49:00 PM", 0, 37, "Hamburger", 2, 1, 40],
    ["12:49:00 PM", "12:50:00 PM", 1, 38, "Hamburger", 2, 1, 40],
    ["12:50:00 PM", "12:54:00 PM", 4, 39, "Cheese Burger", 4, 2, 100],
    ["12:54:00 PM", "1:00:00 PM", 6, 40, "Cheese Burger", 4, 2, 100],
    ["1:00:00 PM", "1:00:00 PM", 0, 41, "Hamburger", 2, 1, 40]
]

# Define column names
columns = ["Time start", "Time end", "Order Time Duration", "Customer Number",
           "Products", "Quantity", "Orders", "Price"]

# Create DataFrame
df = pd.DataFrame(data, columns=columns)

# Save DataFrame to CSV file
df.to_csv('your_data.csv', index=False)
