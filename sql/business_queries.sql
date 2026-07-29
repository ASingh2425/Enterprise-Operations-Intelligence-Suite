-- ============================================================================
-- Business Analytical Queries (Amazon Senior BI Analyst Scenarios)
-- ============================================================================

-- Query 1: Top 10 High-Volume Products with Declining Margin & High Return Rates
SELECT 
    p.ProductID,
    p.SKU,
    p.Category,
    SUM(o.Quantity) AS TotalUnitsSold,
    SUM(o.NetRevenue) AS TotalRevenue,
    SUM(o.Profit) AS TotalProfit,
    ROUND((SUM(o.Profit) / NULLIF(SUM(o.NetRevenue), 0)) * 100, 2) AS ProfitMarginPct,
    COUNT(r.ReturnID) AS ReturnCount,
    ROUND((COUNT(r.ReturnID)::DECIMAL / NULLIF(COUNT(o.OrderID), 0)) * 100, 2) AS ReturnRatePct
FROM FactOrders o
JOIN DimProducts p ON o.ProductID = p.ProductID
LEFT JOIN FactReturns r ON o.OrderID = r.OrderID
GROUP BY 1, 2, 3
HAVING COUNT(o.OrderID) > 100
ORDER BY ReturnRatePct DESC, ProfitMarginPct ASC
LIMIT 10;

-- Query 2: Carrier Reliability & Shipping Cost Efficiency Window Functions
SELECT 
    c.CarrierName,
    COUNT(o.OrderID) AS TotalShipments,
    SUM(o.ShippingCost) AS TotalShippingCost,
    ROUND(AVG(o.ShippingCost), 2) AS AvgShippingCostPerOrder,
    ROUND(AVG(o.TransitDays), 2) AS AvgTransitDays,
    ROUND((SUM(CASE WHEN o.IsLate = 1 THEN 1 ELSE 0 END)::DECIMAL / COUNT(o.OrderID)) * 100, 2) AS LatePct,
    DENSE_RANK() OVER (ORDER BY (SUM(CASE WHEN o.IsLate = 1 THEN 1 ELSE 0 END)::DECIMAL / COUNT(o.OrderID)) ASC) AS ReliabilityRank
FROM FactOrders o
JOIN DimLogisticsCarriers c ON o.CarrierID = c.CarrierID
GROUP BY 1
ORDER BY ReliabilityRank ASC;

-- Query 3: Regional Customer RFM Segmentation Distribution
WITH CustomerMetrics AS (
    SELECT 
        o.CustomerID,
        c.Region,
        c.Segment,
        MAX(o.OrderDate) AS LastOrderDate,
        COUNT(DISTINCT o.OrderID) AS OrderFrequency,
        SUM(o.NetRevenue) AS TotalSpend
    FROM FactOrders o
    JOIN DimCustomers c ON o.CustomerID = c.CustomerID
    GROUP BY 1, 2, 3
)
SELECT 
    Region,
    Segment,
    COUNT(CustomerID) AS TotalCustomers,
    ROUND(AVG(OrderFrequency), 1) AS AvgOrderFrequency,
    ROUND(AVG(TotalSpend), 2) AS AvgLifetimeSpend
FROM CustomerMetrics
GROUP BY 1, 2
ORDER BY TotalCustomers DESC;
