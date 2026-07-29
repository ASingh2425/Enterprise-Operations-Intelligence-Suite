# 📊 Executive Storyline & 10-Page Dashboard Analytics Report

> **Enterprise Operations Intelligence Suite**  
> *Simulating Senior Business Intelligence Analyst Decision Support at Amazon Global Operations*

---

## 🧭 Master Analytical Storyline & Executive Flow

The 10-page Operations Intelligence Suite follows a structured, narrative-driven analytics flow—moving from high-level executive KPIs down to root-cause operational analysis, predictive forecasting, risk mitigation, and automated strategic recommendations:

```text
[ Page 1: Executive Overview ] ──► "How is our global network performing overall?"
          │
          ├──► [ Page 2: Sales Analytics ] ────────► "Which products & categories generate revenue/margin?"
          ├──► [ Page 3: Supply Chain Analytics ] ─► "Are fulfillment centers & suppliers operating efficiently?"
          ├──► [ Page 4: Logistics Dashboard ] ───► "Which freight carriers meet SLA delivery promises?"
          ├──► [ Page 5: Demand Forecasting ] ────► "What will customer demand look like over 180 days?"
          ├──► [ Page 6: Customer Intelligence ] ──► "Which customer cohorts are driving LTV vs drifting to churn?"
          ├──► [ Page 7: Profitability Analysis ] ─► "Where is gross margin being lost in the financial waterfall?"
          ├──► [ Page 8: Inventory Optimization ] ─► "How can we optimize EOQ & safety stock to free capital?"
          └──► [ Page 9: Risk Monitoring ] ────────► "What statistical anomalies & stockout risks threaten operations?"
                    │
                    ▼
[ Page 10: Executive AI Insights ] ──► "What specific strategic decisions must leadership execute today?"
```

---

## 📄 Detailed Breakdown of the 10 Dashboard Pages

---

### Page 1: Executive Dashboard
- **Business Objective**: Provide C-Suite leadership and the VP of Supply Chain with a single-pane-of-glass overview of global operational throughput, financial health, and customer satisfaction.
- **Target Persona**: VP of Global Supply Chain, Chief Operating Officer (COO), Chief Financial Officer (CFO).
- **Executive Storyline**: *"Our global operational network is delivering strong top-line revenue ($142.8M, +14.2% YoY) and solid gross margins (32.5%), while maintaining an industry-leading Perfect Order Rate of 94.8%. However, regional disparities exist between North America and APAC that require localized fulfillment tuning."*

#### Core KPI Cards
1. **Net Revenue ($142.8M)**: Total sales revenue after promotional discounts (`+14.2% YoY`).
2. **Gross Profit ($46.4M)**: Net dollar margin after subtracting COGS and freight shipping (`32.5% Gross Margin`).
3. **Total Orders (520,000)**: Total volume of fulfilled order lines (`+8.6% Growth`).
4. **Perfect Order Rate (94.8%)**: Fulfillment accuracy metric measuring on-time, non-returned, undamaged orders (`Target > 93.5%`).
5. **Return Rate (4.80%)**: Percentage of orders returned by buyers (`SLA Limit < 5.0%`).
6. **On-Time Delivery (96.2%)**: Logistics carrier SLA compliance (`+1.4% MoM`).

#### Visual Graphs & Chart Types
- **12-Month Rolling Revenue & Profit Trend (Line Chart)**: Tracks monthly Net Revenue against Gross Profit. Shows peak demand in Q4 (November $16.8M, December $18.2M) driven by holiday shopping surges.
- **Regional Revenue Distribution (Doughnut Chart)**: Visualizes revenue share across regions: **North America** ($64.2M / 45%), **Europe** ($48.6M / 34%), and **APAC** ($30.0M / 21%).

#### Key Findings & Action Enabled
- **Finding**: Q4 accounts for 34.5% of annual revenue; APAC revenue lags North America by 53.2%.
- **Decision Enabled**: Rebalance Q4 inventory allocations to North American and European hubs 45 days prior to peak season.

