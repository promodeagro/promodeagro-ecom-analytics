import csv
import random
import pandas as pd
from google.colab import drive
import os

def create_product_data():
    # Define product categories and their base items
    product_categories = {
        'Vegetables': [
            'Tomatoes', 'Potatoes', 'Onions', 'Carrots', 'Spinach', 'Cauliflower', 'Capsicum', 'Green Peas',
            'Broccoli', 'Cabbage', 'Lettuce', 'Cucumber', 'Bell Pepper', 'Zucchini', 'Eggplant', 'Mushrooms',
            'Beans', 'Corn', 'Pumpkin', 'Radish', 'Beetroot', 'Turnip', 'Sweet Potato', 'Yam', 'Ginger',
            'Garlic', 'Celery', 'Asparagus', 'Artichoke', 'Okra', 'Bitter Gourd', 'Bottle Gourd', 'Ridge Gourd'
        ],
        'Fruits': [
            'Apples', 'Bananas', 'Oranges', 'Mangoes', 'Grapes', 'Watermelon', 'Papaya', 'Pomegranate',
            'Pineapple', 'Strawberries', 'Blueberries', 'Raspberries', 'Blackberries', 'Kiwi', 'Peaches',
            'Plums', 'Apricots', 'Cherries', 'Guava', 'Lychee', 'Dragon Fruit', 'Passion Fruit', 'Jackfruit',
            'Custard Apple', 'Sapodilla', 'Star Fruit', 'Persimmon', 'Mulberries', 'Cranberries', 'Gooseberries',
            'Elderberries', 'Currants', 'Dates', 'Figs'
        ],
        'Dairy': [
            'Milk', 'Curd', 'Butter', 'Cheese', 'Paneer', 'Ghee', 'Buttermilk', 'Cream',
            'Yogurt', 'Sour Cream', 'Cottage Cheese', 'Ricotta', 'Mozzarella', 'Cheddar', 'Feta',
            'Parmesan', 'Swiss Cheese', 'Provolone', 'Gouda', 'Brie', 'Camembert', 'Blue Cheese',
            'Goat Cheese', 'Condensed Milk', 'Evaporated Milk', 'Powdered Milk', 'Whipped Cream',
            'Ice Cream', 'Frozen Yogurt', 'Kefir', 'Clotted Cream', 'Mascarpone', 'Quark', 'Labneh'
        ],
        'Non-Vegetarian': [
            'Chicken', 'Fish', 'Mutton', 'Eggs', 'Prawns', 'Turkey', 'Crab', 'Lobster',
            'Shrimp', 'Squid', 'Octopus', 'Oysters', 'Mussels', 'Clams', 'Scallops', 'Duck',
            'Goose', 'Quail', 'Pheasant', 'Venison', 'Rabbit', 'Bacon', 'Ham', 'Sausages',
            'Salami', 'Pepperoni', 'Beef', 'Pork', 'Lamb', 'Goat', 'Bison', 'Elk', 'Wild Boar'
        ],
        'Grocery': [
            'Rice', 'Wheat Flour', 'Pulses', 'Cooking Oil', 'Sugar', 'Salt', 'Spices', 'Tea & Coffee',
            'Pasta', 'Noodles', 'Cereals', 'Oats', 'Cornflakes', 'Muesli', 'Granola', 'Bread',
            'Biscuits', 'Cookies', 'Crackers', 'Chips', 'Popcorn', 'Nuts', 'Dried Fruits', 'Honey',
            'Jam', 'Jelly', 'Peanut Butter', 'Chocolate', 'Cocoa Powder', 'Baking Powder', 'Yeast',
            'Vinegar', 'Soy Sauce', 'Ketchup', 'Mayonnaise', 'Mustard', 'Olives', 'Pickles'
        ]
    }

    # Generate product data
    products = []
    for category, base_items in product_categories.items():
        prefix = category[0].upper()  # First letter of category
        for i in range(1, 101):  # Generate 100 products per category
            # Randomly select a base item
            base_item = random.choice(base_items)
            # Add variations to create more unique products
            variations = ['Organic', 'Premium', 'Fresh', 'Frozen', 'Dried', 'Local', 'Imported', 
                         'Extra Large', 'Medium', 'Small', 'Family Pack', 'Value Pack']
            variation = random.choice(variations)
            product_name = f"{variation} {base_item}"
            
            product_id = f"{prefix}{i:03d}"  # Format: V001, F001, etc.
            products.append({
                'Product ID': product_id,
                'Product Category': category,
                'Product Name': product_name
            })

    print(f"Product data has been generated  with {len(products)} products")
    return pd.DataFrame(products)

def save_to_drive(df, filename='products.xlsx'):
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
        print("\nCustomer Table:")
        print(df)

        # Display basic information about the DataFrame
        print("\nDataFrame Info:")
        print(df.info())

        # Display basic statistics
        print("\nBasic Statistics:")
        print(df.describe(include='all'))

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    # Create the customer DataFrame
    products_df = create_product_data()

    # Save to Google Drive
    save_to_drive(products_df)

if __name__ == "__main__":
    main()