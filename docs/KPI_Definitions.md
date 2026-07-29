# Master Key Performance Indicator (KPI) Catalog & Mapping Matrix

> **Benchmark Disclaimer**: *Target values listed in this document represent standardized operational benchmarks for analytical demonstration purposes and do not represent any private corporation's internal performance objectives.*

---

## 1. Master KPI Definitions & Mathematical Formulas

| KPI Name | Mathematical Formula | Target Benchmark | Target Persona | Business Significance |
|---|---|---|---|---|
| **Net Revenue** | $\sum (\text{GrossRevenue} - \text{Discounts})$ | > $140.0M / Yr | VP Supply Chain, CFO | Core top-line financial throughput after promotions. |
| **Gross Profit** | $\sum (\text{NetRevenue} - \text{COGS} - \text{ShippingCost})$ | > $45.0M / Yr | CFO, Category Leads | Net dollar profit after direct manufacturing and freight shipping costs. |
| **Gross Margin %** | $\frac{\text{Gross Profit}}{\text{Net Revenue}} \times 100$ | > 32.0% | Category Leads, CFO | Percentage of revenue retained as gross profit. |
| **Average Order Value (AOV)** | $\frac{\text{Net Revenue}}{\text{Total Orders}}$ | > $270.00 | Marketing, Merchandising | Average transaction basket monetary size. |
| **Perfect Order Rate %** | $\frac{\text{On-Time \& Non-Returned Orders}}{\text{Total Orders}} \times 100$ | > 93.5% | VP Supply Chain, Logistics | Industry-standard fulfillment accuracy metric widely used by enterprise e-commerce organizations. |
| **On-Time Delivery %** | $\frac{\text{Orders Delivered} \le \text{Promised Date}}{\text{Total Orders}} \times 100$ | > 95.0% | Logistics Director | Measures carrier delivery SLA compliance. |
| **Return Rate %** | $\frac{\text{Returned Orders}}{\text{Total Orders}} \times 100$ | < 5.0% | Quality Lead, Merchandising | Evaluates product quality and order accuracy dissatisfaction. |
| **Fill Rate %** | $\frac{\text{Orders Shipped Complete}}{\text{Total Orders Placed}} \times 100$ | > 98.0% | Warehouse Managers | Immediate stock availability against order demand. |
| **Economic Order Quantity (EOQ)** | $\sqrt{\frac{2 \cdot D \cdot S}{H}}$ | Batch Specific | Warehouse Managers | Mathematically balances holding cost $H$ and setup cost $S$. |
| **Safety Stock Level** | $Z \times \sqrt{\text{LeadTime}} \times \sigma_{\text{DailyDemand}}$ | SKU Specific | Inventory Analysts | Stock buffer guarding against demand spikes during lead time. |
| **Days of Inventory (DOI)** | $\frac{\text{Current Inventory Value}}{\text{Daily COGS}}$ | 30 – 45 Days | VP Supply Chain, Warehouse | Quantifies capital velocity and stockholding efficiency. |
| **Inventory Turnover Ratio** | $\frac{365}{\text{Days of Inventory}}$ | 8.0x – 12.0x / Yr | CFO, Warehouse Managers | Number of times inventory is sold and replaced per year. |
| **Supplier Risk Index** | $(5 - \text{Rating})\cdot 15 + (\text{DefectRate}\cdot 1000) + (\text{LeadTime}\cdot 1.5)$ | < 30.0 (Low Risk) | Vendor Management Lead | Composite score evaluating supplier reliability and quality. |
| **Stockout Risk Score** | $\max\left(0, \frac{\text{ReorderPoint} - \text{CurrentStock}}{\text{ReorderPoint}}\right)$ | < 0.15 | Warehouse Operations | Probability metric flagging imminent stockout risk. |

---

## 2. KPI-to-Dashboard Page Mapping Matrix

This matrix demonstrates how each KPI is intentionally assigned across the 10 interactive dashboard pages to support specific decision-making workflows:

| Dashboard Page | Assigned Primary KPIs | Secondary / Supporting KPIs | Target Visual Component |
|---|---|---|---|
| **1. Executive Dashboard** | Net Revenue, Gross Profit, Perfect Order Rate % | Return Rate %, On-Time Delivery %, Gross Margin % | Executive KPI Cards, 12M Line Trend, Region Donut |
| **2. Sales Analytics** | Net Revenue, Gross Margin %, AOV | Category Revenue, Top SKU Margins | Category Bar Chart, Top SKU Horizontal Bars |
| **3. Supply Chain Analytics** | Capacity Utilization %, Supplier Risk Index | Defect Rate %, Avg Delivery Days | Warehouse Capacity Bars, Supplier Risk Radar |
| **4. Logistics Dashboard** | On-Time Delivery %, Carrier Late % | Route Shipping Cost, Transit Days | Carrier SLA Horizontal Bars, Route Line Chart |
| **5. Demand Forecasting** | Predicted Demand Units, MAPE, RMSE | 95% Confidence Bounds | 180-Day Predictive Time Series Line Chart |
| **6. Customer Intelligence** | Customer LTV, RFM Segment Distribution | Recency Days, Order Frequency | RFM Segment Pie Chart, LTV Bar Chart |
| **7. Profitability Analysis** | Gross Revenue, Net Revenue, COGS, Net Profit | Discount Payouts, Shipping Cost Payouts | Financial Waterfall Flow Chart |
| **8. Inventory Optimization**| ABC Class Revenue Share, Days of Inventory (DOI) | EOQ, Safety Stock Level, Reorder Alerts | ABC Pareto Bar Chart, Warehouse DOI Bars |
| **9. Risk Monitoring** | Anomaly Incident Count, Stockout Risk Score | Freight Cost Z-Scores, Margin Dips | Anomaly Count Bars, Stockout Risk Index Bars |
| **10. Executive AI Insights** | Strategic Operational Impact Score | Priority Classification (Critical/High) | Narrative AI Recommendation Cards |
