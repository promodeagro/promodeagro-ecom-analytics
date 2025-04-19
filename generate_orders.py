import json
import random
import pandas as pd
from google.colab import drive
import os

def create_order_data():
    # Define base data
    customers = [
        {'name': 'Rahul Sharma', 'phone': '+91-9876543210'},
        {'name': 'Priya Patel', 'phone': '+91-9876543211'},
        {'name': 'Amit Kumar', 'phone': '+91-9876543212'},
        {'name': 'Sneha Singh', 'phone': '+91-9876543213'},
        {'name': 'Rajesh Verma', 'phone': '+91-9876543214'},
        {'name': 'Meera Reddy', 'phone': '+91-9876543215'},
        {'name': 'Vikram Malhotra', 'phone': '+91-9876543216'},
        {'name': 'Anjali Desai', 'phone': '+91-9876543217'},
        {'name': 'Suresh Menon', 'phone': '+91-9876543218'},
        {'name': 'Pooja Gupta', 'phone': '+91-9876543219'}
    ]
    
    # Define product categories and their price ranges
    product_categories = {
        'V': {'min_price': 20, 'max_price': 100},  # Vegetables
        'F': {'min_price': 30, 'max_price': 150},  # Fruits
        'D': {'min_price': 40, 'max_price': 200},  # Dairy
        'N': {'min_price': 100, 'max_price': 500}, # Non-Vegetarian
        'G': {'min_price': 50, 'max_price': 300}   # Grocery
    }
    
    # Generate 5000 orders
    orders = []
    for i in range(1, 5001):
        # Select a random customer
        customer = random.choice(customers)
        
        # Generate random order items
        order_items = {}
        total = 0
        
        # Generate 5-10 random items per order
        num_items = random.randint(5, 10)
        for _ in range(num_items):
            # Select a random category
            category = random.choice(list(product_categories.keys()))
            # Generate a random product ID (e.g., V001, F002, etc.)
            product_id = f"{category}{random.randint(1, 8):03d}"
            # Generate random quantity (1-5)
            quantity = random.randint(1, 5)
            
            # Calculate price based on category
            price_range = product_categories[category]
            price = random.uniform(price_range['min_price'], price_range['max_price'])
            
            order_items[product_id] = quantity
            total += price * quantity
        
        order = {
            'Order ID': f'ORD{i:04d}',  # Updated to 4 digits for 5000 orders
            'Customer Name': customer['name'],
            'Phone No': customer['phone'],
            'Order Items': json.dumps(order_items),
            'Total': round(total, 2)
        }
        orders.append(order)
    
    return pd.DataFrame(orders)

def save_to_drive(df, filename='orders.xlsx'):
    try:
        # Mount Google Drive
        drive.mount('/content/drive')

        # Create path for saving the file
        save_path = '/content/drive/My Drive/analytics/'
        full_path = os.path.join(save_path, filename)

        # Save the DataFrame to Excel
        df.to_excel(full_path, index=False)
        print(f"File successfully saved to: {full_path}")

        # Display the DataFrame
        print("\nOrder Table (first 10 rows):")
        print(df.head(10))

        # Display basic information about the DataFrame
        print("\nDataFrame Info:")
        print(df.info())

        # Display basic statistics
        print("\nBasic Statistics:")
        print(df.describe(include='all'))

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    # Create the order DataFrame
    orders_df = create_order_data()

    # Save to Google Drive
    save_to_drive(orders_df)

if __name__ == "__main__":
    main() 