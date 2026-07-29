# 📚 Data References, Mathematical Formulas & Code Lineage Catalog

> **Enterprise Operations Intelligence Suite**  
> *Complete Lineage Mapping Connecting Every Metric, Graph, Insight, and Recommendation to its Source Code, SQL View, DAX Measure, and Mathematical Formula.*

---

## 1. Summary of Data Lineage & Reference Architecture

Every number, KPI card, visual graph, and narrative recommendation displayed across the 10 dashboard pages is **100% reproducible** and directly linked to an underlying Python script, SQL query/view, DAX measure, or statistical algorithm:

```text
[ Raw Data Seed (np.random.seed(42)) ] ──► python/generate_raw_data.py
                                                      │
                                                      ▼
[ Mathematical & ML Pipeline ] ────────► python/feature_engineering.py
                                          python/forecasting.py
                                          python/customer_segmentation.py
                                          python/inventory_analysis.py
                                          python/anomaly_detection.py
                                                      │
                                                      ▼
[ SQL Relational Database Engine ] ─────► python/setup_database.py (data/ops_intelligence.db)
                                          sql/views.sql (vw_ExecutiveMonthlySummary)
                                                      │
                                                      ▼
[ Power BI DAX & Web UI Canvas ] ──────► docs/DAX_Measures.md
                                          app.js (Chart.js Engine)
```

---

## 2. Complete Metric-to-Source Lineage Reference Table

| Dashboard Metric / Number | Displayed Value | Mathematical Formula / Algorithm | Exact Python File & Code Line | SQL Table / Column Source | DAX Measure Reference |
|---|---|---|---|---|---|
| **Net Revenue** | **$142.84M** | $\sum (\text{GrossRevenue} - \text{Discounts})$ | `feature_engineering.py` (Line 16) | `FactOrders.NetRevenue` | `[Total Net Revenue]` |
| **Gross Profit** | **$46.42M** | $\sum (\text{NetRevenue} - \text{COGS} - \text{Shipping})$ | `generate_raw_data.py` (Line 173) | `FactOrders.Profit` | `[Total Gross Profit]` |
| **Gross Margin %** | **32.50%** | $\frac{\text{Gross Profit}}{\text{Net Revenue}} \times 100$ | `feature_engineering.py` (Line 16) | `vw_ExecutiveMonthlySummary.ProfitMarginPct` | `[Gross Margin %]` |
| **Total Order Lines** | **520,000** | $\text{COUNT}(\text{OrderID})$ | `generate_raw_data.py` (Line 146) | `FactOrders.OrderID` | `[Total Orders]` |
| **Perfect Order Rate** | **94.8%** | $\frac{\text{On-Time \& Non-Returned}}{\text{Total Orders}} \times 100$ | `feature_engineering.py` (Line 20) | `FactOrders.IsPerfectOrder` | `[Perfect Order Rate %]` |
| **Return Rate %** | **4.80%** | $\frac{\text{Returned Orders}}{\text{Total Orders}} \times 100$ | `generate_raw_data.py` (Line 189) | `FactReturns.ReturnID` | `[Return Rate %]` |
| **On-Time Delivery %** | **96.2%** | $\frac{\text{TransitDays} \le \text{PromisedDays}}{\text{Total Orders}} \times 100$ | `feature_engineering.py` (Line 23) | `FactOrders.IsLate` | `[On-Time Delivery %]` |
| **Forecast Accuracy (MAPE)**| **4.03%** | $\frac{1}{n} \sum \left|\frac{Y - \hat{Y}}{Y}\right| \times 100$ | `forecasting.py` (Line 27) | `FactForecastResults.MAPE` | `[Forecast MAPE]` |
| **Forecast Accuracy (RMSE)**| **142.74 Units** | $\sqrt{\frac{1}{n} \sum (Y - \hat{Y})^2}$ | `forecasting.py` (Line 28) | `FactForecastResults.RMSE` | `[Forecast RMSE]` |
| **RFM Champions Count** | **3,200 (12.8%)** | Quantile score $R=4, F=4, M=4$ | `customer_segmentation.py` (Line 36) | `FactRFMSegments.CustomerSegment` | `[Champions Count]` |
| **At Risk Customer Spend** | **2,500 Accounts** | Quantile score $R \le 2$, Spend High | `customer_segmentation.py` (Line 39) | `FactRFMSegments.CustomerSegment` | `[At Risk Spend]` |
| **Class A Product Share** | **$114.2M (80%)** | Cumulative Revenue $\le 0.80$ Pareto | `inventory_analysis.py` (Line 32) | `Inventory_Optimization_Metrics.csv` | `[Class A Revenue]` |
| **Economic Order Quantity**| **EOQ Units** | $\sqrt{\frac{2 \cdot D \cdot S}{H}}$ ($S=\$125, H=\text{Cost}\times 0.18$) | `inventory_analysis.py` (Line 42) | `Inventory_Optimization_Metrics.EOQ` | `[EOQ]` |
| **Days of Inventory (DOI)**| **48 Days (US-WEST)**| $\frac{\text{CurrentStock} \times \text{Cost}}{\text{Daily COGS}}$ | `inventory_analysis.py` (Line 50) | `Inventory_Optimization_Metrics.DaysOfInventory` | `[Days of Inventory]` |
| **Excess Working Capital** | **$420,000** | $(\text{DOI}_{\text{Actual}} - \text{DOI}_{\text{Target}}) \times \text{Daily COGS}$ | `generate_insights.py` (Line 22) | `Executive_AI_Insights.csv` | `[Excess Capital]` |
| **Supplier SUP-014 Defect**| **4.25% (vs 1.5%)** | $\frac{\text{Defective Units}}{\text{Total Units Received}}$ | `generate_raw_data.py` (Line 115) | `DimSuppliers.DefectRate` | `[Supplier Defect %]` |
| **Carrier SLA Breach** | **86.2% (Regional)**| $\frac{\text{On-Time Shipments}}{\text{Total Carrier Shipments}}$ | `generate_raw_data.py` (Line 132) | `DimLogisticsCarriers.ReliabilityScore` | `[Carrier SLA %]` |
| **Freight Cost Anomalies** | **142 Incidents** | Statistical Z-score $|Z| > 3.0$ | `anomaly_detection.py` (Line 16) | `Operational_Anomalies.csv` | `[Anomaly Count]` |

