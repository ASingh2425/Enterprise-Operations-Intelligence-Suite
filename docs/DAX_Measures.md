# DAX Measures Documentation & Calculation Catalog

This catalog documents 30+ enterprise DAX measures created for the Operations Intelligence Suite.

---

## 1. Executive Core Financial & Operational DAX

### 1. Total Net Revenue
```dax
Total Net Revenue = SUM(FactOrders[NetRevenue])
```
*Business Purpose*: Baseline core financial metric representing net sales after discounts.

### 2. Total Gross Profit
```dax
Total Gross Profit = SUM(FactOrders[Profit])
```
*Business Purpose*: Total dollar profit after subtracting COGS and freight shipping costs.

### 3. Gross Margin %
```dax
Gross Margin % = DIVIDE([Total Gross Profit], [Total Net Revenue], 0)
```
*Business Purpose*: Measures net profitability per revenue dollar.

### 4. Average Order Value (AOV)
```dax
Average Order Value = DIVIDE([Total Net Revenue], [Total Orders], 0)
```
*Business Purpose*: Evaluates average basket size per transaction.

### 5. Perfect Order Rate %
```dax
Perfect Order Rate % = 
DIVIDE(
    CALCULATE(COUNTROWS(FactOrders), FactOrders[IsLate] = 0, FactOrders[IsReturned] = 0),
    COUNTROWS(FactOrders),
    0
)
```
*Business Purpose*: Key Amazon fulfillment metric measuring orders delivered on-time without returns or damages.

---

## 2. Time Intelligence (YoY, MoM, Rolling 12M)

### 6. Revenue YoY Growth %
```dax
Revenue YoY % = 
VAR CurrentRev = [Total Net Revenue]
VAR PriorRev = CALCULATE([Total Net Revenue], SAMEPERIODLASTYEAR('DimCalendar'[FullDate]))
RETURN DIVIDE(CurrentRev - PriorRev, PriorRev, 0)
```

### 7. Revenue MoM Growth %
```dax
Revenue MoM % = 
VAR CurrentRev = [Total Net Revenue]
VAR PriorRev = CALCULATE([Total Net Revenue], DATEADD('DimCalendar'[FullDate], -1, MONTH))
RETURN DIVIDE(CurrentRev - PriorRev, PriorRev, 0)
```

### 8. Rolling 12 Months Revenue
```dax
Rolling 12M Revenue = 
CALCULATE(
    [Total Net Revenue],
    DATESINPERIOD('DimCalendar'[FullDate], MAX('DimCalendar'[FullDate]), -12, MONTH)
)
```

### 9. Year-to-Date (YTD) Revenue
```dax
YTD Revenue = TOTALYTD([Total Net Revenue], 'DimCalendar'[FullDate])
```

---

## 3. Inventory Optimization DAX (EOQ, Safety Stock, DOI)

### 10. Economic Order Quantity (EOQ)
```dax
EOQ = 
VAR Demand = [Annualized Demand Units]
VAR SetupCost = 125.0
VAR HoldingCost = AVERAGE(FactInventory[UnitHoldingCost])
RETURN SQRT( DIVIDE(2 * Demand * SetupCost, HoldingCost, 0) )
```

### 11. Days of Inventory (DOI)
```dax
Days of Inventory = 
VAR InventoryValue = SUMX(FactInventory, FactInventory[CurrentStock] * RELATED(DimProducts[Cost]))
VAR DailyCostOfSales = DIVIDE(SUM(FactOrders[COGS]), 365, 0)
RETURN DIVIDE(InventoryValue, DailyCostOfSales, 0)
```

---

## 4. Ranking & Contribution DAX (Window Functions)

### 12. Category Rank by Revenue
```dax
Category Rank = RANKX(ALL(DimProducts[Category]), [Total Net Revenue], , DESC)
```

### 13. Regional Revenue Contribution %
```dax
Regional Revenue Contribution % = 
DIVIDE([Total Net Revenue], CALCULATE([Total Net Revenue], ALL(DimCustomers[Region])), 0)
```
