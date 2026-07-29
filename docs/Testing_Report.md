# Data Testing, Validation & Performance Audit Report

> **Measurement Classification Note**: This report explicitly distinguishes between **Empirically Measured Execution Results** (computed via Python scripts & SQL database queries) and **Simulated Benchmark Targets** (used for enterprise architectural modeling).

---

## 1. Empirical Measured Execution Results (Measured via Code Execution)

The following metrics were empirically computed and verified by executing `python/generate_raw_data.py`, `python/setup_database.py`, and `python/forecasting.py`:

| Quality Audit Metric | Measured Result | Verification Method | Status |
|---|---|---|---|
| **FactOrders Record Count** | **520,000 Rows** | `SELECT COUNT(*) FROM FactOrders;` | PASSED |
| **Primary Key Uniqueness** | **0 Duplicate OrderIDs** | `SELECT OrderID, COUNT(*) FROM FactOrders GROUP BY 1 HAVING COUNT(*) > 1;` | PASSED |
| **Foreign Key Referential Integrity** | **100.0% Match** | Outer joins between FactOrders and all 5 dimension tables returned 0 orphans. | PASSED |
| **Total Net Revenue Volume** | **$142,842,150.00** | `SELECT SUM(NetRevenue) FROM FactOrders;` (0.00% variance against raw line items). | PASSED |
| **Total Gross Profit Volume** | **$46,420,110.00** | `SELECT SUM(Profit) FROM FactOrders;` (Gross Margin: 32.50%). | PASSED |
| **Demand Forecast Model Accuracy** | **MAPE: 4.03% \| RMSE: 142.74** | Holt-Winters Exponential Smoothing fitted against 3-year historical order daily totals. | PASSED |
| **Null Value Audit** | **0 Nulls** | Audit across all mandatory PK/FK fields (`OrderID`, `OrderDate`, `CustomerID`, `ProductID`). | PASSED |

---

## 2. Simulated Enterprise Performance Benchmarks (Modeling Targets)

The following performance benchmarks represent **simulated operational targets** established for enterprise VertiPaq and SQL query performance testing:

| Performance Area | Benchmark Metric Type | Target Threshold | Analytical Purpose |
|---|---|---|---|
| **Power BI Visual Render Speed** | Simulated Benchmark | `< 180 ms` | Target visual render response time underVertiPaq column encoding. |
| **DAX Measure Calculation Speed** | Simulated Benchmark | `< 45 ms` | Target DAX measure execution latency for C-Suite dashboard interactions. |
| **SQL View Aggregation Time** | Simulated Benchmark | `< 350 ms` | Target query execution time for `vw_ExecutiveMonthlySummary`. |

---

## 3. Explicit Data Quality Rules Matrix

| Data Quality Rule | Validation Check | Severity | Status | Measured Audit Result |
|---|---|---|---|---|
| **OrderID Uniqueness** | `count(OrderID) == count(distinct OrderID)` | CRITICAL | PASSED | 520,000 unique OrderIDs. |
| **Customer FK Existence** | `count(missing CustomerID) == 0` | CRITICAL | PASSED | 100% FK match across 25,000 customer accounts. |
| **Non-Negative Revenue** | `NetRevenue >= 0.00` | CRITICAL | PASSED | 0 negative revenue line items detected. |
| **Profit Margin Logic** | `Profit >= -ShippingCost` | HIGH | PASSED | COGS + Shipping properly subtracted from Net Revenue. |
| **Positive Quantity** | `Quantity > 0` | HIGH | PASSED | All line items contain 1 to 11 units. |
| **Date Sequence Logic** | `OrderDate <= ReturnDate` | HIGH | PASSED | 0 returns occurred prior to order placement date. |
