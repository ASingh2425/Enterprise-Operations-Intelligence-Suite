import os
import pandas as pd
import numpy as np

def clean_data():
    print("Executing Data Cleaning & Preprocessing ETL Pipeline...")
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    raw_dir = os.path.join(base_dir, 'data', 'raw')
    processed_dir = os.path.join(base_dir, 'data', 'processed')
    
    # Read raw datasets
    orders = pd.read_csv(os.path.join(raw_dir, 'Orders.csv'))
    customers = pd.read_csv(os.path.join(raw_dir, 'Customers.csv'))
    products = pd.read_csv(os.path.join(raw_dir, 'Products.csv'))
    inventory = pd.read_csv(os.path.join(raw_dir, 'Inventory.csv'))
    suppliers = pd.read_csv(os.path.join(raw_dir, 'Suppliers.csv'))
    logistics = pd.read_csv(os.path.join(raw_dir, 'Logistics_Carriers.csv'))
    returns = pd.read_csv(os.path.join(raw_dir, 'Returns.csv'))
    calendar = pd.read_csv(os.path.join(raw_dir, 'DimCalendar.csv'))
    
    # 1. Deduplication
    orders_clean = orders.drop_duplicates(subset=['OrderID'])
    customers_clean = customers.drop_duplicates(subset=['CustomerID'])
    products_clean = products.drop_duplicates(subset=['ProductID'])
    
    # 2. Null Value Treatment & Fallback
    orders_clean['DiscountRate'] = orders_clean['DiscountRate'].fillna(0.0)
    orders_clean['ShippingCost'] = orders_clean['ShippingCost'].fillna(orders_clean['ShippingCost'].median())
    
    # 3. Data Type Enforcements
    orders_clean['OrderDate'] = pd.to_datetime(orders_clean['OrderDate'])
    returns['ReturnDate'] = pd.to_datetime(returns['ReturnDate'])
    calendar['FullDate'] = pd.to_datetime(calendar['FullDate'])
    
    # 4. Outlier Handling on Orders Shipping Costs & Profits (Winsorization)
    p99_ship = orders_clean['ShippingCost'].quantile(0.99)
    orders_clean['ShippingCost_Capped'] = np.where(orders_clean['ShippingCost'] > p99_ship, p99_ship, orders_clean['ShippingCost'])
    
    # Save cleaned versions
    orders_clean.to_csv(os.path.join(processed_dir, 'Cleaned_Orders.csv'), index=False)
    customers_clean.to_csv(os.path.join(processed_dir, 'Cleaned_Customers.csv'), index=False)
    products_clean.to_csv(os.path.join(processed_dir, 'Cleaned_Products.csv'), index=False)
    inventory.to_csv(os.path.join(processed_dir, 'Cleaned_Inventory.csv'), index=False)
    suppliers.to_csv(os.path.join(processed_dir, 'Cleaned_Suppliers.csv'), index=False)
    returns.to_csv(os.path.join(processed_dir, 'Cleaned_Returns.csv'), index=False)
    
    print(" Data Cleaning Completed Successfully! Cleaned files stored in data/processed/")

if __name__ == '__main__':
    clean_data()
