import csv
import random
import datetime

# Data options for realistic values
regions = ["North", "South", "East", "West", "Central"]
product_categories = ["Electronics", "Clothing", "Home Goods", "Books", "Food"]
product_names = {  # Example products, expand as needed
    "Electronics": ["Laptop", "Smartphone", "Tablet", "Headphones"],
    "Clothing": ["T-Shirt", "Jeans", "Dress", "Sweater"],
    "Home Goods": ["Table", "Chair", "Lamp", "Rug"],
    "Books": ["Fiction", "Non-Fiction", "Sci-Fi", "Mystery"],
    "Food": ["Snacks", "Beverages", "Produce", "Grains"]
}
genders = ["Male", "Female"]

customer_satisfaction = random.randint(1, 5)  # 1 to 5 scale


def generate_random_data(num_rows):
    data = []
    for _ in range(num_rows):
        date = (datetime.date(2022, 1, 1) + datetime.timedelta(days=random.randint(0, 730))).strftime("%Y-%m-%d") # Dates within 2 years
        region = random.choice(regions)
        product_category = random.choice(product_categories)
        product_name = random.choice(product_names[product_category])
        units_sold = random.randint(1, 50)
        revenue = round(random.uniform(10, 500) * units_sold, 2)  # Revenue with 2 decimal places
        customer_age = random.randint(18, 70)
        customer_gender = random.choice(genders)
        customer_satisfaction = random.randint(1, 5)  # 1 to 5 scale
        product_cost = round(random.uniform(5, 250) * units_sold, 2)
        profit = round(revenue - product_cost, 2)
        data.append([date, region, product_category, product_name, units_sold, revenue, customer_age, customer_gender, customer_satisfaction, product_cost, profit])
    return data

# Generate the data
data = generate_random_data(1050)

# Write to CSV
with open('sales_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Date", "Region", "Product Category", "Product Name", "Units Sold", "Revenue", "Customer Age", "Customer Gender", "Customer Satisfaction", "Product Cost", "Profit"]) # Header row
    writer.writerows(data)

print("CSV file 'sales_data.csv' created successfully.")