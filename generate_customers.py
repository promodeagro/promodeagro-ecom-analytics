import csv
import random
import pandas as pd
import os
from google.colab import drive

def create_customer_data():
    # Define base data for generating customers
    first_names = ['Rahul', 'Priya', 'Amit', 'Sneha', 'Rajesh', 'Meera', 'Vikram', 'Anjali', 'Suresh', 'Pooja']
    last_names = ['Sharma', 'Patel', 'Kumar', 'Singh', 'Verma', 'Reddy', 'Malhotra', 'Desai', 'Menon', 'Gupta']
    cities = ['Kolkata', 'Mumbai', 'Bangalore', 'Delhi', 'Hyderabad', 'Chennai', 'Pune', 'Ahmedabad', 'Kochi', 'Jaipur']
    streets = ['Park Street', 'MG Road', 'Brigade Road', 'Civil Lines', 'Jubilee Hills', 
              'Anna Nagar', 'Aundh', 'CG Road', 'MG Marg', 'Civil Lines']
    
    # Generate 1000 customers
    customers = []
    for i in range(1, 1001):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        city = random.choice(cities)
        street = random.choice(streets)
        house_number = random.randint(1, 999)
        
        customer = {
            'Customer ID': f'CUST{i:03d}',
            'Phone No': f'+91-{random.randint(9000000000, 9999999999)}',
            'Name': f'{first_name} {last_name}',
            'Address': f'{house_number} {street}, {city}'
        }
        customers.append(customer)
    
    return pd.DataFrame(customers)

def save_to_drive(df, filename='customers.xlsx'):
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
        print("\nCustomer Table (first 10 rows):")
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
    # Create the customer DataFrame
    customers_df = create_customer_data()

    # Save to Google Drive
    save_to_drive(customers_df)

if __name__ == "__main__":
    main() 