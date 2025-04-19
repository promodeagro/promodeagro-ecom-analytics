import pandas as pd
import json
import os
from google.colab import drive

def load_data():
    """Load data from Google Drive"""
    try:
        # Mount Google Drive
        drive.mount('/content/drive')
        
        # Define paths
        base_path = '/content/drive/My Drive/analytics/'
        orders_path = os.path.join(base_path, 'orders.xlsx')
        products_path = os.path.join(base_path, 'products.xlsx')
        customers_path = os.path.join(base_path, 'customers.xlsx')
        
        # Load data
        orders_df = pd.read_excel(orders_path)
        products_df = pd.read_excel(products_path)
        customers_df = pd.read_excel(customers_path)
        
        return orders_df, products_df, customers_df
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        return None, None, None

def generate_features(orders_df, products_df, customers_df):
    """Generate features from the data"""
    try:
        # Create a mapping of product IDs to their names and categories
        product_map = {}
        for _, row in products_df.iterrows():
            category = row['Product Category']
            name = row['Product Name']
            product_id = row['Product ID']
            product_map[product_id] = {'category': category, 'name': name}
        
        # Initialize the transformed dataframe with basic order information
        transformed_df = orders_df[['Order ID', 'Customer Name', 'Phone No', 'Total']].copy()
        
        # Create columns for each product
        for product_id, info in product_map.items():
            category = info['category']
            name = info['name']
            column_name = f"{category}.{name}"
            transformed_df[column_name] = 0
        
        # Fill in the quantities for each order
        for idx, row in orders_df.iterrows():
            order_items = json.loads(row['Order Items'])
            for product_id, quantity in order_items.items():
                if product_id in product_map:
                    info = product_map[product_id]
                    category = info['category']
                    name = info['name']
                    column_name = f"{category}.{name}"
                    transformed_df.at[idx, column_name] = quantity
        
        # Reorder columns to match the required format
        base_columns = ['Order ID', 'Customer Name', 'Phone No']
        product_columns = sorted([col for col in transformed_df.columns if '.' in col])
        total_column = ['Total']
        final_columns = base_columns + product_columns + total_column
        
        transformed_df = transformed_df[final_columns]
        
        return transformed_df
    except Exception as e:
        print(f"Error generating features: {str(e)}")
        return None

def save_transformed_data(df, filename='transformed_orders.xlsx'):
    """Save the transformed data to Google Drive"""
    try:
        # Mount Google Drive
        drive.mount('/content/drive')
        
        # Create path for saving the file
        save_path = '/content/drive/My Drive/analytics/'
        full_path = os.path.join(save_path, filename)
        
        # Save the DataFrame to Excel
        df.to_excel(full_path, index=False)
        print(f"Transformed data successfully saved to: {full_path}")
        
        # Display the first few rows
        print("\nTransformed Data (first 10 rows):")
        print(df.head(10))
        
    except Exception as e:
        print(f"Error saving transformed data: {str(e)}")

def main():
    # Load data
    orders_df, products_df, customers_df = load_data()
    
    if orders_df is not None and products_df is not None and customers_df is not None:
        # Generate features
        transformed_df = generate_features(orders_df, products_df, customers_df)
        
        if transformed_df is not None:
            # Save transformed data
            save_transformed_data(transformed_df)
    else:
        print("Failed to load data. Please check the file paths and try again.")

if __name__ == "__main__":
    main() 