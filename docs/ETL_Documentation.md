# ETL & Data Transformation Documentation

## 1. Overview
The ETL pipeline processes raw transactional data into normalized, analytical-ready tables formatted for SQL loading and Power BI import.

## 2. Ingestion & Transformation Steps
1. **Deduplication**: Drops duplicate records on `OrderID`, `CustomerID`, and `ProductID`.
2. **Missing Value Imputation**:
   - `DiscountRate`: Imputed with `0.0` default.
   - `ShippingCost`: Imputed with median shipping cost by carrier.
3. **Outlier Capping**:
   - Shipping costs exceeding 99th percentile are capped at P99 ($48.00) to prevent distorted freight cost metrics.
4. **Feature Engineering**:
   - `ProfitMarginPct`: `(Profit / NetRevenue) * 100`.
   - `IsReturned`: Binary flag derived via left join with `Returns.csv`.
   - `IsPerfectOrder`: Binary indicator set to 1 if `IsLate == 0` AND `IsReturned == 0`.
5. **Quality Verification**:
   - Enforces referential integrity between Fact tables and Dimension tables.