---

## 3. Detailed Source Reference Breakdown by Domain

### 3.1 Raw Synthetic Seed Foundation (`python/generate_raw_data.py`)
- **Random Seed**: `np.random.seed(42)` and `random.seed(42)` guarantee **100% deterministic reproducibility**. Running the generator produces the exact same numbers on any machine.
- **Date Horizon**: 1,096 days spanning 2023-01-01 to 2025-12-31 (`DimCalendar.csv`).
- **Entity Counts**:
  - `FactOrders`: 520,000 rows
  - `DimCustomers`: 25,000 accounts
  - `DimProducts`: 2,000 SKUs (Technology 38.4%, Furniture 26.7%, Office Supplies 20.7%, Logistics Gear 14.2%)
  - `DimWarehouses`: 15 regional facilities
  - `DimSuppliers`: 120 global suppliers
  - `DimLogisticsCarriers`: 8 enterprise carriers

### 3.2 Time Series Demand Forecasting Engine (`python/forecasting.py`)
- **Algorithm**: Holt-Winters Triple Exponential Smoothing (Level, Trend, Seasonality).
- **Historical Fitting Window**: 1,096 daily aggregated demand observations.
- **Formulas**:
  - Point Forecast: $\hat{Y}_{t+h} = (\ell_t + h b_t) s_{t+h-m(k+1)}$
  - 95% Confidence Interval: $\hat{Y}_{t+h} \pm 1.96 \times \sigma_{\text{residual}}$
  - Evaluated Fitted Accuracy: **MAPE = 4.03%**, **RMSE = 142.74 units**.

### 3.3 Inventory Optimization Math (`python/inventory_analysis.py`)
- **Pareto ABC Rule**: Sorts products by total revenue descending. Products contributing up to 80.0% of cumulative revenue are labeled `Class A` ($114.2M), next 15% `Class B` ($21.4M), remaining 5% `Class C` ($7.2M).
- **EOQ Formula**: $\text{EOQ} = \sqrt{\frac{2 \cdot D \cdot S}{H}}$
  - Annual Demand ($D$): Aggregated unit sales per ProductID.
  - Setup Cost ($S$): Fixed procurement order cost ($125.00/order).
  - Holding Cost ($H$): $18.0\%$ of unit cost price ($\text{Cost} \times 0.18$).
- **Days of Inventory (DOI)**: $\text{DOI} = \frac{\text{CurrentStock} \times \text{Cost}}{\text{Annual COGS} / 365}$
  - `WH-US-WEST-1`: Current stock 580,000 units -> DOI = 48 days. Reducing DOI to target 35 days liberates $13 \text{ days} \times \$32,307/\text{day} = \$420,000$ in working capital.

### 3.4 Operational Anomaly Detection Engine (`python/anomaly_detection.py`)
- **Z-Score Formula**: $Z = \frac{X - \mu}{\sigma}$
  - Mean freight shipping cost ($\mu$): $26.25
  - Standard deviation ($\sigma$): $7.15
  - Filter condition $|Z| > 3.0$ identifies 142 shipping cost outlier transactions exceeding $48.00/order.

### 3.5 SQL Database & View Specifications (`sql/views.sql` & `python/setup_database.py`)
- SQLite Database file: `data/ops_intelligence.db` generated by loading cleaned datasets.
- View `vw_ExecutiveMonthlySummary`: Computes monthly aggregated revenue, profit, profit margin %, average order value, and late delivery % directly via SQL `GROUP BY SUBSTR(OrderDate, 1, 7)`.

### 3.6 Web UI Interactive Canvas Engine (`app.js`)
- Renders dynamic Chart.js canvas visuals across all 10 dashboard pages.
- Dynamically recalculates datasets when the user interacts with the Region (`slicer-region`) or Period (`slicer-period`) dropdown controls.
