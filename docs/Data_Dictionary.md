# Complete Enterprise Data Dictionary & Data Catalog

## 1. Data Dictionary Overview & Entity Relationship Index
This dictionary provides a complete data catalog across all **10 relational tables** in the Operations Intelligence Suite.

### Tables Index
1. `DimCalendar`: Date dimension table.
2. `DimCustomers`: Customer master records.
3. `DimProducts`: Product SKU catalog.
4. `DimWarehouses`: Regional fulfillment centers.
5. `DimSuppliers`: Vendor scorecards and master records.
6. `DimLogisticsCarriers`: Transportation freight carriers.
7. `FactOrders`: Central order transaction line items.
8. `FactInventory`: Periodic warehouse stock snapshots.
9. `FactReturns`: Returned order lines and refund payouts.
10. `FactOperationalAnomalies`: Machine learning anomaly alerts log.

---

## 2. Table Specifications & Column Catalog

### 2.1 DimCalendar
- **Description**: Standard business calendar table supporting time-intelligence calculations.
- **Source**: System Generated (`python/generate_raw_data.py`).
- **Primary Key**: `DateKey`

| Column Name | Physical Type | Key Type | Nullable | Allowed / Sample Values | Constraints | Source | Business Description |
|---|---|---|---|---|---|---|---|
| `DateKey` | INT | Primary Key | NO | `20250615` | Unique YYYYMMDD integer | Generated | Integer surrogate key for fast table joins. |
| `FullDate` | DATE | Alternate Key | NO | `2025-06-15` | `2023-01-01` to `2025-12-31` | Generated | ISO standard calendar date. |
| `Year` | INT | Attribute | NO | `2025` | `2023`, `2024`, `2025` | Derived | Calendar year. |
| `Quarter` | VARCHAR(5) | Attribute | NO | `Q2` | `Q1`, `Q2`, `Q3`, `Q4` | Derived | Fiscal calendar quarter indicator. |
| `MonthNumber` | INT | Attribute | NO | `6` | `1` to `12` | Derived | Numerical month index. |
| `MonthName` | VARCHAR(15) | Attribute | NO | `June` | `January` to `December` | Derived | Full English month name. |
| `DayOfWeek` | VARCHAR(15) | Attribute | NO | `Sunday` | `Monday` to `Sunday` | Derived | Day name of the week. |
| `IsWeekend` | INT | Flag | NO | `1` | `0` (Weekday), `1` (Weekend) | Derived | Binary weekend indicator. |
| `IsHoliday` | INT | Flag | NO | `0` | `0` (No), `1` (Yes) | Derived | Enterprise holiday flag. |

---

### 2.2 DimCustomers
- **Description**: Customer master table containing customer demographic and segment attributes.
- **Source**: System Generated (`python/generate_raw_data.py`).
- **Primary Key**: `CustomerID`

| Column Name | Physical Type | Key Type | Nullable | Allowed / Sample Values | Constraints | Source | Business Description |
|---|---|---|---|---|---|---|---|
| `CustomerID` | VARCHAR(20) | Primary Key | NO | `CUST-000142` | Unique `CUST-XXXXXX` | Generated | Unique customer account identifier. |
| `Segment` | VARCHAR(30) | Attribute | NO | `Corporate` | `Consumer`, `Corporate`, `Home Office` | Generated | Customer market classification tier. |
| `Region` | VARCHAR(30) | Attribute | NO | `North America` | `North America`, `Europe`, `APAC` | Generated | Macro-geographic sales region. |
| `Country` | VARCHAR(50) | Attribute | NO | `United States` | 7 valid countries | Generated | Country of customer address. |
| `City` | VARCHAR(50) | Attribute | NO | `Seattle` | 28 valid cities | Generated | City of customer primary location. |
| `LifetimeValue` | DECIMAL(12,2) | Metric | NO | `3420.50` | `> 0.00` | Calculated | Modeled historical customer lifetime spend ($). |

---

### 2.3 DimProducts
- **Description**: Master product catalog containing SKU specifications, costs, and selling prices.
- **Source**: System Generated (`python/generate_raw_data.py`).
- **Primary Key**: `ProductID`