---

### Page 2: Sales Analytics
- **Business Objective**: Evaluate revenue growth, price realization, and margin profitability across product categories and individual SKUs.
- **Target Persona**: Category Managers, Merchandising Directors, Pricing Analysts.
- **Executive Storyline**: *"Technology is our primary revenue growth engine ($54.8M), but high-margin Furniture SKUs (48.1% margin) represent our most profitable upsell opportunity."*

#### Core KPI Metrics
- **Category Revenue ($)**: Aggregated sales by catalog category.
- **Gross Margin % per SKU**: `(Selling Price - Cost) / Selling Price`.
- **Average Order Value (AOV)**: `$274.60` global average transaction basket size.

#### Visual Graphs & Chart Types
- **Net Revenue by Product Category (Vertical Bar Chart)**: Compares category revenue:
  - **Technology**: $54.8M (38.4% share)
  - **Furniture**: $38.2M (26.7% share)
  - **Office Supplies**: $29.5M (20.7% share)
  - **Logistics Gear**: $20.3M (14.2% share)
- **Top 5 High-Margin SKUs (Horizontal Bar Chart)**: Ranks top product SKUs by margin percentage:
  1. `PROD-0001 (Laptop)`: 52.4% Margin ($850 Price / $404.60 Cost)
  2. `PROD-0005 (Desk)`: 48.1% Margin
  3. `PROD-0012 (Smartphone)`: 45.3% Margin
  4. `PROD-0020 (Office Chair)`: 42.8% Margin
  5. `PROD-0033 (Barcode Scanner)`: 41.5% Margin

#### Key Findings & Action Enabled
- **Finding**: Technology and Furniture generate 65.1% of total net revenue.
- **Decision Enabled**: Shift promotional ad spend toward Class A Technology SKUs while renegotiating component acquisition costs for Office Supplies.

---

### Page 3: Supply Chain Analytics
- **Business Objective**: Monitor fulfillment center (FC) warehouse capacity utilization and evaluate vendor quality scorecards to prevent supply chain bottlenecks.
- **Target Persona**: Fulfillment Center Managers, Procurement Officers, Vendor Management Leads.
- **Executive Storyline**: *"FC capacity is severely strained at WH-US-WEST-1 (77.3% capacity occupied), while Supplier SUP-014 exhibits a critical defect rate of 4.25% that threatens product quality."*

#### Core KPI Metrics
- **Warehouse Capacity Utilization (%)**: `(Current Units Held / Max Capacity Units) * 100`.
- **Supplier Defect Rate (%)**: Percentage of received vendor batches failing quality inspection (`SLA Limit < 1.5%`).
- **Supplier Risk Index**: Composite score calculating vendor reliability (`Target < 30.0`).

#### Visual Graphs & Chart Types
- **Fulfillment Center Capacity Utilization (Clustered Bar Chart)**: Compares current stock units against maximum storage capacity across top FCs:
  - `WH-US-WEST-1 (Seattle)`: 580,000 units held / 750,000 capacity (77.3% utilization)
  - `WH-EU-CENT-1 (Frankfurt)`: 490,000 / 600,000 (81.7% utilization)
  - `WH-US-EAST-1 (New Jersey)`: 420,000 / 500,000 (84.0% utilization)
- **Supplier Quality & SLA Radar (Radar Chart)**: Maps vendor performance across 5 axes: Rating (5.0), On-Time %, Quality/Defect Rate, Lead Time Days, and Risk Index. Contrasts **Top Preferred Vendor** (Rating 4.9, Defect 1.0%) against **At-Risk Vendor SUP-014** (Rating 3.3, Defect 4.25%, Lead Time 18 days).

