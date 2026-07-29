import os
import pandas as pd
import numpy as np

def run_inventory_optimization():
    print("Executing ABC Classification, EOQ, & Safety Stock Optimization...")
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    processed_dir = os.path.join(base_dir, 'data', 'processed')
    
    orders = pd.read_csv(os.path.join(processed_dir, 'Enriched_Orders.csv'))
    inventory = pd.read_csv(os.path.join(processed_dir, 'Cleaned_Inventory.csv'))
    products = pd.read_csv(os.path.join(processed_dir, 'Cleaned_Products.csv'))
    
    # 1. Product Annual Demand & Revenue
    prod_demand = orders.groupby('ProductID').agg({
        'Quantity': 'sum',
        'NetRevenue': 'sum'
    }).reset_index()
    prod_demand.rename(columns={'Quantity': 'AnnualDemand', 'NetRevenue': 'TotalProductRevenue'}, inplace=True)
    
    # Merge with product catalog
    df_inv = inventory.merge(prod_demand, on='ProductID', how='left')
    df_inv = df_inv.merge(products[['ProductID', 'Cost', 'SellingPrice']], on='ProductID', how='left')
    
    df_inv['AnnualDemand'] = df_inv['AnnualDemand'].fillna(100)
    df_inv['TotalProductRevenue'] = df_inv['TotalProductRevenue'].fillna(df_inv['AnnualDemand'] * df_inv['SellingPrice'])
    
    # 2. ABC Classification (Pareto Pareto distribution on Total Revenue)
    df_sorted = df_inv.sort_values(by='TotalProductRevenue', ascending=False).reset_index(drop=True)
    df_sorted['CumRevenue'] = df_sorted['TotalProductRevenue'].cumsum()
    total_rev = df_sorted['TotalProductRevenue'].sum()
    df_sorted['CumPct'] = df_sorted['CumRevenue'] / total_rev
    
    def get_abc(pct):
        if pct <= 0.80:
            return 'A (High Value)'
        elif pct <= 0.95:
            return 'B (Medium Value)'
        else:
            return 'C (Low Value)'
            
    df_sorted['ABC_Category'] = df_sorted['CumPct'].apply(get_abc)
    
    # 3. EOQ (Economic Order Quantity) Calculation
    # Formula: sqrt((2 * Demand * OrderCost) / HoldingCost)
    # Assume fixed Ordering Cost S = $125 per order
    S = 125.0
    df_sorted['UnitHoldingCost'] = np.where(df_sorted['UnitHoldingCost'] <= 0, df_sorted['Cost'] * 0.15, df_sorted['UnitHoldingCost'])
    df_sorted['EOQ'] = np.round(np.sqrt((2 * df_sorted['AnnualDemand'] * S) / df_sorted['UnitHoldingCost']), 0)
    
    # 4. Safety Stock Calculation (95% service level -> Z = 1.65)
    # Safety Stock = Z * sqrt(LeadTime) * StdDev_Daily_Demand
    Z = 1.65
    daily_std = 4.5 # Average daily demand variation
    df_sorted['SafetyStock'] = np.round(Z * np.sqrt(df_sorted['LeadTimeDays']) * daily_std, 0)
    
    # 5. Inventory Valuation & Days of Inventory (DOI)
    df_sorted['InventoryValuation'] = np.round(df_sorted['CurrentStock'] * df_sorted['Cost'], 2)
    daily_cost_sales = (df_sorted['AnnualDemand'] * df_sorted['Cost']) / 365.0
    df_sorted['DaysOfInventory'] = np.round(df_sorted['InventoryValuation'] / np.maximum(daily_cost_sales, 1.0), 1)
    df_sorted['InventoryTurnoverRatio'] = np.round(365.0 / np.maximum(df_sorted['DaysOfInventory'], 1.0), 2)
    
    df_sorted.to_csv(os.path.join(processed_dir, 'Inventory_Optimization_Metrics.csv'), index=False)
    print(" Inventory Optimization Completed! Metrics saved to data/processed/Inventory_Optimization_Metrics.csv")

if __name__ == '__main__':
    run_inventory_optimization()