| Column Name | Physical Type | Key Type | Nullable | Allowed / Sample Values | Constraints | Source | Business Description |
|---|---|---|---|---|---|---|---|
| `ProductID` | VARCHAR(20) | Primary Key | NO | `PROD-0004` | Unique `PROD-XXXX` | Generated | Internal catalog product ID. |
| `SKU` | VARCHAR(50) | Alternate Key | NO | `SKU-TEC-LAP-0004` | Unique SKU string | Generated | Stock keeping unit code. |
| `Category` | VARCHAR(50) | Attribute | NO | `Technology` | 4 main categories | Generated | Top-level product category. |
| `SubCategory` | VARCHAR(50) | Attribute | NO | `Laptops` | 20 sub-categories | Generated | Detailed merchandise category. |
| `Brand` | VARCHAR(50) | Attribute | NO | `ApexCorp` | 8 active brands | Generated | Manufacturer brand name. |
| `Cost` | DECIMAL(10,2) | Attribute | NO | `450.00` | `$8.00` to `$950.00` | Generated | Unit cost price ($). |
| `SellingPrice` | DECIMAL(10,2) | Attribute | NO | `850.00` | `> Cost` | Calculated | Retail selling price ($). |
| `Margin` | DECIMAL(5,4) | Metric | NO | `0.4706` | `0.18` to `0.55` | Calculated | Standard profit margin %. |

---

### 2.4 DimWarehouses
- **Description**: Regional fulfillment center master database.
- **Source**: System Generated (`python/generate_raw_data.py`).
- **Primary Key**: `WarehouseID`

| Column Name | Physical Type | Key Type | Nullable | Allowed / Sample Values | Constraints | Source | Business Description |
|---|---|---|---|---|---|---|---|
| `WarehouseID` | VARCHAR(20) | Primary Key | NO | `WH-US-WEST-1` | Unique WH code | Generated | Fulfillment center ID. |
| `WarehouseName` | VARCHAR(100) | Attribute | NO | `Seattle Mega Hub` | 15 facility names | Generated | Descriptive facility name. |
| `City` | VARCHAR(50) | Attribute | NO | `Seattle` | Facility city | Generated | Physical location city. |
| `Country` | VARCHAR(50) | Attribute | NO | `United States` | Facility country | Generated | Physical location country. |
| `Region` | VARCHAR(30) | Attribute | NO | `North America` | `North America`, `Europe`, `APAC` | Generated | Macro region assignment. |
| `CapacityUnits` | INT | Capacity | NO | `950000` | `350,000` to `950,000` | Generated | Maximum unit storage capacity. |
| `OperatingCost` | DECIMAL(12,2) | Metric | NO | `220000.00` | `$95,000` to `$220,000` | Generated | Monthly operational overhead ($). |

---

### 2.5 DimSuppliers
- **Description**: Vendor scorecards and supplier master profiles.
- **Source**: System Generated (`python/generate_raw_data.py`).
- **Primary Key**: `SupplierID`

| Column Name | Physical Type | Key Type | Nullable | Allowed / Sample Values | Constraints | Source | Business Description |
|---|---|---|---|---|---|---|---|
| `SupplierID` | VARCHAR(20) | Primary Key | NO | `SUP-014` | Unique `SUP-XXX` | Generated | Unique vendor identifier. |
| `SupplierName` | VARCHAR(100) | Attribute | NO | `Global Supplier 14 (Germany)` | 120 supplier names | Generated | Full supplier company name. |
| `Country` | VARCHAR(50) | Attribute | NO | `Germany` | 10 country origins | Generated | Country of origin. |
| `Rating` | DECIMAL(3,2) | Metric | NO | `4.25` | `1.00` to `5.00` | Generated | Quality rating score (5.0 scale). |
| `AvgDeliveryDays`| DECIMAL(4,1) | Metric | NO | `14.5` | `3.0` to `24.0` | Generated | Average procurement lead time. |
| `DefectRate` | DECIMAL(5,4) | Metric | NO | `0.0125` | `0.002` to `0.048` | Generated | Historical defect percentage. |
| `SupplierRiskIndex`| DECIMAL(6,2)| Metric | NO | `24.50` | Derived score | Calculated | Multi-criteria vendor risk score. |

---

### 2.6 DimLogisticsCarriers
- **Description**: Master table of transportation and freight shipping carriers.
- **Source**: System Generated (`python/generate_raw_data.py`).
- **Primary Key**: `CarrierID`

