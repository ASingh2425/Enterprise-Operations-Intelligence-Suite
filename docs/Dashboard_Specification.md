# Dashboard Specification & Visual Blueprint

## 1. Design System & UX Standards
- **Theme Aesthetics**: Custom Enterprise Dark Navy Glassmorphism (`#0F172A` background, `#1E293B` cards with `rgba(255,255,255,0.08)` glass borders).
- **Color Palette Tokens**:
  - Primary Accent: Cyan (`#38BDF8`)
  - Financial Growth / Success: Emerald (`#34D399`)
  - Risk / SLA Breach: Rose Red (`#F87171`)
  - Caution / Warning: Amber (`#FBBF24`)
  - Secondary Category: Indigo (`#818CF8`) / Purple (`#A78BFA`)
- **Typography**: Inter (UI font) and JetBrains Mono (Code/DAX view).
- **Layout Grid**: Responsive 12-column flexbox grid with sticky top header controls.

---

## 2. Page-by-Page Visual Specification (10 Pages)

### Page 1: Executive Dashboard
- **Target Persona**: VP of Global Supply Chain, C-Suite Executives.
- **Top Row KPI Cards**:
  1. Net Revenue ($142.8M, +14.2% YoY)
  2. Gross Profit ($46.4M, 32.5% Margin)
  3. Total Orders (520,000, +8.6% Growth)
  4. Perfect Order Rate (94.8%, Target > 93.5%)
  5. Return Rate (4.80%, SLA < 5.0%)
  6. On-Time Delivery (96.2%, +1.4% MoM)
- **Main Canvas Visuals**:
  - `Visual 1.1` (Line Chart): 12-Month Net Revenue & Gross Profit Rolling Trend.
  - `Visual 1.2` (Doughnut Chart): Regional Revenue Distribution (North America vs Europe vs APAC).

### Page 2: Sales Analytics
- **Target Persona**: Category Managers, Merchandising Analysts.
- **Main Canvas Visuals**:
  - `Visual 2.1` (Vertical Bar Chart): Net Revenue by Product Category.
  - `Visual 2.2` (Horizontal Bar Chart): Top 5 SKUs by Gross Margin %.

### Page 3: Supply Chain Analytics
- **Target Persona**: Fulfillment Center Managers, Procurement Officers.
- **Main Canvas Visuals**:
  - `Visual 3.1` (Clustered Bar Chart): Warehouse Current Units Held vs Capacity Threshold.
  - `Visual 3.2` (Radar Chart): Supplier Quality Rating vs Defect Rate vs Delivery SLA.

### Page 4: Logistics Dashboard
- **Target Persona**: Director of Logistics, Fleet Operations.
- **Main Canvas Visuals**:
  - `Visual 4.1` (Horizontal Bar Chart): Carrier SLA On-Time Delivery Reliability %.
  - `Visual 4.2` (Area Line Chart): Average Freight Shipping Cost ($) per Order by Route.

### Page 5: Demand Forecasting
- **Target Persona**: Inventory Planners, Demand Forecasting Analysts.
- **Main Canvas Visuals**:
  - `Visual 5.1` (Predictive Line Chart): 180-Day Daily Order Demand Forecast with 95% Upper/Lower Confidence Interval Band. Model: Holt-Winters Exponential Smoothing (MAPE: 4.09%, RMSE: 144.94 units).

### Page 6: Customer Intelligence
- **Target Persona**: Customer Success Lead, Marketing Analytics.
- **Main Canvas Visuals**:
  - `Visual 6.1` (Pie Chart): Customer Distribution by RFM Segment (Champions, Loyal, Promising, At Risk, Lost).
  - `Visual 6.2` (Vertical Bar Chart): Average Lifetime Value (LTV) per Customer Segment.

### Page 7: Profitability Analysis
- **Target Persona**: Financial Analysts, CFO.
- **Main Canvas Visuals**:
  - `Visual 7.1` (Waterfall Chart): Financial Flow Breakdown (Gross Sales -> Discounts -> Net Revenue -> COGS -> Shipping Cost -> Net Profit).

### Page 8: Inventory Optimization
- **Target Persona**: Supply Chain Analysts, Warehouse Operations.
- **Main Canvas Visuals**:
  - `Visual 8.1` (Pareto Bar Chart): ABC Category Revenue Share (Class A 80%, Class B 15%, Class C 5%).
  - `Visual 8.2` (Vertical Bar Chart): Days of Inventory (DOI) per Fulfillment Center.

### Page 9: Risk Monitoring
- **Target Persona**: Risk Officers, Operations Leads.
- **Main Canvas Visuals**:
  - `Visual 9.1` (Stacked Bar Chart): Anomaly Count by Type (Freight Spikes, Margin Dips, Defect Outliers, Return Surges).
  - `Visual 9.2` (Gauge / Bar Chart): Stockout Probability Index by Warehouse.

### Page 10: Executive AI Insights
- **Target Persona**: C-Suite Executives, Operational Steering Committee.
- **Main Canvas Visuals**:
  - `Visual 10.1` (Dynamic Card Grid): AI Narrative Generator Cards displaying title, priority tag (Critical, High, Medium), operational category, and actionable business recommendation text.

---

## 3. Interactive Controls & Navigation Features
- **Global Region Slicers**: Dropdown filtering all visual calculations by Global, North America, Europe, or APAC.
- **Global Date Period Slicer**: Dropdown toggling historical scope (2023, 2024, 2025).
- **Reset Filters Button**: Resets active slicer selections to default global view.
- **DAX Calculation Modal**: Popup window displaying DAX code blocks for 30+ measures.