#### Key Findings & Action Enabled
- **Finding**: Three major FCs are operating above 75% capacity; Vendor `SUP-014` exceeds defect thresholds by 2.83x.
- **Decision Enabled**: Execute a 18% inventory reduction at `WH-US-WEST-1` and issue a formal vendor quality warning to `SUP-014`.

---

### Page 4: Logistics Dashboard
- **Business Objective**: Analyze transportation freight carrier performance, transit latencies, on-time delivery compliance, and shipping route costs.
- **Target Persona**: Director of Logistics & Transportation, Fleet Operations Lead.
- **Executive Storyline**: *"Amazon Air Logistics leads network reliability (96.4% on-time), whereas Regional Freight Co accounts for 42% of all late delivery SLA breaches."*

#### Core KPI Metrics
- **On-Time Delivery SLA (%)**: Percentage of shipments delivered on or before promised SLA date (`Target > 95.0%`).
- **Average Freight Shipping Cost ($)**: Mean shipping fee charged per order line (`$26.30` average).
- **Transit Latency (Days)**: Average transit duration from FC dispatch to doorstep delivery (`4.0 days`).

#### Visual Graphs & Chart Types
- **Carrier SLA Reliability (Horizontal Bar Chart)**: Ranks carrier on-time delivery percentages:
  1. `Amazon Air Logistics`: 96.4% On-Time SLA
  2. `DHL Express Global`: 95.2% On-Time SLA
  3. `FedEx Express`: 94.1% On-Time SLA
  4. `UPS Worldwide`: 92.5% On-Time SLA
  5. `Regional Freight Co`: 86.2% On-Time SLA (Severe SLA breach)
- **Average Shipping Cost per Route (Area Line Chart)**: Compares freight costs across international shipping lanes:
  - `US-APAC Lane`: $34.20 / order
  - `EU-APAC Lane`: $31.80 / order
  - `US-EU Lane`: $28.50 / order
  - `Domestic US`: $12.40 / order

#### Key Findings & Action Enabled
- **Finding**: Regional Freight Co's 86.2% SLA lowers global network delivery performance by 1.4%.
- **Decision Enabled**: Shift 15% of regional freight volume from Regional Freight Co to Amazon Air Logistics, raising network SLA to 96.2%.

---

### Page 5: Demand Forecasting
- **Business Objective**: Predict future product order demand for 30, 60, 90, and 180-day horizons using time-series machine learning models to guide procurement.
- **Target Persona**: Inventory Planners, Demand Forecasting Analysts, Supply Chain Directors.
- **Executive Storyline**: *"Time-series forecasting models (MAPE 4.03%) predict a 28% daily order demand surge over the next 180 days, requiring proactive safety stock accumulation."*

#### Core KPI Metrics
- **Predicted Daily Demand (Units)**: Time-series point forecast generated via Holt-Winters Exponential Smoothing.
- **95% Upper & Lower Confidence Bounds**: Statistically calculated demand uncertainty band ($\pm 1.96 \times \sigma$).
- **Forecast Accuracy Metrics**: **MAPE: 4.03%** (Mean Absolute Percentage Error), **RMSE: 142.74 Units**.

#### Visual Graphs & Chart Types
- **30/60/90/180-Day Predictive Demand Forecast (Line Chart with Confidence Ribbon)**: Displays 15 days of historical daily demand (1,420 to 1,780 units) seamlessly transitioning into a 180-day future point forecast (1,780 to 2,220 units/day) bounded by a shaded green 95% confidence interval ribbon (1,980 to 2,460 units/day).

#### Key Findings & Action Enabled
- **Finding**: Daily demand is projected to increase from 1,780 units/day to 2,220 units/day over 6 months.
- **Decision Enabled**: Issue advance purchase orders to key suppliers 60 days in advance to secure production capacity before peak surge.

---

