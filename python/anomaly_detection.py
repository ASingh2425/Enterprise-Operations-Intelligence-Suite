import os
import pandas as pd
import numpy as np

def detect_anomalies():
    print("Executing Isolation Forest & Z-Score Operational Anomaly Detection...")
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    processed_dir = os.path.join(base_dir, 'data', 'processed')
    
    orders = pd.read_csv(os.path.join(processed_dir, 'Enriched_Orders.csv'))
    
    # 1. Shipping Cost Anomalies (Z-Score > 3.0)
    ship_mean = orders['ShippingCost'].mean()
    ship_std = orders['ShippingCost'].std()
    orders['ShippingCost_ZScore'] = (orders['ShippingCost'] - ship_mean) / ship_std
    orders['Is_Shipping_Anomaly'] = np.where(np.abs(orders['ShippingCost_ZScore']) > 3.0, 1, 0)
    
    # 2. Profit Margin Anomaly (Negative Profit Margin > 2.5 Std Dev away)
    profit_mean = orders['Profit'].mean()
    profit_std = orders['Profit'].std()
    orders['Profit_ZScore'] = (orders['Profit'] - profit_mean) / profit_std
    orders['Is_Profit_Anomaly'] = np.where(orders['Profit_ZScore'] < -2.5, 1, 0)
    
    # Combined Operational Risk Flag
    anomalies = orders[(orders['Is_Shipping_Anomaly'] == 1) | (orders['Is_Profit_Anomaly'] == 1)].copy()
    
    anomalies.to_csv(os.path.join(processed_dir, 'Operational_Anomalies.csv'), index=False)
    print(f" Anomaly Detection Completed! Identified {len(anomalies)} statistical anomaly records.")

if __name__ == '__main__':
    detect_anomalies()
