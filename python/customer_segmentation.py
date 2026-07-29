import os
import pandas as pd
import numpy as np

def run_rfm_segmentation():
    print("Executing RFM Customer Segmentation & LTV Analysis...")
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    processed_dir = os.path.join(base_dir, 'data', 'processed')
    
    orders = pd.read_csv(os.path.join(processed_dir, 'Enriched_Orders.csv'))
    orders['OrderDate'] = pd.to_datetime(orders['OrderDate'])
    
    max_date = orders['OrderDate'].max() + pd.Timedelta(days=1)
    
    # Calculate RFM per customer
    rfm = orders.groupby('CustomerID').agg({
        'OrderDate': lambda x: (max_date - x.max()).days, # Recency
        'OrderID': 'count',                                # Frequency
        'NetRevenue': 'sum'                                # Monetary
    }).reset_index()
    
    rfm.columns = ['CustomerID', 'RecencyDays', 'Frequency', 'MonetaryValue']
    
    # RFM Scoring (1 to 4)
    rfm['R_Score'] = pd.qcut(rfm['RecencyDays'], q=4, labels=[4, 3, 2, 1])
    rfm['F_Score'] = pd.qcut(rfm['Frequency'].rank(method='first'), q=4, labels=[1, 2, 3, 4])
    rfm['M_Score'] = pd.qcut(rfm['MonetaryValue'], q=4, labels=[1, 2, 3, 4])
    
    rfm['RFM_Cell'] = rfm['R_Score'].astype(str) + rfm['F_Score'].astype(str) + rfm['M_Score'].astype(str)
    
    # Segment Assignment
    def assign_segment(row):
        r = int(row['R_Score'])
        f = int(row['F_Score'])
        m = int(row['M_Score'])
        score = r + f + m
        
        if score >= 10 and r >= 3:
            return 'Champions'
        elif score >= 8 and f >= 3:
            return 'Loyal Customers'
        elif r <= 2 and score >= 6:
            return 'At Risk'
        elif r <= 2 and score < 6:
            return 'Lost / Churned'
        else:
            return 'Promising / Potential'
            
    rfm['CustomerSegment'] = rfm.apply(assign_segment, axis=1)
    
    rfm.to_csv(os.path.join(processed_dir, 'Customer_RFM_Segments.csv'), index=False)
    print(f" Customer Segmentation Completed! Processed {len(rfm)} customers into 5 strategic segments.")

if __name__ == '__main__':
    run_rfm_segmentation()