| Column Name | Physical Type | Key Type | Nullable | Allowed / Sample Values | Constraints | Source | Business Description |
|---|---|---|---|---|---|---|---|
| `CarrierID` | VARCHAR(20) | Primary Key | NO | `CAR-01` | Unique `CAR-XX` | Generated | Carrier ID. |
| `CarrierName` | VARCHAR(100) | Attribute | NO | `Amazon Air Logistics` | 8 carrier names | Generated | Freight logistics provider name. |
| `ReliabilityScore`| DECIMAL(3,2)| Metric | NO | `0.96` | `0.85` to `0.99` | Generated | On-time delivery SLA score. |
| `BaseRatePerKm` | DECIMAL(6,2) | Metric | NO | `0.45` | `$0.35` to `$0.52` | Generated | Base freight rate ($ / km). |

---

### 2.7 FactOrders
- **Description**: Central order fulfillment transaction table.
- **Fact Table Grain**: **One row represents one product line item within a customer order.**
- **Source**: System Generated (`python/generate_raw_data.py`) & Cleaned via ETL.
- **Primary Key**: `OrderID`

| Column Name | Physical Type | Key Type | Nullable | Allowed / Sample Values | Constraints | Source | Business Description |
|---|---|---|---|---|---|---|---|
| `OrderID` | VARCHAR(20) | Primary Key | NO | `ORD-00042180` | Unique `ORD-XXXXXXXX` | Generated | Order transaction line ID. |
| `OrderDate` | DATE | FK to DimCalendar | NO | `2025-06-15` | Valid calendar date | Generated | Order creation date. |
| `CustomerID` | VARCHAR(20) | FK to DimCustomers | NO | `CUST-000142` | Existing CustomerID | Generated | Customer purchasing account. |
| `ProductID` | VARCHAR(20) | FK to DimProducts | NO | `PROD-0004` | Existing ProductID | Generated | Catalog product purchased. |
| `WarehouseID` | VARCHAR(20) | FK to DimWarehouses | NO | `WH-US-WEST-1` | Existing WarehouseID | Generated | Fulfillment origin warehouse. |
| `CarrierID` | VARCHAR(20) | FK to DimCarriers | NO | `CAR-01` | Existing CarrierID | Generated | Transportation carrier. |
| `Quantity` | INT | Metric | NO | `4` | `1` to `11` | Generated | Units ordered in line item. |
| `UnitPrice` | DECIMAL(10,2) | Metric | NO | `249.99` | `> 0.00` | Generated | Unit selling price ($). |
| `UnitCost` | DECIMAL(10,2) | Metric | NO | `120.00` | `> 0.00` | Generated | Unit cost price ($). |
| `DiscountRate` | DECIMAL(4,2) | Metric | NO | `0.10` | `0.00` to `0.20` | Generated | Promotional discount rate. |
| `GrossRevenue` | DECIMAL(12,2) | Metric | NO | `999.96` | `Quantity * UnitPrice` | Calculated | Total gross revenue ($). |
| `NetRevenue` | DECIMAL(12,2) | Metric | NO | `899.96` | `GrossRevenue * (1 - Discount)` | Calculated | Net revenue after discount ($). |
| `COGS` | DECIMAL(12,2) | Metric | NO | `480.00` | `Quantity * UnitCost` | Calculated | Cost of Goods Sold ($). |
| `ShippingCost` | DECIMAL(10,2) | Metric | NO | `18.50` | `$4.50` to `$48.00` (Capped) | Calculated | Freight shipping cost ($). |
| `Profit` | DECIMAL(12,2) | Metric | NO | `401.46` | `NetRevenue - COGS - Shipping` | Calculated | Net profit line value ($). |
| `TransitDays` | INT | Metric | NO | `4` | `1` to `8` | Generated | Actual transit days. |
| `PromisedDays` | INT | Metric | NO | `3` | `1` to `8` | Generated | SLA promised delivery days. |
| `IsLate` | INT | Flag | NO | `1` | `1` if `TransitDays > Promised` | Calculated | Binary late delivery flag. |
| `IsReturned` | INT | Flag | NO | `0` | `1` if in FactReturns | Calculated | Binary return status flag. |
| `IsPerfectOrder`| INT | Flag | NO | `0` | `1` if Not Late & Not Returned | Calculated | Perfect order indicator. |

---

### 2.8 FactInventory
- **Description**: Monthly warehouse inventory stock snapshot table.
- **Fact Table Grain**: **One row represents one product SKU at one warehouse for one monthly snapshot.**
- **Source**: System Generated (`python/inventory_analysis.py`).
- **Primary Key**: `InventoryID` (Composite `WarehouseID` + `ProductID`)