### Page 6: Customer Intelligence
- **Business Objective**: Analyze customer behavioral cohorts using Recency, Frequency, Monetary (RFM) quantile scoring and Lifetime Value (LTV) distributions.
- **Target Persona**: Customer Retention Lead, Head of CRM, Marketing Analytics.
- **Executive Storyline**: *"Our 3,200 'Champions' generate $4,250 in average LTV, but 2,500 'At Risk' customers representing $2.3M in potential spend require immediate re-engagement."*

#### Core KPI Metrics
- **RFM Cell Score**: 3-digit quantile score (R_Score 1-4, F_Score 1-4, M_Score 1-4).
- **Customer Lifetime Value (LTV)**: Historical cumulative spend per customer (`$1,420` average across 25,000 accounts).
- **Churn Risk Score**: Inverse recency indicator flagging customers with > 90 days since last purchase.

#### Visual Graphs & Chart Types
- **Customer Distribution by RFM Segment (Pie Chart)**: Categorizes 25,000 active customer accounts:
  - `Champions` (R=4, F=4, M=4): 3,200 customers (12.8%)
  - `Loyal Customers` (F>=3, M>=3): 4,800 customers (19.2%)
  - `Promising`: 2,900 customers (11.6%)
  - `At Risk` (R<=2, Spend High): 2,500 customers (10.0%)
  - `Lost / Churned` (R=1, F=1): 1,600 customers (6.4%)
- **Customer Segment Lifetime Value (Vertical Bar Chart)**: Compares average LTV per segment:
  - `Champions`: $4,250 average LTV
  - `Loyal Customers`: $2,850 average LTV
  - `Promising`: $1,450 average LTV
  - `At Risk`: $920 average LTV
  - `Lost`: $380 average LTV

#### Key Findings & Action Enabled
- **Finding**: Champions and Loyal customers generate 61.4% of total company net revenue.
- **Decision Enabled**: Launch targeted re-engagement campaigns to 2,500 "At Risk" customers, capturing $1.2M in annual recurring revenue.

---

### Page 7: Profitability Analysis
- **Business Objective**: Provide a complete financial audit detailing how top-line gross sales erode into net profit through promotional discounts, COGS, and freight shipping.
- **Target Persona**: Chief Financial Officer (CFO), Controller, Corporate FP&A.
- **Executive Storyline**: *"Gross sales of $160.0M yield $46.4M in net profit after deducting $17.2M in promotional discounts, $85.2M in direct COGS, and $11.2M in freight costs."*

#### Core KPI Metrics
- **Gross Sales ($160.0M)**: Total un-discounted order value (`Quantity * UnitPrice`).
- **Promotional Discounts (-$17.2M)**: Price reductions granted to buyers (`10.75% of Gross Sales`).
- **Net Revenue ($142.8M)**: `Gross Sales - Discounts`.
- **COGS (-$85.2M)**: Direct product acquisition/manufacturing cost (`59.6% of Net Revenue`).
- **Freight Shipping Cost (-$11.2M)**: Carrier logistics shipping payouts (`7.8% of Net Revenue`).
- **Net Profit ($46.4M)**: Final bottom-line earnings (`32.5% Gross Margin`).

#### Visual Graphs & Chart Types
- **Revenue to Net Profit Financial Flow (Waterfall Chart)**: Renders sequential financial deductions starting from **Gross Sales ($160.0M)**, subtracting **Discounts (-$17.2M)** -> **Net Revenue ($142.8M)**, subtracting **COGS (-$85.2M)**, subtracting **Shipping Cost (-$11.2M)**, landing on final **Net Profit ($46.4M)**.

#### Key Findings & Action Enabled
- **Finding**: Discounts and shipping costs reduce top-line sales by $28.4M (17.75%).
- **Decision Enabled**: Restructure promotional discount caps to 15% maximum and renegotiate bulk carrier shipping contracts to save $1.1M annually.

---

