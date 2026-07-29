-- ============================================================================
-- Business Intelligence Analytical Views
-- Designed for Power BI Power Query DirectQuery & Import Layer
-- ============================================================================

-- 1. Executive Summary Monthly View
CREATE OR REPLACE VIEW vw_ExecutiveMonthlySummary AS
SELECT 
    DATE_TRUNC('month', o.OrderDate) AS MonthYear,
    COUNT(DISTINCT o.OrderID) AS TotalOrders,
    COUNT(DISTINCT o.CustomerID) AS ActiveCustomers,
    SUM(o.NetRevenue) AS TotalRevenue,
    SUM(o.Profit) AS TotalProfit,
    ROUND((SUM(o.Profit) / NULLIF(SUM(o.NetRevenue), 0)) * 100, 2) AS ProfitMarginPct,
    ROUND(SUM(o.NetRevenue) / NULLIF(COUNT(DISTINCT o.OrderID), 0), 2) AS AvgOrderValue,
    ROUND((SUM(CASE WHEN o.IsLate = 1 THEN 1 ELSE 0 END)::DECIMAL / COUNT(o.OrderID)) * 100, 2) AS LateDeliveryPct
FROM FactOrders o
GROUP BY 1;

-- 2. Warehouse & Inventory Performance View
CREATE OR REPLACE VIEW vw_WarehouseInventoryStatus AS
SELECT 
    w.WarehouseID,
    w.WarehouseName,
    w.City,
    w.Country,
    COUNT(i.ProductID) AS TotalSKUs,
    SUM(i.CurrentStock) AS TotalStockUnits,
    SUM(i.CurrentStock * p.Cost) AS TotalInventoryValue,
    SUM(CASE WHEN i.CurrentStock <= i.ReorderPoint THEN 1 ELSE 0 END) AS SKUsBelowReorderPoint,
    ROUND(AVG(i.StockoutRiskScore), 3) AS AvgStockoutRisk
FROM DimWarehouses w
JOIN FactInventory i ON w.WarehouseID = i.WarehouseID
JOIN DimProducts p ON i.ProductID = p.ProductID
GROUP BY 1, 2, 3, 4;

-- 3. Supplier Defect & SLA Compliance View
CREATE OR REPLACE VIEW vw_SupplierPerformanceScorecard AS
SELECT 
    SupplierID,
    SupplierName,
    Country,
    Rating,
    AvgDeliveryDays,
    DefectRate,
    SupplierRiskIndex,
    CASE 
        WHEN DefectRate > 0.03 OR Rating < 3.5 THEN 'High Risk - Audit Required'
        WHEN DefectRate BETWEEN 0.015 AND 0.03 THEN 'Medium Risk - Monitor'
        ELSE 'Preferred Supplier'
    END AS SupplierStatus
FROM DimSuppliers;
