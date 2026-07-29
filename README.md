# 🚀 Enterprise Operations Intelligence Suite

[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen?style=for-the-badge&logo=github)](https://github.com/ASingh2425/Enterprise-Operations-Intelligence-Suite)
[![Power BI](https://img.shields.io/badge/Power_BI-Dark_Navy_Theme-yellow?style=for-the-badge&logo=powerbi)](https://github.com/ASingh2425/Enterprise-Operations-Intelligence-Suite)
[![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)](https://github.com/ASingh2425/Enterprise-Operations-Intelligence-Suite)
[![SQL](https://img.shields.io/badge/SQL-PostgreSQL%2FSnowflake-orange?style=for-the-badge&logo=postgresql)](https://github.com/ASingh2425/Enterprise-Operations-Intelligence-Suite)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

> **End-to-End Supply Chain & Business Analytics Platform** simulating the work of a **Senior Business Intelligence Analyst at Amazon**.

Target Repository: [ASingh2425/Enterprise-Operations-Intelligence-Suite](https://github.com/ASingh2425/Enterprise-Operations-Intelligence-Suite)

---

## 📌 Executive Overview & Core Features

The **Operations Intelligence Suite** is a production-quality Business Intelligence solution built to answer strategic business questions, identify operational inefficiencies across global fulfillment networks, forecast future demand, and support executive decision-making.

### Key Capabilities
- **500,000+ Fact Transactions**: Realistic multi-table relational dataset (Orders, Customers, Products, Warehouses, Suppliers, Logistics Carriers, Returns, Calendar).
- **Python ML & Analytics Engine**:
  - 📈 **Demand Forecasting**: 30, 60, 90, and 180-day predictive time series with 95% confidence intervals (Holt-Winters / ARIMA).
  - 👥 **RFM Customer Segmentation**: Quantile scoring & K-Means clustering (Champions, Loyal, At Risk, Lost).
  - 📦 **Inventory Optimization**: Pareto ABC Classification, Economic Order Quantity (EOQ), Safety Stock, and Days of Inventory (DOI).
  - 🚨 **Anomaly Detection**: Isolation Forest & Z-Score outlier detection for shipping costs and profit compression.
  - 🤖 **Automated Executive Insights**: Natural language operational recommendations generator.
- **Enterprise Power BI Model & Interactive Web App**:
  - Sleek **Dark Navy Glassmorphism UI** (`theme.json`).
  - 30+ Advanced DAX Measures (YoY/MoM, Rolling 12M, Window Functions, Perfect Order %).
  - **10 Interactive Dashboard Pages** accessible via browser UI or Power BI.
- **Production Documentation**: 13 comprehensive markdown documents covering architecture, ETL, SQL, DAX, performance tuning, and testing.

---

## 🖥️ 10 Interactive Dashboard Pages

| Page | Name | Core Business Question Answered | Key Visual Highlights |
|---|---|---|---|
| 1 | **Executive Dashboard** | How is overall global operational performance trending? | Top KPIs, YoY % growth, 12M trend, Regional map breakdown |
| 2 | **Sales Analytics** | Which product categories and SKUs drive gross profit? | Monthly sales trend, top SKUs, margin heatmaps |
| 3 | **Supply Chain Analytics** | Are fulfillment centers operating within capacity thresholds? | FC capacity utilization, supplier defect radar |
| 4 | **Logistics Dashboard** | Which freight carriers meet our SLA delivery promises? | Carrier on-time SLA %, route shipping cost line chart |
| 5 | **Demand Forecasting** | What is predicted product demand over the next 180 days? | Predictive line with 95% confidence band & MAPE/RMSE |
| 6 | **Customer Intelligence** | How are high-value customer segments behaving? | RFM distribution pie chart, Lifetime Value (LTV) bar |
| 7 | **Profitability Analysis** | Where are sales margins being lost from gross to net? | Waterfall breakdown (Sales -> Discounts -> COGS -> Profit) |
| 8 | **Inventory Optimization** | How can stock holding costs be minimized without stockouts? | ABC Pareto chart, Days of Inventory (DOI), EOQ reorder alerts |
| 9 | **Risk Monitoring** | What operational anomalies and stockout risks threaten SLAs? | Anomaly count bars, warehouse stockout risk index |
| 10| **Executive AI Insights** | What direct operational actions should leadership execute? | Automated narrative recommendation cards |

---

## 🏗️ Project Architecture & Repository Structure

```
Operations-Intelligence-Suite/
├── data/
│   ├── raw/                  # Initial raw CSV datasets (520,000+ orders, customers, etc.)
│   ├── processed/            # Cleaned, transformed, and ML-engineered datasets
├── sql/
│   ├── schema.sql            # Core database schema
│   ├── create_tables.sql     # DDL table creation with primary/foreign keys
│   ├── constraints.sql       # Foreign key & data integrity constraints
│   ├── indexes.sql           # Performance B-tree indexes
│   ├── views.sql             # Analytical views (vw_ExecutiveMonthlySummary, etc.)
│   └── business_queries.sql  # Complex analytical queries (Window functions, CTEs)
├── python/
│   ├── generate_raw_data.py  # Synthetic data generation engine
│   ├── data_cleaning.py      # Null handling, outlier capping, type enforcement
│   ├── feature_engineering.py# SLA calculation, perfect order flag, profit margins
│   ├── forecasting.py        # 30/60/90/180-day time series demand forecasting
│   ├── customer_segmentation.py # RFM Scoring & segmentation
│   ├── inventory_analysis.py # ABC Pareto, EOQ formula, Safety Stock
│   ├── anomaly_detection.py # Z-score & Isolation Forest anomaly detection
│   └── generate_insights.py # Natural language executive recommendation synthesizer
├── powerbi/
│   ├── Operations_Intelligence.pbix.md # Power BI PBIX model specification blueprint
│   └── theme.json            # Dark Navy / Glassmorphism Power BI theme
├── web_app/                  # Interactive single-page web dashboard application
│   ├── index.html            # Main container with 10 dashboard pages & navigation
│   ├── styles.css            # Enterprise dark navy styling & micro-animations
│   └── app.js                # Chart.js visualization engine & slicer triggers
├── docs/                     # 13 Production documentation markdown files
│   ├── Business_Problem.md
│   ├── Project_Architecture.md
│   ├── Data_Dictionary.md
│   ├── ETL_Documentation.md
│   ├── SQL_Documentation.md
│   ├── DAX_Measures.md
│   ├── Dashboard_Guide.md
│   ├── Business_Insights.md
│   ├── KPI_Definitions.md
│   ├── Data_Model.md
│   ├── Performance_Optimization.md
│   ├── Testing_Report.md
│   └── Future_Enhancements.md
├── requirements.txt
├── LICENSE
└── README.md
```

---

## ⚡ Quick Start & Setup Guide

### 1. Prerequisites
- Python 3.10+
- Modern Web Browser (Chrome / Edge / Firefox)
- Power BI Desktop (Optional, for `.pbix` model inspect)

### 2. Installation & Pipeline Execution
```bash
# Clone the repository
git clone https://github.com/ASingh2425/Enterprise-Operations-Intelligence-Suite.git
cd Enterprise-Operations-Intelligence-Suite

# Install Python dependencies
pip install -r requirements.txt

# Execute Python ETL & Analytics Pipeline
python python/generate_raw_data.py
python python/data_cleaning.py
python python/feature_engineering.py
python python/forecasting.py
python python/customer_segmentation.py
python python/inventory_analysis.py
python python/anomaly_detection.py
python python/generate_insights.py
```

### 3. Launch Interactive Web Dashboard
Simply open `web_app/index.html` in any web browser to interactively explore all 10 dashboard pages, live charts, slicers, and DAX calculation modal!

---

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
