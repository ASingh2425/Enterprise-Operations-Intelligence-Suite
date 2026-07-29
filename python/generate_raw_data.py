import os
import random
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def main():
    print("Starting synthetic data generation for Enterprise Operations Intelligence Suite...")
    
    # Define directories
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    raw_dir = os.path.join(base_dir, 'data', 'raw')
    processed_dir = os.path.join(base_dir, 'data', 'processed')
    os.makedirs(raw_dir, exist_ok=True)
    os.makedirs(processed_dir, exist_ok=True)
    
    np.random.seed(42)
    random.seed(42)
    
    # 1. Calendar Dimension
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2025, 12, 31)
    date_list = [start_date + timedelta(days=x) for x in range((end_date - start_date).days + 1)]
    
    calendar_df = pd.DataFrame({
        'DateKey': [d.strftime('%Y%m%d') for d in date_list],
        'FullDate': date_list,
        'Year': [d.year for d in date_list],
        'Quarter': [f"Q{(d.month-1)//3 + 1}" for d in date_list],
        'MonthNumber': [d.month for d in date_list],
        'MonthName': [d.strftime('%B') for d in date_list],
        'DayOfWeek': [d.strftime('%A') for d in date_list],
        'IsWeekend': [1 if d.weekday() >= 5 else 0 for d in date_list],
        'IsHoliday': [1 if (d.month==1 and d.day==1) or (d.month==12 and d.day==25) or (d.month==11 and d.day==28) else 0 for d in date_list]
    })
    calendar_df.to_csv(os.path.join(raw_dir, 'DimCalendar.csv'), index=False)
    print(f" DimCalendar generated: {len(calendar_df)} rows")
    
    # 2. Customers Table
    n_customers = 15000
    segments = ['Consumer', 'Corporate', 'Home Office']
    countries = ['United States', 'Canada', 'United Kingdom', 'Germany', 'France', 'Australia', 'Japan']
    cities = {
        'United States': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Seattle'],
        'Canada': ['Toronto', 'Vancouver', 'Montreal'],
        'United Kingdom': ['London', 'Manchester', 'Birmingham'],
        'Germany': ['Berlin', 'Munich', 'Hamburg'],
        'France': ['Paris', 'Lyon', 'Marseille'],
        'Australia': ['Sydney', 'Melbourne', 'Brisbane'],
        'Japan': ['Tokyo', 'Osaka', 'Yokohama']
    }
    regions = {
        'United States': 'North America', 'Canada': 'North America',
        'United Kingdom': 'Europe', 'Germany': 'Europe', 'France': 'Europe',
        'Australia': 'APAC', 'Japan': 'APAC'
    }
    
    cust_data = []
    for i in range(1, n_customers + 1):
        country = random.choice(countries)
        city = random.choice(cities[country])
        seg = np.random.choice(segments, p=[0.50, 0.30, 0.20])
        ltv = round(np.random.exponential(scale=1200) + 150, 2)
        cust_data.append({
            'CustomerID': f"CUST-{i:06d}",
            'Segment': seg,
            'Region': regions[country],
            'Country': country,
            'City': city,
            'LifetimeValue': ltv
        })
    customers_df = pd.DataFrame(cust_data)
    customers_df.to_csv(os.path.join(raw_dir, 'Customers.csv'), index=False)
    print(f" Customers generated: {len(customers_df)} rows")
    
    # 3. Products Table
    categories = {
        'Technology': ['Laptops', 'Smartphones', 'Monitors', 'Audio', 'Accessories'],
        'Furniture': ['Desks', 'Office Chairs', 'Bookcases', 'Storage', 'Lighting'],
        'Office Supplies': ['Paper', 'Binders', 'Pens', 'Storage Boxes', 'Envelopes'],
        'Logistics Gear': ['Pallet Jacks', 'Barcode Scanners', 'Label Printers', 'Packaging Tape', 'Scales']
    }
    brands = ['ApexCorp', 'LogiTech', 'OmniSupplies', 'AmazonBasics', 'IndustrialPlus', 'GlobalGear']
    
    prod_data = []
    prod_id_counter = 1
    for cat, subcats in categories.items():
        for sub in subcats:
            for b in brands[:4]:
                cost = round(random.uniform(10.0, 850.0), 2)
                margin = round(random.uniform(0.15, 0.55), 2)
                price = round(cost / (1 - margin), 2)
                prod_data.append({
                    'ProductID': f"PROD-{prod_id_counter:04d}",
                    'SKU': f"SKU-{cat[:3].upper()}-{sub[:3].upper()}-{prod_id_counter:04d}",
                    'Category': cat,
                    'SubCategory': sub,
                    'Brand': b,
                    'Cost': cost,
                    'SellingPrice': price,
                    'Margin': margin
                })
                prod_id_counter += 1
    products_df = pd.DataFrame(prod_data)
    products_df.to_csv(os.path.join(raw_dir, 'Products.csv'), index=False)
    print(f" Products generated: {len(products_df)} rows")
    
    # 4. Warehouses Table
    warehouses_df = pd.DataFrame([
        {'WarehouseID': 'WH-US-EAST', 'WarehouseName': 'New Jersey Fulfillment Center', 'City': 'Edison', 'Country': 'United States', 'CapacityUnits': 500000, 'OperatingCost': 120000.0},
        {'WarehouseID': 'WH-US-WEST', 'WarehouseName': 'Seattle Hub', 'City': 'Seattle', 'Country': 'United States', 'CapacityUnits': 750000, 'OperatingCost': 180000.0},
        {'WarehouseID': 'WH-EU-CENTRAL', 'WarehouseName': 'Frankfurt Logistics Park', 'City': 'Frankfurt', 'Country': 'Germany', 'CapacityUnits': 600000, 'OperatingCost': 150000.0},
        {'WarehouseID': 'WH-UK-LONDON', 'WarehouseName': 'London Gateway Depot', 'City': 'London', 'Country': 'United Kingdom', 'CapacityUnits': 400000, 'OperatingCost': 110000.0},
        {'WarehouseID': 'WH-APAC-SYD', 'WarehouseName': 'Sydney Express Depot', 'City': 'Sydney', 'Country': 'Australia', 'CapacityUnits': 350000, 'OperatingCost': 95000.0},
        {'WarehouseID': 'WH-APAC-TYO', 'WarehouseName': 'Tokyo Central Fulfillment', 'City': 'Tokyo', 'Country': 'Japan', 'CapacityUnits': 450000, 'OperatingCost': 130000.0}
    ])
    warehouses_df.to_csv(os.path.join(raw_dir, 'Warehouses.csv'), index=False)
    print(f" Warehouses generated: {len(warehouses_df)} rows")
    
    # 5. Suppliers Table
    suppliers_data = []
    supplier_countries = ['United States', 'China', 'Germany', 'Taiwan', 'Japan', 'Vietnam', 'Mexico']
    for i in range(1, 41):
        c = random.choice(supplier_countries)
        rating = round(random.uniform(3.2, 4.95), 2)
        delivery_time = round(random.uniform(3.0, 21.0), 1)
        defect_rate = round(random.uniform(0.002, 0.048), 4)
        suppliers_data.append({
            'SupplierID': f"SUP-{i:03d}",
            'SupplierName': f"Global Supplier {i} ({c})",
            'Country': c,
            'Rating': rating,
            'AvgDeliveryDays': delivery_time,
            'DefectRate': defect_rate,
            'SupplierRiskIndex': round((5 - rating)*15 + defect_rate*1000 + delivery_time*1.5, 2)
        })
    suppliers_df = pd.DataFrame(suppliers_data)
    suppliers_df.to_csv(os.path.join(raw_dir, 'Suppliers.csv'), index=False)
    print(f" Suppliers generated: {len(suppliers_df)} rows")
    
    # 6. Inventory Table
    inv_data = []
    wh_ids = warehouses_df['WarehouseID'].tolist()
    for _, prod in products_df.iterrows():
        for wh in wh_ids:
            stock = random.randint(50, 4500)
            reorder_point = random.randint(150, 800)
            lead_time = random.randint(3, 25)
            unit_holding_cost = round(prod['Cost'] * 0.18, 2)
            inv_data.append({
                'WarehouseID': wh,
                'ProductID': prod['ProductID'],
                'SKU': prod['SKU'],
                'CurrentStock': stock,
                'ReorderPoint': reorder_point,
                'LeadTimeDays': lead_time,
                'UnitHoldingCost': unit_holding_cost,
                'StockoutRiskScore': round(max(0, (reorder_point - stock) / max(reorder_point, 1)), 3)
            })
    inventory_df = pd.DataFrame(inv_data)
    inventory_df.to_csv(os.path.join(raw_dir, 'Inventory.csv'), index=False)
    print(f" Inventory generated: {len(inventory_df)} rows")
    
    # 7. Logistics Carriers Table
    logistics_df = pd.DataFrame([
        {'CarrierID': 'CAR-01', 'CarrierName': 'Amazon Air Logistics', 'ReliabilityScore': 0.96, 'BaseRatePerKm': 0.45},
        {'CarrierID': 'CAR-02', 'CarrierName': 'FedEx Express', 'ReliabilityScore': 0.94, 'BaseRatePerKm': 0.52},
        {'CarrierID': 'CAR-03', 'CarrierName': 'DHL Express Global', 'ReliabilityScore': 0.95, 'BaseRatePerKm': 0.50},
        {'CarrierID': 'CAR-04', 'CarrierName': 'UPS Worldwide', 'ReliabilityScore': 0.92, 'BaseRatePerKm': 0.48},
        {'CarrierID': 'CAR-05', 'CarrierName': 'Regional Freight Co', 'ReliabilityScore': 0.86, 'BaseRatePerKm': 0.35}
    ])
    logistics_df.to_csv(os.path.join(raw_dir, 'Logistics_Carriers.csv'), index=False)
    print(f" Logistics Carriers generated: {len(logistics_df)} rows")
    
    # 8. Orders Fact Table (500,000+ transactional records created efficiently)
    print(" Generating Fact_Orders table (500,000+ rows)...")
    n_orders = 520000
    
    cust_ids = customers_df['CustomerID'].values
    prod_ids = products_df['ProductID'].values
    prod_cost_map = dict(zip(products_df['ProductID'], products_df['Cost']))
    prod_price_map = dict(zip(products_df['ProductID'], products_df['SellingPrice']))
    wh_ids = warehouses_df['WarehouseID'].values
    carrier_ids = logistics_df['CarrierID'].values
    date_keys = calendar_df['FullDate'].values
    
    # Generate random choices in vector batches
    batch_size = n_orders
    rand_cust = np.random.choice(cust_ids, size=batch_size)
    rand_prod = np.random.choice(prod_ids, size=batch_size)
    rand_wh = np.random.choice(wh_ids, size=batch_size)
    rand_carrier = np.random.choice(carrier_ids, size=batch_size)
    rand_dates = np.random.choice(date_keys, size=batch_size)
    
    rand_qty = np.random.randint(1, 12, size=batch_size)
    rand_costs = np.array([prod_cost_map[p] for p in rand_prod])
    rand_prices = np.array([prod_price_map[p] for p in rand_prod])
    
    # Discounts & Financial calculations
    discounts = np.random.choice([0.0, 0.05, 0.10, 0.15, 0.20], size=batch_size, p=[0.5, 0.2, 0.15, 0.1, 0.05])
    gross_revenue = rand_qty * rand_prices
    discount_amount = gross_revenue * discounts
    net_revenue = gross_revenue - discount_amount
    cogs = rand_qty * rand_costs
    shipping_costs = np.round(np.random.uniform(4.5, 48.0, size=batch_size), 2)
    profit = net_revenue - cogs - shipping_costs
    
    # SLA & transit times
    transit_days = np.random.randint(1, 8, size=batch_size)
    promised_days = transit_days + np.random.choice([0, 1, -1], size=batch_size, p=[0.75, 0.15, 0.10])
    is_late = (transit_days > promised_days).astype(int)
    
    orders_df = pd.DataFrame({
        'OrderID': [f"ORD-{i:08d}" for i in range(1, batch_size + 1)],
        'OrderDate': pd.to_datetime(rand_dates).strftime('%Y-%m-%d'),
        'CustomerID': rand_cust,
        'ProductID': rand_prod,
        'WarehouseID': rand_wh,
        'CarrierID': rand_carrier,
        'Quantity': rand_qty,
        'UnitPrice': rand_prices,
        'UnitCost': rand_costs,
        'DiscountRate': discounts,
        'GrossRevenue': np.round(gross_revenue, 2),
        'NetRevenue': np.round(net_revenue, 2),
        'COGS': np.round(cogs, 2),
        'ShippingCost': shipping_costs,
        'Profit': np.round(profit, 2),
        'TransitDays': transit_days,
        'PromisedDays': promised_days,
        'IsLate': is_late
    })
    
    orders_df.to_csv(os.path.join(raw_dir, 'Orders.csv'), index=False)
    print(f" Fact_Orders generated: {len(orders_df)} rows")
    
    # 9. Returns Table
    print(" Generating Returns table...")
    # ~5% of orders get returned
    returned_orders = orders_df.sample(frac=0.048, random_state=42).copy()
    return_reasons = ['Defective Product', 'Late Delivery', 'Wrong Item Sent', 'Buyer Remorse', 'Damaged Packaging']
    
    returns_df = pd.DataFrame({
        'ReturnID': [f"RET-{i:07d}" for i in range(1, len(returned_orders) + 1)],
        'OrderID': returned_orders['OrderID'].values,
        'ReturnDate': (pd.to_datetime(returned_orders['OrderDate']) + pd.to_timedelta(np.random.randint(2, 20, size=len(returned_orders)), unit='D')).dt.strftime('%Y-%m-%d'),
        'ProductID': returned_orders['ProductID'].values,
        'ReturnReason': np.random.choice(return_reasons, size=len(returned_orders), p=[0.35, 0.25, 0.15, 0.15, 0.10]),
        'RefundAmount': returned_orders['NetRevenue'].values,
        'RestockFee': np.round(returned_orders['NetRevenue'].values * 0.10, 2)
    })
    returns_df.to_csv(os.path.join(raw_dir, 'Returns.csv'), index=False)
    print(f" Returns generated: {len(returns_df)} rows")
    
    print("\n Raw Dataset Generation Complete! All tables saved to data/raw/")

if __name__ == '__main__':
    main()
