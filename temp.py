import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

# Initialize Faker to generate fake data
fake = Faker()

# Function to generate random date within a given range
def random_date(start, end):
    return start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))

# Generate dataset
data = []

# Specify the range for dates
start_date = datetime(2022, 1, 1)
end_date = datetime(2023, 12, 31)

# Generate 1000 records
for _ in range(1000):
    order_date = random_date(start_date, end_date)
    order_time = fake.time_object()
    aging = random.randint(1, 30)
    customer_id = fake.uuid4()
    gender = random.choice(['Male', 'Female'])
    device_type = random.choice(['Mobile', 'Desktop', 'Tablet'])
    customer_login_type = random.choice(['Email', 'Social Media', 'Guest'])
    product_category = fake.random_element(elements=('Electronics', 'Clothing', 'Books', 'Home Appliances'))
    product = fake.word()
    sales = round(random.uniform(10, 1000), 2)
    quantity = random.randint(1, 5)
    discount = round(random.uniform(0, 0.3) * sales, 2)
    profit = round(random.uniform(0, 0.2) * sales, 2)
    shipping_cost = round(random.uniform(1, 20), 2)
    order_priority = random.choice(['High', 'Medium', 'Low'])
    payment_method = random.choice(['Credit Card', 'Debit Card', 'PayPal', 'Cash on Delivery'])

    data.append([order_date, order_time, aging, customer_id, gender, device_type, customer_login_type,
                 product_category, product, sales, quantity, discount, profit, shipping_cost, order_priority, payment_method])

# Create DataFrame
columns = ['Order_Date', 'Time', 'Aging', 'Customer_Id', 'Gender', 'Device_Type', 'Customer_Login_Type',
           'Product_Category', 'Product', 'Sales', 'Quantity', 'Discount', 'Profit', 'Shipping_Cost', 'Order_Priority', 'Payment_Method']
df = pd.DataFrame(data, columns=columns)

# Save DataFrame to CSV file
df.to_csv('ecommerce_dataset.csv', index=False)
