import os
import pandas as pd
import numpy as np

def run_feature_engineering():
    print("Executing Feature Engineering Pipeline...")
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    processed_dir = os.path.join(base_dir, 'data', 'processed')
    
    orders = pd.read_csv(os.path.join(processed_dir, 'Cleaned_Orders.csv'))
    products = pd.read_csv(os.path.join(processed_dir, 'Cleaned_Products.csv'))
    returns = pd.read_csv(os.path.join(processed_dir, 'Cleaned_Returns.csv'))
    
    # 1. Enriched Margin % Metrics
    orders['ProfitMarginPct'] = np.round((orders['Profit'] / np.maximum(orders['NetRevenue'], 1.0)) * 100, 2)
    
    # 2. Perfect Order Indicator (Not Late & Not Returned)
    returned_order_ids = set(returns['OrderID'].values)
    orders['IsReturned'] = orders['OrderID'].apply(lambda x: 1 if x in returned_order_ids else 0)
    orders['IsPerfectOrder'] = np.where((orders['IsLate'] == 0) & (orders['IsReturned'] == 0), 1, 0)
    
    # 3. SLA Delivery Performance Category
    conditions = [
        orders['TransitDays'] < orders['PromisedDays'],
        orders['TransitDays'] == orders['PromisedDays'],
        orders['TransitDays'] > orders['PromisedDays']
    ]
    choices = ['Early', 'On-Time', 'Delayed']
    orders['DeliveryStatus'] = np.select(conditions, choices, default='On-Time')
    
    # 4. Product Category Enriched Join
    prod_map = dict(zip(products['ProductID'], products['Category']))
    sub_map = dict(zip(products['ProductID'], products['SubCategory']))
    orders['Category'] = orders['ProductID'].map(prod_map)
    orders['SubCategory'] = orders['ProductID'].map(sub_map)
    
    # Save enriched orders
    orders.to_csv(os.path.join(processed_dir, 'Enriched_Orders.csv'), index=False)
    print(" Feature Engineering Completed! Enriched_Orders.csv created.")

if __name__ == '__main__':
    run_feature_engineering()