### Page 8: Inventory Optimization
- **Business Objective**: Balance inventory holding costs against stockout risks using Economic Order Quantity (EOQ), Safety Stock math, and ABC Pareto classification.
- **Target Persona**: Supply Chain Directors, Warehouse Inventory Planners.
- **Executive Storyline**: *"Class A SKUs account for 80% of revenue ($114.2M), but overall Days of Inventory (48 days at WH-US-WEST-1) indicates $420,000 in excess working capital lockup."*

#### Core KPI Metrics
- **Economic Order Quantity (EOQ)**: $\sqrt{\frac{2 \cdot D \cdot S}{H}}$ (Optimal reorder batch size).
- **Days of Inventory (DOI)**: `(Current Inventory Value / Daily COGS)` (`42.5 days` global average).
- **ABC Revenue Share**: Pareto rule classifying products into Class A (Top 80% revenue), Class B (Next 15%), and Class C (Tail 5%).

#### Visual Graphs & Chart Types
- **ABC Inventory Pareto Revenue Classification (Bar Chart)**: Visualizes revenue contribution by Pareto category:
  - `Class A (Top SKUs)`: $114.2M Net Revenue (80.0% share)
  - `Class B (Mid SKUs)`: $21.4M Net Revenue (15.0% share)
  - `Class C (Tail SKUs)`: $7.2M Net Revenue (5.0% share)
- **Days of Inventory per Warehouse (Vertical Bar Chart)**: Compares inventory holding duration across FCs:
  - `WH-EU-CENT-1`: 52 Days of Inventory (High overstock)
  - `WH-US-WEST-1`: 48 Days of Inventory
  - `WH-APAC-TYO-1`: 44 Days of Inventory
  - `WH-US-EAST-1`: 38 Days of Inventory
  - `WH-UK-LOND-1`: 32 Days of Inventory (Optimal velocity)

#### Key Findings & Action Enabled
- **Finding**: `WH-EU-CENT-1` and `WH-US-WEST-1` exceed target DOI (35 days) by 13 to 17 days.
- **Decision Enabled**: Implement automated EOQ batch reordering and reduce safety stock buffers for slow-moving Class C items.

---

### Page 9: Risk Monitoring
- **Business Objective**: Detect operational anomalies (freight cost spikes, margin compression) and monitor warehouse stockout probabilities in real time.
- **Target Persona**: Operational Risk Officers, Supply Chain Steering Committee.
- **Executive Storyline**: *"Automated anomaly engines flagged 142 freight cost spikes and identified a 0.42 stockout probability at WH-EU-CENT-1 due to lead time delays."*

#### Core KPI Metrics
- **Statistical Z-Score**: Measure of standard deviation distance ($|Z| > 3.0$ flags shipping cost outliers).
- **Stockout Risk Index**: `(ReorderPoint - CurrentStock) / ReorderPoint` (`0.18` global mean).
- **Anomaly Incident Count**: Total operational risk events detected by Isolation Forest algorithms.

#### Visual Graphs & Chart Types
- **Detected Operational Anomalies by Category (Stacked Bar Chart)**: Breaks down 315 total detected anomaly incidents:
  - `Freight Cost Spikes`: 142 incidents (Outlier shipping charges > $48.00)
  - `Margin Compression Events`: 88 incidents (Profit margin drops < 15%)
  - `Supplier Defect Outliers`: 54 incidents (Vendor defect rates > 3.0%)
  - `Return Surges`: 31 incidents (Localized return rate spikes)
- **Stockout Probability Index by Warehouse (Vertical Bar Chart)**: Evaluates stockout risk across FCs:
  - `WH-EU-CENT-1`: 0.42 Stockout Risk (HIGH RISK)
  - `WH-APAC-TYO-1`: 0.28 Stockout Risk (MEDIUM RISK)
  - `WH-US-WEST-1`: 0.18 Stockout Risk
  - `WH-US-EAST-1`: 0.12 Stockout Risk
  - `WH-UK-LOND-1`: 0.08 Stockout Risk (LOW RISK)

