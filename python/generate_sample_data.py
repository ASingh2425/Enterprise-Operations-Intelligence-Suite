import os
import pandas as pd

def create_sample_datasets():
    print("Generating committed sample datasets in data/sample/...")
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    raw_dir = os.path.join(base_dir, 'data', 'raw')
    sample_dir = os.path.join(base_dir, 'data', 'sample')
    os.makedirs(sample_dir, exist_ok=True)
    
    files_to_sample = {
        'Orders.csv': ('Sample_Orders.csv', 1000),
        'Customers.csv': ('Sample_Customers.csv', 200),
        'Products.csv': ('Sample_Products.csv', 100),
        'Warehouses.csv': ('Sample_Warehouses.csv', 15),
        'Suppliers.csv': ('Sample_Suppliers.csv', 40),
        'Logistics_Carriers.csv': ('Sample_Logistics_Carriers.csv', 8),
        'Inventory.csv': ('Sample_Inventory.csv', 300),
        'Returns.csv': ('Sample_Returns.csv', 150)
    }
    
    for raw_filename, (sample_filename, n_rows) in files_to_sample.items():
        raw_path = os.path.join(raw_dir, raw_filename)
        sample_path = os.path.join(sample_dir, sample_filename)
        if os.path.exists(raw_path):
            df = pd.read_csv(raw_path)
            sample_df = df.head(min(n_rows, len(df)))
            sample_df.to_csv(sample_path, index=False)
            print(f" Saved {len(sample_df)} rows to data/sample/{sample_filename}")
            
    print(" Sample datasets created in data/sample/")

if __name__ == '__main__':
    create_sample_datasets()
