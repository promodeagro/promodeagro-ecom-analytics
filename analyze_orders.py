import pandas as pd
import os
from google.colab import drive

def load_transformed_data():
    """Load transformed data from Google Drive"""
    try:
        # Mount Google Drive
        drive.mount('/content/drive')
        
        # Define path
        file_path = '/content/drive/My Drive/analytics/transformed_orders.xlsx'
        
        # Load data
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        return None

def analyze_vegetable_sales(df):
    """Analyze vegetable sales from the transformed data"""
    try:
        # Get all vegetable columns
        vegetable_columns = [col for col in df.columns if col.startswith('Vegetables.')]
        
        # Calculate total sales for each vegetable
        vegetable_sales = {}
        for col in vegetable_columns:
            vegetable_name = col.split('.')[1]
            total_quantity = df[col].sum()
            vegetable_sales[vegetable_name] = total_quantity
        
        # Create a DataFrame for the results
        results_df = pd.DataFrame({
            'Vegetable': list(vegetable_sales.keys()),
            'Total Quantity Sold': list(vegetable_sales.values())
        })
        
        # Sort by quantity sold
        results_df = results_df.sort_values('Total Quantity Sold', ascending=False)
        
        return results_df
    except Exception as e:
        print(f"Error analyzing vegetable sales: {str(e)}")
        return None

def analyze_category_sales(df):
    """Analyze sales by product category"""
    try:
        # Get all product columns
        product_columns = [col for col in df.columns if '.' in col]
        
        # Calculate total sales for each category
        category_sales = {}
        for col in product_columns:
            category = col.split('.')[0]
            if category not in category_sales:
                category_sales[category] = 0
            category_sales[category] += df[col].sum()
        
        # Create a DataFrame for the results
        results_df = pd.DataFrame({
            'Category': list(category_sales.keys()),
            'Total Quantity Sold': list(category_sales.values())
        })
        
        # Sort by quantity sold
        results_df = results_df.sort_values('Total Quantity Sold', ascending=False)
        
        return results_df
    except Exception as e:
        print(f"Error analyzing category sales: {str(e)}")
        return None

def analyze_top_customers(df):
    """Analyze top customers by total order value"""
    try:
        # Group by customer and calculate total spent
        customer_analysis = df.groupby(['Customer Name', 'Phone No'])['Total'].agg([
            ('Total Spent', 'sum'),
            ('Number of Orders', 'count'),
            ('Average Order Value', 'mean')
        ]).round(2)
        
        # Sort by total spent
        customer_analysis = customer_analysis.sort_values('Total Spent', ascending=False)
        
        return customer_analysis
    except Exception as e:
        print(f"Error analyzing customer data: {str(e)}")
        return None

def main():
    # Load transformed data
    df = load_transformed_data()
    
    if df is not None:
        print("\n=== Vegetable Sales Analysis ===")
        vegetable_sales = analyze_vegetable_sales(df)
        if vegetable_sales is not None:
            print("\nTotal Quantity Sold by Vegetable:")
            print(vegetable_sales)
        
        print("\n=== Category Sales Analysis ===")
        category_sales = analyze_category_sales(df)
        if category_sales is not None:
            print("\nTotal Quantity Sold by Category:")
            print(category_sales)
        
        print("\n=== Top Customers Analysis ===")
        top_customers = analyze_top_customers(df)
        if top_customers is not None:
            print("\nTop Customers by Total Spent:")
            print(top_customers.head(10))
    else:
        print("Failed to load data. Please check the file path and try again.")

if __name__ == "__main__":
    main() 