| Column Name | Physical Type | Key Type | Nullable | Allowed / Sample Values | Constraints | Source | Business Description |
|---|---|---|---|---|---|---|---|
| `WarehouseID` | VARCHAR(20) | FK to DimWarehouses | NO | `WH-US-WEST-1` | Existing WarehouseID | Generated | Warehouse location. |
| `ProductID` | VARCHAR(20) | FK to DimProducts | NO | `PROD-0004` | Existing ProductID | Generated | Product SKU held. |
| `SKU` | VARCHAR(50) | Attribute | NO | `SKU-TEC-LAP-0004` | Matching SKU | Generated | Product SKU string. |
| `CurrentStock` | INT | Metric | NO | `1420` | `40` to `3,500` | Generated | On-hand physical stock units. |
| `ReorderPoint` | INT | Metric | NO | `450` | `150` to `750` | Calculated | Minimum reorder stock trigger. |
| `LeadTimeDays` | INT | Metric | NO | `12` | `3` to `25` | Generated | Supplier replenishment lead time. |
| `UnitHoldingCost`| DECIMAL(8,2) | Metric | NO | `21.60` | `Cost * 0.18` | Calculated | Annual unit holding cost ($). |
| `StockoutRiskScore`| DECIMAL(5,3)| Metric | NO | `0.180` | `0.000` to `1.000` | Calculated | Stockout probability score. |
| `EOQ` | INT | Metric | NO | `350` | Formula calculated | Calculated | Economic Order Quantity batch. |
| `SafetyStock` | INT | Metric | NO | `120` | Formula calculated | Calculated | Required safety stock buffer. |
| `DaysOfInventory`| DECIMAL(8,1)| Metric | NO | `42.5` | `DOI = StockVal / DailyCOGS` | Calculated | Days of Inventory on hand. |

---

### 2.9 FactReturns
- **Description**: Log of returned order lines, return reasons, and refund payouts.
- **Fact Table Grain**: **One row represents one returned order line item.**
- **Source**: System Generated (`python/generate_raw_data.py`).
- **Primary Key**: `ReturnID`

| Column Name | Physical Type | Key Type | Nullable | Allowed / Sample Values | Constraints | Source | Business Description |
|---|---|---|---|---|---|---|---|
| `ReturnID` | VARCHAR(20) | Primary Key | NO | `RET-0000412` | Unique `RET-XXXXXXX` | Generated | Unique return transaction ID. |
| `OrderID` | VARCHAR(20) | FK to FactOrders | NO | `ORD-00042180` | Existing OrderID | Generated | Returned original order ID. |
| `ReturnDate` | DATE | FK to DimCalendar | NO | `2025-06-22` | `ReturnDate > OrderDate` | Generated | Processing date of return. |
| `ProductID` | VARCHAR(20) | FK to DimProducts | NO | `PROD-0004` | Existing ProductID | Generated | Returned product catalog ID. |
| `ReturnReason` | VARCHAR(50) | Attribute | NO | `Defective Product` | 5 valid reasons | Generated | Primary return reason category. |
| `RefundAmount` | DECIMAL(12,2) | Metric | NO | `899.96` | Equal to Order NetRevenue | Generated | Total refund money paid ($). |
| `RestockFee` | DECIMAL(10,2) | Metric | NO | `89.99` | `RefundAmount * 0.10` | Calculated | Warehouse restocking fee ($). |

---

### 2.10 FactOperationalAnomalies
- **Description**: Output table storing detected shipping cost and profit margin compression outliers.
- **Source**: Python Anomaly Engine (`python/anomaly_detection.py`).
- **Primary Key**: `AnomalyID`

| Column Name | Physical Type | Key Type | Nullable | Allowed / Sample Values | Constraints | Source | Business Description |
|---|---|---|---|---|---|---|---|
| `AnomalyID` | INT | Primary Key | NO | `142` | Auto-increment ID | Calculated | Unique anomaly incident ID. |
| `OrderID` | VARCHAR(20) | FK to FactOrders | NO | `ORD-00042180` | Existing OrderID | Calculated | Flagged transaction ID. |
| `AnomalyType` | VARCHAR(50) | Attribute | NO | `Shipping Freight Spike` | Valid type string | Calculated | Outlier incident category. |
| `ZScore` | DECIMAL(5,2) | Metric | NO | `3.42` | `|Z| > 3.0` | Calculated | Statistical Z-score deviation. |
| `SeverityLevel`| VARCHAR(20) | Attribute | NO | `CRITICAL` | `CRITICAL`, `HIGH`, `MEDIUM` | Calculated | Risk priority level. |
