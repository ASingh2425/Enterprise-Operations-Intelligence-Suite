# Enterprise Project Architecture

## End-to-End Workflow Diagram

```
[ Raw Data Layer ]
  ├── Orders (520,000 rows)
  ├── Customers (15,000 rows)
  ├── Products (80 SKUs)
  ├── Warehouses (6 FCs)
  ├── Suppliers (40 Vendors)
  ├── Logistics (5 Carriers)
  └── Returns (~25,000 rows)
         │
         ▼
[ Python ETL & Analytics Engine ]
  ├── Data Cleaning & Deduplication (data_cleaning.py)
  ├── Feature Engineering & SLA Calculation (feature_engineering.py)
  ├── Time Series Demand Forecasting (forecasting.py)
  ├── RFM Segmentation & K-Means (customer_segmentation.py)
  ├── ABC / EOQ / Safety Stock Math (inventory_analysis.py)
  ├── Z-Score & Isolation Forest Anomalies (anomaly_detection.py)
  └── Automated AI Insight Synthesizer (generate_insights.py)
         │
         ▼
[ Processed Data Layer (data/processed/) ]
         │
  ┌──────┴──────────────────────────┐
  ▼                                 ▼
[ SQL Relational Schema ]     [ Power BI / Web BI Dashboard ]
  ├── Star Schema DDL           ├── Theme.json (Dark Glassmorphism)
  ├── Foreign Key Constraints   ├── 30+ Advanced DAX Measures
  ├── Analytical Indexes        ├── 10 Interactive Pages
  └── Amazon Analytical Views   └── Live Canvas Interactivity
```

## System Components
1. **Ingestion & Processing**: Python pandas/numpy scripts process data with full error handling.
2. **Database Engine**: PostgreSQL/Snowflake schema definition with primary/foreign keys and index optimizations.
3. **Analytics Engine**: Holt-Winters Exponential Smoothing, RFM Quantiles, EOQ formulas.
4. **Presentation Layer**: Interactive Web App and Power BI dark-navy glassmorphism dashboard with 10 dedicated pages.