#### Key Findings & Action Enabled
- **Finding**: `WH-EU-CENT-1` faces a 42% stockout probability for high-demand Class A products.
- **Decision Enabled**: Trigger emergency inventory transfer of 25,000 units from `WH-UK-LOND-1` to `WH-EU-CENT-1`.

---

### Page 10: Executive AI Insights
- **Business Objective**: Synthesize complex multi-system analytics into plain-language, prioritized operational recommendations for executive decision support.
- **Target Persona**: Chief Executive Officer (CEO), Executive Steering Committee, VP of Operations.
- **Executive Storyline**: *"Machine learning narrative engines continuously synthesize real-time data into prioritized, actionable business decisions with quantified ROI."*

#### Dynamic Card Components
- **Priority Indicator**: Color-coded risk badges (`CRITICAL`, `HIGH`, `MEDIUM`, `INFO`).
- **Strategic Title**: Concise operational headline.
- **Actionable Recommendation**: Detailed natural language recommendation text detailing current status, target fix, and dollar impact.

#### Sample Live Recommendations Generated
1. **[CRITICAL] Inventory Reduction Opportunity at WH-US-WEST-1**  
   *Recommendation*: Current stock level at WH-US-WEST-1 stands at 580,000 units. Reduce holding inventory by 18% to free up ~$420,000 in working capital and lower holding costs.
2. **[CRITICAL] Vendor Audit Recommended for Global Supplier 14**  
   *Recommendation*: Supplier 14 exhibits a defect rate of 4.25% (Threshold: 1.5%) and average delivery delay of 18 days. Contract renegotiation or vendor replacement recommended.
3. **[HIGH] Carrier SLA Late Delivery Alert**  
   *Recommendation*: Regional Freight Co accounts for 42% of all late shipments. Shift 15% volume to Amazon Air Logistics to boost overall network SLA to 97.1%.
4. **[HIGH] Margin Compression in European Fulfillment Hub**  
   *Recommendation*: Net profit margin at WH-EU-CENT-1 is lagging target by 4.2%. Re-evaluate localized freight costs and order fulfillment routes.
5. **[MEDIUM] APAC Demand Surge in Technology Category**  
   *Recommendation*: Technology products in APAC generated $11.2M in net revenue. Maintain 30-day safety stock buffer to capture projected peak demand.

---

## 📑 Summary of Decisions Enabled & Business Value

| Dashboard Page | Primary Focus | Key Decision Enabled | Financial / Operational Impact |
|---|---|---|---|
| **Page 1: Executive** | Global Throughput | Rebalance Q4 inventory 45 days prior to peak. | Captures $18.2M peak December revenue. |
| **Page 2: Sales** | Margin Profitability | Shift ad spend to Class A Technology SKUs. | Elevates category sales by 12.4%. |
| **Page 3: Supply Chain** | Warehouse & Vendors | Issue quality audit to Supplier SUP-014. | Reduces return refunds by $85,000/yr. |
| **Page 4: Logistics** | Carrier SLAs | Reallocate 15% freight volume to Amazon Air. | Raises global Perfect Order Rate to 96.2%. |
| **Page 5: Forecasting** | Demand Prediction | Place advance purchase orders 60 days ahead. | Prevents $2.4M in peak stockout losses. |
| **Page 6: Customers** | RFM & LTV | Launch targeted retention campaign for At Risk. | Captures $1.2M recurring annual spend. |
| **Page 7: Profitability** | Financial Flow | Cap promotional discounts at 15%. | Recovers $1.1M in net profit margin. |
| **Page 8: Inventory** | Capital Velocity | Execute 18% inventory reduction at US-WEST. | Liberates $420,000 working capital. |
| **Page 9: Risk** | Anomalies & Stockouts | Transfer 25k units from UK to EU-CENTRAL. | Mitigates 42% stockout probability. |
| **Page 10: AI Insights** | Automated Action | Execute prioritized C-Suite recommendation cards. | Unified strategic operational alignment. |
