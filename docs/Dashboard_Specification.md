# Dashboard Specification & Visual Interaction Blueprint

## 1. Design System & UX Principles
- **Theme Theme Tokens**: Custom Enterprise Dark Navy Glassmorphism (`#0F172A` canvas background, `#1E293B` cards with `rgba(255,255,255,0.08)` borders).
- **Color Accent Matrix**:
  - Primary Accent: Cyan (`#38BDF8`)
  - Financial Success: Emerald (`#34D399`)
  - SLA Breach / Risk: Rose Red (`#F87171`)
  - Warning / Caution: Amber (`#FBBF24`)
  - Secondary Accents: Indigo (`#818CF8`) / Purple (`#A78BFA`)
- **Typography**: Inter (Body & UI text) and JetBrains Mono (DAX & Code modal).

---

## 2. Interactive Feature & Control Specifications

### 2.1 Cross-Filtering & Slicer Behavior
- **Global Region Slicer**: Selecting a region (`North America`, `Europe`, `APAC`) dynamically filters all visuals across all 10 pages simultaneously.
- **Global Period Slicer**: Toggles historical evaluation window (`2023`, `2024`, `2025`).
- **Reset Filters Trigger**: Clicking the **Reset** button restores all slicer selections to global view.

### 2.2 Tooltip & Hover Pages
- **Product SKU Hover Tooltip**: Hovering over any product bar on Sales Analytics displays a custom tooltip page rendering a mini historical 12-month sales trend line.
- **Supplier Risk Hover Tooltip**: Hovering over a supplier node renders a breakdown of vendor defect rate history and avg lead times.

### 2.3 Dynamic Field Parameters & Measure Switching
- **Sales Measure Switcher**: Toggle visual charts between `Net Revenue`, `Gross Profit`, `Order Volume`, and `Gross Margin %`.
- **Bookmark Navigation**: Bookmarks allow toggling between Revenue View and Profitability View without changing page tabs.

### 2.4 Drill-Through Paths
- **Executive to Sales Drillthrough**: Right-clicking a regional visual on Page 1 allows drill-through to Page 2 (Sales Analytics) pre-filtered for that specific region.
- **Inventory to Supplier Drillthrough**: Right-clicking an out-of-stock SKU on Page 8 drills through to Page 3 pre-filtered for the associated supplier.

---

## 3. Page-by-Page Visual Specification (10 Pages)

### Page 1: Executive Dashboard
- **Target Persona**: VP of Global Supply Chain, C-Suite.
- **Top Row KPI Cards**:
  1. Net Revenue ($142.8M, +14.2% YoY)
  2. Gross Profit ($46.4M, 32.5% Margin)
  3. Total Orders (520,000, +8.6% Growth)
  4. Perfect Order Rate (94.8%, Target > 93.5%)
  5. Return Rate (4.80%, SLA < 5.0%)
  6. On-Time Delivery (96.2%, +1.4% MoM)
- **Visuals**:
  - `1.1 Line Chart`: 12-Month Net Revenue & Profit Rolling Trend.
  - `1.2 Doughnut Chart`: Regional Revenue Distribution (NA, EU, APAC).

### Page 2: Sales Analytics
- **Target Persona**: Category Managers, Merchandising Analysts.
- **Visuals**:
  - `2.1 Vertical Bar`: Net Revenue by Product Category.
  - `2.2 Horizontal Bar`: Top 5 SKUs by Gross Margin %.

### Page 3: Supply Chain Analytics
- **Target Persona**: Fulfillment Center Managers, Procurement Officers.
- **Visuals**:
  - `3.1 Clustered Bar`: Warehouse Units Held vs Capacity Threshold.
  - `3.2 Radar Chart`: Supplier Quality Rating vs Defect Rate vs Delivery SLA.

### Page 4: Logistics Dashboard
- **Target Persona**: Director of Logistics, Fleet Operations.
- **Visuals**:
  - `4.1 Horizontal Bar`: Carrier SLA On-Time Delivery Reliability %.
  - `4.2 Area Line Chart`: Average Freight Shipping Cost ($) per Order by Route.

### Page 5: Demand Forecasting
- **Target Persona**: Inventory Planners, Demand Forecasting Analysts.
- **Visuals**:
  - `5.1 Predictive Line`: 180-Day Daily Order Demand Forecast with 95% Upper/Lower Confidence Interval Band (MAPE: 4.09%, RMSE: 144.94 units).

### Page 6: Customer Intelligence
- **Target Persona**: Customer Success Lead, Marketing Analytics.
- **Visuals**:
  - `6.1 Pie Chart`: Customer Distribution by RFM Segment.
  - `6.2 Vertical Bar`: Average Lifetime Value (LTV) per Customer Segment.

### Page 7: Profitability Analysis
- **Target Persona**: Financial Analysts, CFO.
- **Visuals**:
  - `7.1 Waterfall Chart`: Financial Flow (Gross Sales -> Discounts -> Net Revenue -> COGS -> Shipping -> Net Profit).

### Page 8: Inventory Optimization
- **Target Persona**: Supply Chain Analysts, Warehouse Operations.
- **Visuals**:
  - `8.1 Pareto Bar`: ABC Category Revenue Share (Class A 80%, Class B 15%, Class C 5%).
  - `8.2 Vertical Bar`: Days of Inventory (DOI) per Fulfillment Center.

### Page 9: Risk Monitoring
- **Target Persona**: Risk Officers, Operations Leads.
- **Visuals**:
  - `9.1 Stacked Bar`: Anomaly Count by Category (Freight Spikes, Margin Dips, Defect Outliers).
  - `9.2 Bar Chart`: Stockout Probability Index by Warehouse.

### Page 10: Executive AI Insights
- **Target Persona**: C-Suite Executives, Operational Steering Committee.
- **Visuals**:
  - `10.1 Card Grid`: Dynamic AI Recommendation Cards displaying title, priority tag (Critical/High), category, and recommendation text.
