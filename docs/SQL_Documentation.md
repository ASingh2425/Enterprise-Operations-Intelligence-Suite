# SQL Database Schema & Optimization Documentation

## 1. Relational Database Design
The SQL database is built on a Star Schema layout consisting of 1 central transaction fact table (`FactOrders`), 1 sub-fact table (`FactReturns`), 1 snapshot table (`FactInventory`), and 5 dimension tables (`DimCalendar`, `DimCustomers`, `DimProducts`, `DimWarehouses`, `DimSuppliers`, `DimLogisticsCarriers`).

## 2. DDL Scripts Summary
- `schema.sql`: Sets up schema `ops_intelligence`.
- `create_tables.sql`: DDL specifying data types, primary keys, and non-null constraints.
- `constraints.sql`: Foreign keys connecting facts to dimensions.
- `indexes.sql`: B-tree indexes created on all join keys (`OrderDate`, `CustomerID`, `ProductID`, `WarehouseID`, `CarrierID`).
- `views.sql`: Pre-built analytical views (`vw_ExecutiveMonthlySummary`, `vw_WarehouseInventoryStatus`, `vw_SupplierPerformanceScorecard`).
- `business_queries.sql`: Amazon BI analyst queries leveraging window functions (`DENSE_RANK() OVER (...)`), aggregation rollups, and CTEs.
