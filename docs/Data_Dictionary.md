# Data Dictionary & Schema Documentation

## 1. Fact_Orders (`data/raw/Orders.csv`, `data/processed/Enriched_Orders.csv`)
| Column Name | Data Type | Description | Key Type |
|---|---|---|---|
| OrderID | VARCHAR(20) | Unique identifier for order line item | Primary Key |
| OrderDate | DATE | Date order was placed (YYYY-MM-DD) | FK to DimCalendar |
| CustomerID | VARCHAR(20) | Customer identifier | FK to DimCustomers |
| ProductID | VARCHAR(20) | Product identifier | FK to DimProducts |
| WarehouseID | VARCHAR(20) | Fulfillment center identifier | FK to DimWarehouses |
| CarrierID | VARCHAR(20) | Logistics carrier identifier | FK to DimLogisticsCarriers |
| Quantity | INT | Units purchased | - |
| UnitPrice | DECIMAL(10,2) | Selling price per unit | - |
| UnitCost | DECIMAL(10,2) | Cost price per unit | - |
| DiscountRate | DECIMAL(4,2) | Applied percentage discount | - |
| GrossRevenue | DECIMAL(12,2) | Quantity * UnitPrice | Derived |
| NetRevenue | DECIMAL(12,2) | GrossRevenue * (1 - DiscountRate) | Derived |
| COGS | DECIMAL(12,2) | Quantity * UnitCost | Derived |
| ShippingCost | DECIMAL(10,2) | Freight shipping cost charged | - |
| Profit | DECIMAL(12,2) | NetRevenue - COGS - ShippingCost | Derived |
| TransitDays | INT | Actual transit time in days | - |
| PromisedDays | INT | SLA promised delivery days | - |
| IsLate | INT | Binary flag (1 if TransitDays > PromisedDays) | Derived |

## 2. DimCustomers (`Customers.csv`)
| Column Name | Data Type | Description | Key Type |
|---|---|---|---|
| CustomerID | VARCHAR(20) | Unique customer ID | Primary Key |
| Segment | VARCHAR(30) | Consumer / Corporate / Home Office | - |
| Region | VARCHAR(30) | North America / Europe / APAC | - |
| Country | VARCHAR(50) | Country of residence | - |
| City | VARCHAR(50) | Primary city | - |
| LifetimeValue| DECIMAL(12,2)| Modeled customer lifetime value ($) | - |

## 3. DimProducts (`Products.csv`)
| Column Name | Data Type | Description | Key Type |
|---|---|---|---|
| ProductID | VARCHAR(20) | Unique product catalog ID | Primary Key |
| SKU | VARCHAR(50) | Stock keeping unit code | Alternate Key |
| Category | VARCHAR(50) | Technology, Furniture, Office Supplies, Logistics | - |
| SubCategory | VARCHAR(50) | Detailed item sub-category | - |
| Brand | VARCHAR(50) | Product brand name | - |
| Cost | DECIMAL(10,2) | Cost price per unit | - |
| SellingPrice | DECIMAL(10,2) | Retail selling price | - |
| Margin | DECIMAL(5,4) | Standard margin percentage | Derived |
