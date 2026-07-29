# Power BI PBIX Project Blueprint & Semantic Model Specification

## 1. Connection & Model Architecture
- **Data Source Engine**: Folder / Direct import from `data/processed/` CSV files.
- **Model Topology**: Star Schema centered on `Fact_Orders` (520,000 rows) and `Fact_Returns`.
- **Relationships**:
  - `Fact_Orders[OrderDate]` (1) <---> (*) `DimCalendar[FullDate]` (Single Direction)
  - `Fact_Orders[CustomerID]` (*) <---> (1) `DimCustomers[CustomerID]` (Single Direction)
  - `Fact_Orders[ProductID]` (*) <---> (1) `DimProducts[ProductID]` (Single Direction)
  - `Fact_Orders[WarehouseID]` (*) <---> (1) `DimWarehouses[WarehouseID]` (Single Direction)
  - `Fact_Orders[CarrierID]` (*) <---> (1) `DimLogisticsCarriers[CarrierID]` (Single Direction)
  - `Fact_Returns[OrderID]` (*) <---> (1) `Fact_Orders[OrderID]` (Both Directions for Drillthrough)

## 2. Interactive Page Roster (10 Pages)
1. **Executive Dashboard**: Top-level KPIs, sparklines, YoY metrics, operational health summary.
2. **Sales Analytics**: Monthly trend, top products/categories, regional profit heatmap.
3. **Supply Chain Analytics**: Warehouse utilization, supplier performance, inventory aging matrix, lead times.
4. **Logistics Dashboard**: Carrier delay comparison, geographic route cost, delivery heatmaps.
5. **Demand Forecasting**: Interactive 30/60/90/180-day forecast visualization with confidence intervals.
6. **Customer Intelligence**: RFM distribution chart, retention analysis, LTV vs Churn risk.
7. **Profitability Analysis**: Category/Regional waterfall profit breakdown and margin analysis.
8. **Inventory Optimization**: EOQ metrics, ABC Pareto chart, Reorder level alerts.
9. **Risk Monitoring**: Supplier risk score, stockout probability, fraud detection indicators.
10. **Executive Insights**: Automated AI recommendations engine displaying strategic operational fixes.

## 3. Custom Visual Features & Bookmarks
- **Theme JSON**: Embedded `theme.json` for sleek dark navy glassmorphism UI.
- **Field Parameters**: Dynamic measure switcher (Revenue vs Profit vs Order Volume vs Margin %).
- **Tooltip Pages**: Custom tooltip page rendering mini historical sales sparkline on hover over product SKU.
