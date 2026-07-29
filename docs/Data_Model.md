# Data Model Architecture & Relationship Specification

## 1. Star Schema Topology
The data model strictly implements a **Star Schema** pattern optimized for VertiPaq column store compression and high-throughput DAX evaluation.

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

## 2. Table Relationship Specs & Cardinality

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

## 3. VertiPaq Engine Optimization Rules
- **Single-Direction Filtering**: All dimension-to-fact relationships enforce single-direction filtering to preserve VertiPaq scan efficiency and prevent circular relationship paths.
- **Surrogate Keys**: Foreign key joins utilize numeric integer keys where feasible (`DateKey`) to minimize hash dictionary lookup memory.
- **Hierarchy Disable**: Native auto date-table creation is disabled globally to eliminate hidden metadata tables.
