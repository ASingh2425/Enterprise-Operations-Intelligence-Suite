# Data Model Architecture & Semantic Layer Specification

## 1. Star Schema Topology & Diagram
The data model strictly implements a **Star Schema** pattern optimized for VertiPaq column store dictionary encoding and fast DAX measures.

```
                        +----------------------+
                        |     DimCalendar      |
                        +----------------------+
                                   | (1)
                                   |
                                   | (*)
+-------------------+      +-------------------+      +-------------------+
|   DimCustomers    |------|    FactOrders     |------|    DimProducts    |
+-------------------+ (1)(*)+-------------------+(*)(1)+-------------------+
                           | (*)           | (*)
                       (1) |           (1) |
      +--------------------+               +-----------------------+
      |   DimWarehouses    |               | DimLogisticsCarriers  |
      +--------------------+               +-----------------------+
```

---

## 2. Fact Table Grain Declarations

Defining explicit table grains prevents double-counting metrics and ensures correct aggregation logic across all Power BI visuals and SQL queries:

### 2.1 FactOrders
- **Declared Grain**: **One row represents one product line item within a customer order.**
- **Primary Key**: `OrderID`
- **Fact Metrics**: `Quantity`, `UnitPrice`, `UnitCost`, `GrossRevenue`, `NetRevenue`, `COGS`, `ShippingCost`, `Profit`.

### 2.2 FactInventory
- **Declared Grain**: **One row represents one product SKU at one warehouse for one monthly snapshot.**
- **Primary Key**: Composite (`WarehouseID` + `ProductID`)
- **Fact Metrics**: `CurrentStock`, `ReorderPoint`, `UnitHoldingCost`, `StockoutRiskScore`, `EOQ`, `SafetyStock`, `DaysOfInventory`.

### 2.3 FactReturns
- **Declared Grain**: **One row represents one returned order line item.**
- **Primary Key**: `ReturnID`
- **Fact Metrics**: `RefundAmount`, `RestockFee`.

### 2.4 FactOperationalAnomalies
- **Declared Grain**: **One row represents one statistical anomaly incident.**
- **Primary Key**: `AnomalyID`
- **Fact Metrics**: `ZScore`, `SeverityLevel`.

---

## 3. Relationship Specifications & Cardinality

| Parent Table (1) | Primary Key | Child Table (*) | Foreign Key | Cardinality | Cross Filter Direction |
|---|---|---|---|---|---|
| `DimCalendar` | `FullDate` | `FactOrders` | `OrderDate` | 1 to Many (1:*) | Single Direction |
| `DimCustomers` | `CustomerID` | `FactOrders` | `CustomerID` | 1 to Many (1:*) | Single Direction |
| `DimProducts` | `ProductID` | `FactOrders` | `ProductID` | 1 to Many (1:*) | Single Direction |
| `DimWarehouses` | `WarehouseID` | `FactOrders` | `WarehouseID` | 1 to Many (1:*) | Single Direction |
| `DimLogisticsCarriers`| `CarrierID` | `FactOrders` | `CarrierID` | 1 to Many (1:*) | Single Direction |
| `DimWarehouses` | `WarehouseID` | `FactInventory` | `WarehouseID` | 1 to Many (1:*) | Single Direction |
| `DimProducts` | `ProductID` | `FactInventory` | `ProductID` | 1 to Many (1:*) | Single Direction |
| `FactOrders` | `OrderID` | `FactReturns` | `OrderID` | 1 to Many (1:*) | Both Directions (Drillthrough) |

---

## 4. VertiPaq Storage Engine Optimizations

1. **Single-Direction Relationship Enforcement**: All dimension-to-fact relationships use single-direction filtering to eliminate bidirectional ambiguity and maximizeVertiPaq scan speed.
2. **Surrogate Key Joins**: Integer surrogate keys (`DateKey`) used for temporal joins.
3. **Column Encoding Tuning**: High-cardinality floating-point measures rounded to 2 decimal places to minimize dictionary bit-width.
4. **Auto Date/Time Disabled**: Native Power BI auto date-table generation disabled globally.
