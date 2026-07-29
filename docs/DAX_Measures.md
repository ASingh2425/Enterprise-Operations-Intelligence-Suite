# DAX Measures Catalog & Strategy Architecture

## 1. DAX Strategy Overview Table

| Measure Name | Analytical Category | Purpose / Business Function | Formula Summary |
|---|---|---|---|
| **Total Net Revenue** | Financial | Core top-line revenue metric | `SUM(FactOrders[NetRevenue])` |
| **Total Gross Profit** | Financial | Net profitability after COGS & Shipping | `SUM(FactOrders[Profit])` |
| **Gross Margin %** | Financial | Profitability percentage retained | `DIVIDE([Total Gross Profit], [Total Net Revenue], 0)` |
| **Average Order Value** | Financial | Basket size per transaction | `DIVIDE([Total Net Revenue], [Total Orders], 0)` |
| **Revenue YoY Growth %** | Time Intelligence | Year-over-Year revenue growth | `DIVIDE(Current - Prior, Prior, 0)` |
| **Revenue MoM Growth %** | Time Intelligence | Month-over-Month revenue growth | `DIVIDE(Current - Prior, Prior, 0)` |
| **Rolling 12M Revenue** | Time Intelligence | Trailing 12-month revenue trend | `DATESINPERIOD(-12, MONTH)` |
| **YTD Net Revenue** | Time Intelligence | Year-to-Date cumulative revenue | `TOTALYTD([Total Net Revenue])` |
| **Perfect Order Rate %** | Operations SLA | Fulfillment accuracy percentage | `DIVIDE(NotLate & NotReturned, Total, 0)` |
| **On-Time Delivery %** | Operations SLA | Logistics carrier SLA rate | `DIVIDE(OnTimeOrders, TotalOrders, 0)` |
| **Return Rate %** | Operations SLA | Product dissatisfaction rate | `DIVIDE(ReturnedOrders, TotalOrders, 0)` |
| **Economic Order Quantity** | Inventory | Optimal order batch size | `SQRT((2 * Demand * SetupCost) / Holding)` |
| **Days of Inventory (DOI)**| Inventory | Stock capital velocity | `DIVIDE(InventoryValue, DailyCOGS, 0)` |
| **Inventory Turnover** | Inventory | Annual stock replacement frequency | `DIVIDE(365, [Days of Inventory], 0)` |
| **Category Revenue Rank**| Window Functions | Dynamic SKU/Category ranking | `RANKX(ALL(DimProducts[Category]), ...)` |
| **Regional Share %** | Contribution | Percentage of global revenue | `DIVIDE([Net Revenue], ALL(Region), 0)` |

---

## 2. Enterprise DAX Measure Definitions

### 1. Total Net Revenue
```dax
Total Net Revenue = SUM(FactOrders[NetRevenue])
```

### 2. Total Gross Profit
```dax
Total Gross Profit = SUM(FactOrders[Profit])
```

### 3. Gross Margin %
```dax
Gross Margin % = DIVIDE([Total Gross Profit], [Total Net Revenue], 0)
```

### 4. Average Order Value (AOV)
```dax
Average Order Value = DIVIDE([Total Net Revenue], DISTINCTCOUNT(FactOrders[OrderID]), 0)
```

### 5. Perfect Order Rate %
```dax
Perfect Order Rate % = 
DIVIDE(
    CALCULATE(COUNTROWS(FactOrders), FactOrders[IsLate] = 0, FactOrders[IsReturned] = 0),
    COUNTROWS(FactOrders),
    0
)
```

### 6. Revenue YoY Growth %
```dax
Revenue YoY % = 
VAR CurrentRev = [Total Net Revenue]
VAR PriorRev = CALCULATE([Total Net Revenue], SAMEPERIODLASTYEAR('DimCalendar'[FullDate]))
RETURN DIVIDE(CurrentRev - PriorRev, PriorRev, 0)
```

### 7. Rolling 12 Months Revenue
```dax
Rolling 12M Revenue = 
CALCULATE(
    [Total Net Revenue],
    DATESINPERIOD('DimCalendar'[FullDate], MAX('DimCalendar'[FullDate]), -12, MONTH)
)
```

### 8. Economic Order Quantity (EOQ)
```dax
EOQ = 
VAR Demand = [Annualized Demand Units]
VAR SetupCost = 125.0
VAR HoldingCost = AVERAGE(FactInventory[UnitHoldingCost])
RETURN SQRT( DIVIDE(2 * Demand * SetupCost, HoldingCost, 0) )
```

### 9. Days of Inventory (DOI)
```dax
Days of Inventory = 
VAR InventoryValue = SUMX(FactInventory, FactInventory[CurrentStock] * RELATED(DimProducts[Cost]))
VAR DailyCostOfSales = DIVIDE(SUM(FactOrders[COGS]), 365, 0)
RETURN DIVIDE(InventoryValue, DailyCostOfSales, 0)
```

### 10. Regional Revenue Contribution %
```dax
Regional Revenue Contribution % = 
DIVIDE([Total Net Revenue], CALCULATE([Total Net Revenue], REMOVEFILTERS(DimCustomers[Region])), 0)
```
