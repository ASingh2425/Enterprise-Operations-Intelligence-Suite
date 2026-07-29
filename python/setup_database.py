import os
import sqlite3
import pandas as pd

def build_database():
    print("============================================================================")
    print("Building Operations Intelligence Relational Database (SQLite Engine)...")
    print("============================================================================")
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    raw_dir = os.path.join(base_dir, 'data', 'raw')
    processed_dir = os.path.join(base_dir, 'data', 'processed')
    db_path = os.path.join(base_dir, 'data', 'ops_intelligence.db')
    
    if os.path.exists(db_path):
        os.remove(db_path)
        
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # 1. Load CSVs into SQLite Tables
    tables = {
        'DimCalendar': os.path.join(raw_dir, 'DimCalendar.csv'),
        'DimCustomers': os.path.join(raw_dir, 'Customers.csv'),
        'DimProducts': os.path.join(raw_dir, 'Products.csv'),
        'DimWarehouses': os.path.join(raw_dir, 'Warehouses.csv'),
        'DimSuppliers': os.path.join(raw_dir, 'Suppliers.csv'),
        'DimLogisticsCarriers': os.path.join(raw_dir, 'Logistics_Carriers.csv'),
        'FactInventory': os.path.join(raw_dir, 'Inventory.csv'),
        'FactOrders': os.path.join(processed_dir, 'Enriched_Orders.csv') if os.path.exists(os.path.join(processed_dir, 'Enriched_Orders.csv')) else os.path.join(raw_dir, 'Orders.csv'),
        'FactReturns': os.path.join(raw_dir, 'Returns.csv'),
        'FactForecastResults': os.path.join(processed_dir, 'Demand_Forecast_Results.csv') if os.path.exists(os.path.join(processed_dir, 'Demand_Forecast_Results.csv')) else None,
        'FactRFMSegments': os.path.join(processed_dir, 'Customer_RFM_Segments.csv') if os.path.exists(os.path.join(processed_dir, 'Customer_RFM_Segments.csv')) else None
    }
    
    for table_name, csv_path in tables.items():
        if csv_path and os.path.exists(csv_path):
            print(f" Loading {table_name} from {os.path.basename(csv_path)}...")
            df = pd.read_csv(csv_path)
            df.to_sql(table_name, conn, if_exists='replace', index=False)
            print(f"   [OK] Loaded {len(df):,} rows into table {table_name}")
            
    # 2. Create Performance Indexes
    print("\n Creating Performance Indexes...")
    indexes = [
        "CREATE INDEX idx_orders_orderdate ON FactOrders(OrderDate);",
        "CREATE INDEX idx_orders_customer ON FactOrders(CustomerID);",
        "CREATE INDEX idx_orders_product ON FactOrders(ProductID);",
        "CREATE INDEX idx_orders_warehouse ON FactOrders(WarehouseID);",
        "CREATE INDEX idx_orders_carrier ON FactOrders(CarrierID);",
        "CREATE INDEX idx_inventory_warehouse ON FactInventory(WarehouseID);"
    ]
    for idx_sql in indexes:
        cursor.execute(idx_sql)
    print("   [OK] Indexes created successfully.")
    
    # 3. Create Analytical Views
    print("\n Creating Business Intelligence Analytical Views...")
    views = {
        "vw_ExecutiveMonthlySummary": """
            CREATE VIEW vw_ExecutiveMonthlySummary AS
            SELECT 
                SUBSTR(OrderDate, 1, 7) AS MonthYear,
                COUNT(DISTINCT OrderID) AS TotalOrders,
                COUNT(DISTINCT CustomerID) AS ActiveCustomers,
                ROUND(SUM(NetRevenue), 2) AS TotalRevenue,
                ROUND(SUM(Profit), 2) AS TotalProfit,
                ROUND((SUM(Profit) / SUM(NetRevenue)) * 100, 2) AS ProfitMarginPct,
                ROUND(AVG(NetRevenue), 2) AS AvgOrderValue,
                ROUND((SUM(CASE WHEN IsLate = 1 THEN 1 ELSE 0 END) * 100.0 / COUNT(OrderID)), 2) AS LateDeliveryPct
            FROM FactOrders
            GROUP BY 1;
        """,
        "vw_WarehouseInventoryStatus": """
            CREATE VIEW vw_WarehouseInventoryStatus AS
            SELECT 
                w.WarehouseID,
                w.WarehouseName,
                w.City,
                w.Country,
                COUNT(i.ProductID) AS TotalSKUs,
                SUM(i.CurrentStock) AS TotalStockUnits,
                ROUND(SUM(i.CurrentStock * p.Cost), 2) AS TotalInventoryValue,
                SUM(CASE WHEN i.CurrentStock <= i.ReorderPoint THEN 1 ELSE 0 END) AS SKUsBelowReorderPoint
            FROM DimWarehouses w
            JOIN FactInventory i ON w.WarehouseID = i.WarehouseID
            JOIN DimProducts p ON i.ProductID = p.ProductID
            GROUP BY 1, 2, 3, 4;
        """
    }
    for view_name, view_sql in views.items():
        cursor.execute(f"DROP VIEW IF EXISTS {view_name};")
        cursor.execute(view_sql)
        print(f"   [OK] Created Analytical View: {view_name}")
        
    # 4. Execute Amazon BI Sample Business Query
    print("\n Executing Sample Amazon BI Query (Carrier Reliability & Shipping Efficiency)...")
    sample_query = """
        SELECT 
            c.CarrierName,
            COUNT(o.OrderID) AS TotalShipments,
            ROUND(SUM(o.ShippingCost), 2) AS TotalShippingCost,
            ROUND(AVG(o.ShippingCost), 2) AS AvgShippingCostPerOrder,
            ROUND(AVG(o.TransitDays), 2) AS AvgTransitDays,
            ROUND((SUM(CASE WHEN o.IsLate = 1 THEN 1 ELSE 0 END) * 100.0 / COUNT(o.OrderID)), 2) AS LatePct
        FROM FactOrders o
        JOIN DimLogisticsCarriers c ON o.CarrierID = c.CarrierID
        GROUP BY 1
        ORDER BY LatePct ASC;
    """
    df_result = pd.read_sql_query(sample_query, conn)
    print("\n--- Carrier SLA Performance Query Output ---")
    print(df_result.to_string(index=False))
    print("--------------------------------------------\n")
    
    conn.close()
    print(f" Database build complete! SQLite database created at: {db_path}")

if __name__ == '__main__':
    build_database()
