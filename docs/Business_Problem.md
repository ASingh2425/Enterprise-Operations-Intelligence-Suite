# Phase 1: Business Problem Statement, Stakeholder Alignment & KPI Definitions

## 1. Executive Context & Business Problem
A multinational e-commerce enterprise operating at the scale of **Amazon Global Operations** processes hundreds of thousands of daily customer transactions across multiple regional fulfillment centers, logistics carriers, and international supplier networks.

Despite massive operational volume, executive management and supply chain directors face critical operational bottlenecks:
- **Fragmented Visibility**: Data silos between Warehouse Management Systems (WMS), Transportation Management Systems (TMS), Supplier Quality Databases, and Sales CRM.
- **Suboptimal Capital Allocation**: High holding costs (~$420K+ tied up in overstocked warehouses) occurring simultaneously with stockouts in high-demand technology SKUs.
- **Carrier & Supplier SLA Slippage**: Carrier delay rates exceeding 5% and supplier defect rates surpassing the 1.5% quality threshold, leading to customer churn and inflated return refund amounts.
- **Reactive Executive Decision-Making**: Lack of automated predictive analytics (demand forecasting, anomaly alerts, RFM segmentation) to trigger proactive operational corrections.

---

## 2. Core Stakeholders & Requirements Matrix

| Stakeholder Role | Primary Strategic Concern | Target Insights & Requirements |
|---|---|---|
| **VP of Global Supply Chain** | Overall network throughput, inventory health, perfect order compliance | Executive KPI summary, Perfect Order Rate %, regional fulfillment capacity |
| **Director of Logistics & Transportation** | Carrier SLA performance, transit latency, freight cost efficiency | Carrier SLA on-time %, route cost comparison, late delivery heatmaps |
| **Warehouse Operations Managers** | Fulfillment center utilization, inventory aging, reorder alerts | Days of Inventory (DOI), EOQ batch sizes, safety stock breach alerts |
| **Category Managers / Merchandising** | Product margin, sales trends, inventory turnover | Category revenue trends, top/bottom margin SKUs, ABC Pareto classification |
| **Vendor Management Lead** | Supplier reliability, defect rates, procurement risk | Supplier risk index, vendor defect rate %, delivery lead times |
| **Customer Retention Lead** | Customer LTV, churn risk, return rates | RFM customer segmentation, return reason breakdown, LTV analysis |

---

## 3. Comprehensive Enterprise KPI Definitions

### Financial Performance KPIs
1. **Net Revenue ($)**: `Gross Revenue - Promotional Discounts`
   - *Target*: > $140M annually
   - *Business Importance*: Measures top-line net revenue after price adjustments.
2. **Gross Profit ($)**: `Net Revenue - COGS - Shipping Cost`
   - *Target*: > $45M annually
   - *Business Importance*: Actual net profit generated after direct product costs and freight shipping.
3. **Gross Margin (%)**: `(Gross Profit / Net Revenue) * 100`
   - *Target*: > 32.0%
   - *Business Importance*: Indicates cost efficiency and pricing power across categories.
4. **Average Order Value (AOV)**: `Net Revenue / Total Orders`
   - *Target*: > $270.00
   - *Business Importance*: Tracks average basket spending per transaction.

### Supply Chain & Fulfillment KPIs
5. **Perfect Order Rate (%)**: `(Orders Delivered On-Time & Non-Returned / Total Orders) * 100`
   - *Target*: > 93.5%
   - *Business Importance*: Primary Amazon operational metric for end-to-end fulfillment success.
6. **On-Time Delivery Rate (%)**: `(Orders Delivered <= Promised SLA / Total Orders) * 100`
   - *Target*: > 95.0%
   - *Business Importance*: Measures logistics carrier SLA compliance.
7. **Return Rate (%)**: `(Returned Orders / Total Orders) * 100`
   - *Target*: < 5.0%
   - *Business Importance*: Evaluates product quality and order accuracy.
8. **Fill Rate (%)**: `(Orders Shipped Complete / Total Orders Placed) * 100`
   - *Target*: > 98.0%
   - *Business Importance*: Measures immediate stock availability against customer demand.

### Inventory Optimization KPIs
9. **Economic Order Quantity (EOQ)**: $\sqrt{\frac{2 \times D \times S}{H}}$
   - *Where*: $D$ = Annual Demand Units, $S$ = Setup/Ordering Cost ($125), $H$ = Annual Unit Holding Cost.
   - *Business Importance*: Minimizes combined holding and reorder expenses.
10. **Safety Stock Level**: $Z \times \sqrt{\text{LeadTime}} \times \sigma_{\text{DailyDemand}}$
    - *Where*: $Z = 1.65$ (95% Service Level).
    - *Business Importance*: Buffer stock required to prevent stockout incidents during lead time delays.
11. **Days of Inventory (DOI)**: `(Current Inventory Value / Daily COGS)`
    - *Target*: 30 - 45 Days
    - *Business Importance*: Quantifies capital velocity and stockholding efficiency.
12. **Inventory Turnover Ratio**: `365 / Days of Inventory`
    - *Target*: 8.0x - 12.0x annually
    - *Business Importance*: Measures how rapidly inventory is sold and replaced.

### Supplier & Risk Monitoring KPIs
13. **Supplier Risk Index**: `(5 - Vendor Rating)*15 + (Defect Rate * 1000) + (Avg Delivery Days * 1.5)`
    - *Target*: < 30.0 (Low Risk)
    - *Business Importance*: Multi-criteria vendor score identifying high-risk suppliers needing audits or replacement.
14. **Stockout Probability Index**: `(Reorder Point - Current Stock) / Reorder Point`
    - *Target*: < 0.15
    - *Business Importance*: Early warning metric flagging SKUs approaching safety stock breach.

---

## 4. Phase 1 Milestone Verification
- ✅ Business problem statement aligned with Amazon BI Analyst standards.
- ✅ Stakeholder requirements matrix established across 6 executive/operational personas.
- ✅ Master KPI dictionary defined with mathematical formulas, target benchmarks, and business justifications.
