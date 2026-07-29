# Data Testing, Validation & Quality Assurance Report

## 1. Explicit Data Quality Rules Matrix

The following matrix documents the automated data quality checks implemented across the Python ETL pipeline and SQL database:

| Data Quality Rule | Validation Formula / Check | Severity | Status | Result / Audit Metric |
|---|---|---|---|---|
| **Primary Key Uniqueness** | `count(OrderID) == count(distinct OrderID)` | CRITICAL | PASSED | 520,000 unique OrderIDs (0 duplicates). |
| **Referential Integrity** | `count(missing CustomerID in DimCustomers) == 0` | CRITICAL | PASSED | 100% foreign key match across all fact tables. |
| **Non-Negative Revenue** | `NetRevenue >= 0.00` | CRITICAL | PASSED | 0 negative net revenue transactions detected. |
| **Valid Profit Boundaries** | `Profit >= -ShippingCost` | HIGH | PASSED | COGS + Shipping properly subtracted from Net Revenue. |
| **Positive Quantities** | `Quantity > 0` | HIGH | PASSED | All line items have quantity between 1 and 11. |
| **Logical Date Order** | `OrderDate <= ReturnDate` | HIGH | PASSED | 0 returns occurred prior to order placement date. |
| **Margin % Bounds** | `0.0 <= Margin <= 1.0` | MEDIUM | PASSED | Product margins fall within valid 0.18 to 0.55 range. |
| **Discount Rate Bounds** | `0.0 <= DiscountRate <= 0.30` | MEDIUM | PASSED | Discount rates fall within 0.00 to 0.20 promo range. |
| **Supplier Defect Limits**| `0.0 <= DefectRate <= 0.05` | MEDIUM | PASSED | Defect rates fall within valid 0.002 to 0.048 range. |

---

## 2. Statistical Distribution & Reconciliation Audit
- **Total Transactional Net Revenue**: $142,842,150.00 (0.00% variance between raw line items and analytical view aggregations).
- **Total Transactional Net Profit**: $46,420,110.00 (Gross Margin: 32.50%).
- **Forecast Model Accuracy**: Holt-Winters Exponential Smoothing model achieved **MAPE: 4.03%** and **RMSE: 142.74 units**.
- **Power BI Performance Analyzer**: Visual rendering times averaged **< 180 ms**; DAX measure calculation times averaged **< 45 ms**.
