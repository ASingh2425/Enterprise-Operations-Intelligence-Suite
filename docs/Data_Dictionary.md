# Data Dictionary & Schema Specification

## 1. Relational Entities Summary
The database consists of 8 primary tables structured in a normalized Star Schema:
- **Fact Tables**: `FactOrders`, `FactReturns`, `FactInventory`
- **Dimension Tables**: `DimCalendar`, `DimCustomers`, `DimProducts`, `DimWarehouses`, `DimSuppliers`, `DimLogisticsCarriers`

---

## 2. Comprehensive Field Specifications

### 2.1 Fact_Orders (`data/raw/Orders.csv`, `data/processed/Enriched_Orders.csv`)
| Field Name | Physical Type | Key Type | Nullable | Example Value | Business Description |
|---|---|---|---|---|---|
| `OrderID` | VARCHAR(20) | Primary Key | NO | `ORD-00000001` | Unique transaction line identifier |
| `OrderDate` | DATE | FK to DimCalendar | NO | `2025-06-15` | Date order was placed |
| `CustomerID` | VARCHAR(20) | FK to DimCustomers | NO | `CUST-000142` | Customer ID |
| `ProductID` | VARCHAR(20) | FK to DimProducts | NO | `PROD-0004` | Product catalog item ID |
| `WarehouseID` | VARCHAR(20) | FK to DimWarehouses | NO | `WH-US-WEST` | Fulfillment center origin |
| `CarrierID` | VARCHAR(20) | FK to DimLogisticsCarriers | NO | `CAR-01` | Logistics carrier assigned |
| `Quantity` | INT | None | NO | `4` | Units ordered |
| `UnitPrice` | DECIMAL(10,2) | None | NO | `249.99` | Retail price per unit ($) |
| `UnitCost` | DECIMAL(10,2) | None | NO | `120.00` | Manufacturing/acquisition cost ($) |
| `DiscountRate`| DECIMAL(4,2) | None | NO | `0.10` | Applied promotional discount % |
| `GrossRevenue`| DECIMAL(12,2) | Derived | NO | `999.96` | `Quantity * UnitPrice` |
| `NetRevenue` | DECIMAL(12,2) | Derived | NO | `899.96` | `GrossRevenue * (1 - DiscountRate)` |
| `COGS` | DECIMAL(12,2) | Derived | NO | `480.00` | `Quantity * UnitCost` |
| `ShippingCost`| DECIMAL(10,2) | None | NO | `18.50` | Freight shipping fee charged ($) |
| `Profit` | DECIMAL(12,2) | Derived | NO | `401.46` | `NetRevenue - COGS - ShippingCost` |
| `TransitDays` | INT | None | NO | `4` | Actual transit delivery days |
| `PromisedDays`| INT | None | NO | `3` | SLA promised delivery days |
| `IsLate` | INT | Derived | NO | `1` | Binary flag (1 if `TransitDays > PromisedDays`) |
| `IsReturned` | INT | Derived | NO | `0` | Binary flag (1 if returned in `FactReturns`) |
| `IsPerfectOrder`| INT | Derived | NO | `0` | Binary flag (1 if `IsLate == 0` AND `IsReturned == 0`) |

### 2.2 DimCustomers (`Customers.csv`)
| Field Name | Physical Type | Key Type | Nullable | Example Value | Business Description |
|---|---|---|---|---|---|
| `CustomerID` | VARCHAR(20) | Primary Key | NO | `CUST-000142` | Unique customer ID |
| `Segment` | VARCHAR(30) | None | NO | `Corporate` | Customer segment (Consumer/Corporate/Home Office) |
| `Region` | VARCHAR(30) | None | NO | `North America` | Global geographic region |
| `Country` | VARCHAR(50) | None | NO | `United States` | Country of primary address |
| `City` | VARCHAR(50) | None | NO | `Seattle` | City of primary address |
| `LifetimeValue`| DECIMAL(12,2)| None | NO | `3420.50` | Modeled customer lifetime value ($) |

### 2.3 DimProducts (`Products.csv`)
| Field Name | Physical Type | Key Type | Nullable | Example Value | Business Description |
|---|---|---|---|---|---|
| `ProductID` | VARCHAR(20) | Primary Key | NO | `PROD-0004` | Unique product identifier |
| `SKU` | VARCHAR(50) | Alternate Key | NO | `SKU-TEC-LAP-0004` | Stock keeping unit code |
| `Category` | VARCHAR(50) | None | NO | `Technology` | Top-level catalog category |
| `SubCategory` | VARCHAR(50) | None | NO | `Laptops` | Catalog sub-category |
| `Brand` | VARCHAR(50) | None | NO | `ApexCorp` | Product brand name |
| `Cost` | DECIMAL(10,2) | None | NO | `450.00` | Cost price per unit ($) |
| `SellingPrice`| DECIMAL(10,2) | None | NO | `850.00` | Standard selling price ($) |
| `Margin` | DECIMAL(5,4) | Derived | NO | `0.4706` | `(SellingPrice - Cost) / SellingPrice` |

### 2.4 DimWarehouses (`Warehouses.csv`)
| Field Name | Physical Type | Key Type | Nullable | Example Value | Business Description |
|---|---|---|---|---|---|
| `WarehouseID` | VARCHAR(20) | Primary Key | NO | `WH-US-WEST` | Unique warehouse code |
| `WarehouseName`| VARCHAR(100)| None | NO | `Seattle Hub` | Fulfillment center name |
| `City` | VARCHAR(50) | None | NO | `Seattle` | Facility city |
| `Country` | VARCHAR(50) | None | NO | `United States` | Facility country |
| `CapacityUnits`| INT | None | NO | `750000` | Maximum unit holding capacity |
| `OperatingCost`| DECIMAL(12,2)| None | NO | `180000.00` | Monthly operating overhead ($) |
