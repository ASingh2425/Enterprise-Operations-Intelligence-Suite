# Project Architecture & Workflow Specification

## 1. End-to-End System Workflow

```
[ Raw Synthetic Data Layer (data/raw/) ]
  ├── Orders (520,000 Fact rows)
  ├── Customers (15,000 Rows)
  ├── Products (80 SKUs)
  ├── Warehouses (6 FCs)
  ├── Suppliers (40 Vendors)
  ├── Logistics (5 Carriers)
  └── Returns (~25,000 rows)
         │
         ▼
[ Python ETL & Analytical Analytics Engine ]
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
[ SQL Relational Database ]    [ Power BI / Interactive Web App ]
  ├── Star Schema DDL           ├── Theme.json (Dark Glassmorphism)
  ├── Foreign Key Constraints   ├── 30+ Advanced DAX Measures
  ├── Analytical Indexes        ├── 10-Page Dashboard Application
  └── Amazon Analytical Views   └── Live Chart.js Interactivity
```

---

## 2. Technology Stack Justification

| Layer | Technology Selected | Justification & Architectural Role |
|---|---|---|
| **Data Generation & Preprocessing** | Python 3.11 (pandas, numpy) | High performance vector arithmetic for generating 520,000 orders and performing ETL pipelines. |
| **Statistical & Machine Learning** | scikit-learn, statsmodels | Exponential Smoothing (Holt-Winters) demand forecasting and Isolation Forest anomaly detection. |
| **Relational Database** | PostgreSQL / Snowflake DDL | Production relational database engine with index tuning, views, and complex analytical queries. |
| **BI Presentation & DAX Engine** | Power BI Desktop, VertiPaq | Industry-standard business intelligence semantic modeling with dynamic field parameters and bookmarks. |
| **Interactive Portfolio Showcase** | HTML5, CSS3, JS (Chart.js) | High-performance single-page web app providing an online dashboard visualization. |
| **Documentation & Versioning** | Markdown, Git, GitHub Pages | Consulting-grade enterprise documentation suite hosted on GitHub. |
