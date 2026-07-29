# Solution Architecture & Data Lineage Documentation

## 1. End-to-End Data Lineage Flow

The following lineage diagram illustrates the data flow from synthetic raw generation down to executive decision support:

```text
[ Python Synthetic Data Generator ]
  (generate_raw_data.py)
            │
            ▼
[ Raw Dataset Layer (data/raw/) ]
  ├── Orders.csv (520,000 Fact rows)
  ├── Customers.csv (25,000 Customers)
  ├── Products.csv (2,000 SKUs)
  ├── Warehouses.csv (15 FCs)
  ├── Suppliers.csv (120 Vendors)
  ├── Logistics_Carriers.csv (8 Carriers)
  ├── Returns.csv (25,480 Returns)
  └── DimCalendar.csv (1,096 Days)
            │
            ▼
[ Python ETL & ML Analytics Engine ]
  ├── Data Cleaning (data_cleaning.py)
  ├── Feature Engineering (feature_engineering.py)
  ├── Demand Forecasting (forecasting.py)
  ├── RFM Customer Segmentation (customer_segmentation.py)
  ├── Inventory Optimization (inventory_analysis.py)
  ├── Outlier Anomaly Detection (anomaly_detection.py)
  └── AI Insight Synthesizer (generate_insights.py)
            │
            ▼
[ Processed Dataset Layer (data/processed/) ]
  ├── Enriched_Orders.csv
  ├── Demand_Forecast_Results.csv
  ├── Customer_RFM_Segments.csv
  ├── Inventory_Optimization_Metrics.csv
  ├── Operational_Anomalies.csv
  └── Executive_AI_Insights.csv
            │
            ├─────────────────────────────────────────┐
            ▼                                         ▼
[ SQL Relational Database ]            [ Power BI / Interactive Web App ]
  ├── Star Schema DDL                    ├── Dark Navy Theme (theme.json)
  ├── Foreign Key Constraints            ├── VertiPaq Semantic Model
  ├── Performance Indexes                ├── 30+ Advanced DAX Measures
  └── Amazon Analytical Views            └── 10-Page Interactive Dashboard UI
            │                                         │
            └────────────────────┬────────────────────┘
                                 ▼
                    [ Executive Decision Support ]
```

---

## 2. Solution Component Architecture

```text
Python Synthetic Generator ────► Raw CSV Files ────► Python ETL & Analytics Engine
                                                            │
                                                            ▼
Executive Business Decisions ◄─── Interactive Web Dashboard ◄─── Processed Datasets / SQL Engine
```

---

## 3. Technology Layer Specifications

| System Layer | Technology | Operational Function |
|---|---|---|
| **Data Generation** | Python 3.11, numpy, pandas | Generates 520,000 realistic orders and dimension entities with statistical distributions. |
| **ETL & Data Cleaning** | Python 3.11, pandas | Deduplication, null value imputation, winsorization of freight shipping cost outliers. |
| **Machine Learning & Stats** | scikit-learn, statsmodels | Holt-Winters time-series demand forecasting and Isolation Forest anomaly detection. |
| **Relational Database** | PostgreSQL / Snowflake DDL | Normalized Star Schema with foreign keys, indexes, views, and complex BI queries. |
| **Semantic Data Model** | Power BI VertiPaq | Single-direction Star Schema relationships with dynamic field parameters and calculation groups. |
| **Presentation Web UI** | HTML5, CSS3, JS (Chart.js) | Dark navy glassmorphism responsive single-page web dashboard displaying 10 pages. |
