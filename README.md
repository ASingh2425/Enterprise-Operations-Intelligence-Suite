# 🚀 Enterprise Operations Intelligence Suite

[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen?style=for-the-badge&logo=github)](https://github.com/ASingh2425/Enterprise-Operations-Intelligence-Suite)
[![Power BI](https://img.shields.io/badge/Power_BI-Dark_Navy_Theme-yellow?style=for-the-badge&logo=powerbi)](https://github.com/ASingh2425/Enterprise-Operations-Intelligence-Suite)
[![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)](https://github.com/ASingh2425/Enterprise-Operations-Intelligence-Suite)
[![SQL](https://img.shields.io/badge/SQL-PostgreSQL%2FSnowflake-orange?style=for-the-badge&logo=postgresql)](https://github.com/ASingh2425/Enterprise-Operations-Intelligence-Suite)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

> **End-to-End Supply Chain & Business Analytics Platform** simulating the work of a **Senior Business Intelligence Analyst at Amazon**.

Target Repository: [ASingh2425/Enterprise-Operations-Intelligence-Suite](https://github.com/ASingh2425/Enterprise-Operations-Intelligence-Suite)

---

## 📌 Executive Summary & Scope

The **Operations Intelligence Suite** is a production-quality Business Intelligence solution built to answer strategic business questions, identify operational inefficiencies across global fulfillment networks, forecast future demand, and support executive decision-making.

### In-Scope Functional Modules
- **Sales Performance**: Revenue trends, AOV, category margin analysis, and product profitability.
- **Customer Analytics**: RFM quantile segmentation, lifetime value (LTV) modeling, and churn risk detection.
- **Inventory Optimization**: Pareto ABC classification, Economic Order Quantity (EOQ), Safety Stock buffers, and Days of Inventory (DOI).
- **Supplier Performance**: Vendor defect rate analysis, delivery lead time monitoring, and composite supplier risk index.
- **Warehouse Operations**: Fulfillment center capacity utilization, inventory valuation, and stockout probability modeling.
- **Logistics & Freight Performance**: Carrier SLA on-time delivery rates, transit time latency, and geographic route shipping costs.
- **Financial Analysis**: Gross sales to net profit waterfall breakdown, discount impact, and margin variance.
- **Demand Forecasting**: 30, 60, 90, and 180-day time-series demand predictions with 95% confidence intervals.
- **Executive KPI Monitoring**: C-suite KPI cards, YoY/MoM performance indicators, and rolling 12-month trends.
- **Risk & Anomaly Monitoring**: Z-score and Isolation Forest outlier detection for freight costs and margin compression.

---

## 🖥️ 10 Interactive Dashboard Pages & KPI Mapping

| Page | Name | Primary Assigned KPIs | Target Stakeholder |
|---|---|---|---|
| 1 | **Executive Dashboard** | Net Revenue, Gross Profit, Perfect Order Rate %, Return Rate % | VP Global Supply Chain, C-Suite |
| 2 | **Sales Analytics** | Net Revenue, Gross Margin %, Average Order Value (AOV) | Category Managers, Merchandising |
| 3 | **Supply Chain Analytics** | FC Capacity Utilization %, Supplier Risk Index, Defect Rate % | Fulfillment Managers, Procurement |
| 4 | **Logistics Dashboard** | Carrier On-Time SLA %, Route Shipping Cost, Transit Days | Logistics Director, Fleet Ops |
| 5 | **Demand Forecasting** | 180-Day Predicted Demand, 95% Confidence Band, MAPE, RMSE | Demand Planners, Supply Chain |
| 6 | **Customer Intelligence** | RFM Segment Distribution, Customer Lifetime Value (LTV) | Customer Success Lead, Marketing |
| 7 | **Profitability Analysis** | Gross Revenue, Net Revenue, COGS, Net Profit Waterfall Flow | CFO, Financial Analysts |
| 8 | **Inventory Optimization** | ABC Pareto Revenue Share, Days of Inventory (DOI), EOQ | Warehouse Operations, Inventory Leads |
| 9 | **Risk Monitoring** | Anomaly Incident Count, Stockout Risk Score | Operations Risk Lead, Steering Comm. |
| 10| **Executive AI Insights** | Strategic Operational Impact Score, Priority Action Cards | Executive Committee, C-Suite |

---

## 📚 Master Documentation Index

| Document | Purpose |
|---|---|
| [Business_Problem.md](docs/Business_Problem.md) | Quantified problem statement, scope, success metrics, assumptions, risks & deliverables |
| [Business_Requirements.md](docs/Business_Requirements.md) | User stories, stakeholder personas, acceptance criteria, and non-functional requirements |
| [KPI_Definitions.md](docs/KPI_Definitions.md) | Mathematical formulas, target benchmarks, disclaimers, and dashboard page mapping matrix |
| [Dashboard_Specification.md](docs/Dashboard_Specification.md) | Page-by-page visual layout, visual types, slicers, and interaction specifications |
| [Data_Dictionary.md](docs/Data_Dictionary.md) | Physical schema types, primary/foreign keys, constraints, and business descriptions |
| [Data_Model.md](docs/Data_Model.md) | Star Schema topology, cardinality, filter directions, and VertiPaq tuning rules |
| [Project_Architecture.md](docs/Project_Architecture.md) | End-to-end workflow diagram, tech stack justification, and pipeline specifications |
| [ETL_Documentation.md](docs/ETL_Documentation.md) | Ingestion steps, deduplication, missing value treatment, and winsorization rules |
| [SQL_Documentation.md](docs/SQL_Documentation.md) | RDBMS schema, indexes, views, and complex Amazon BI analyst queries |
| [DAX_Measures.md](docs/DAX_Measures.md) | Catalog of 30+ enterprise DAX measures with code blocks and formula explanations |
| [Performance_Optimization.md](docs/Performance_Optimization.md) | VertiPaq encoding rules, DAX tuning, and SQL index optimizations |
| [Testing_Report.md](docs/Testing_Report.md) | Quality assurance audit, row count checks, and measure verification |
| [Future_Enhancements.md](docs/Future_Enhancements.md) | Microsoft Fabric, Apache Kafka streaming, and NeuralProphet roadmap |

---

## ⚡ Quick Start & Setup Guide

### 1. Prerequisites
- Python 3.10+
- Modern Web Browser (Chrome / Edge / Firefox)
- Power BI Desktop (Optional)

### 2. Execution & Launch
```bash
# Clone the repository
git clone https://github.com/ASingh2425/Enterprise-Operations-Intelligence-Suite.git
cd Enterprise-Operations-Intelligence-Suite

# Install dependencies
pip install -r requirements.txt

# Run Python ETL & Analytics Pipeline
python python/generate_raw_data.py
python python/data_cleaning.py
python python/feature_engineering.py
python python/forecasting.py
python python/customer_segmentation.py
python python/inventory_analysis.py
python python/anomaly_detection.py
python python/generate_insights.py
```

Simply open `index.html` in your browser to interactively explore the live dashboard!

---

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
