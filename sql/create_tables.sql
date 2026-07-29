-- ============================================================================
-- Table DDL Statements for Star Schema Tables
-- ============================================================================

-- 1. Calendar Dimension Table
CREATE TABLE IF NOT EXISTS DimCalendar (
    DateKey INT PRIMARY KEY,
    FullDate DATE NOT NULL,
    Year INT NOT NULL,
    Quarter VARCHAR(5) NOT NULL,
    MonthNumber INT NOT NULL,
    MonthName VARCHAR(15) NOT NULL,
    DayOfWeek VARCHAR(15) NOT NULL,
    IsWeekend INT NOT NULL,
    IsHoliday INT NOT NULL
);

-- 2. Customer Dimension Table
CREATE TABLE IF NOT EXISTS DimCustomers (
    CustomerID VARCHAR(20) PRIMARY KEY,
    Segment VARCHAR(30) NOT NULL,
    Region VARCHAR(30) NOT NULL,
    Country VARCHAR(50) NOT NULL,
    City VARCHAR(50) NOT NULL,
    LifetimeValue DECIMAL(12,2) NOT NULL
);

-- 3. Product Dimension Table
CREATE TABLE IF NOT EXISTS DimProducts (
    ProductID VARCHAR(20) PRIMARY KEY,
    SKU VARCHAR(50) UNIQUE NOT NULL,
    Category VARCHAR(50) NOT NULL,
    SubCategory VARCHAR(50) NOT NULL,
    Brand VARCHAR(50) NOT NULL,
    Cost DECIMAL(10,2) NOT NULL,
    SellingPrice DECIMAL(10,2) NOT NULL,
    Margin DECIMAL(5,4) NOT NULL
);

-- 4. Warehouse Dimension Table
CREATE TABLE IF NOT EXISTS DimWarehouses (
    WarehouseID VARCHAR(20) PRIMARY KEY,
    WarehouseName VARCHAR(100) NOT NULL,
    City VARCHAR(50) NOT NULL,
    Country VARCHAR(50) NOT NULL,
    CapacityUnits INT NOT NULL,
    OperatingCost DECIMAL(12,2) NOT NULL
);

-- 5. Supplier Dimension Table
CREATE TABLE IF NOT EXISTS DimSuppliers (
    SupplierID VARCHAR(20) PRIMARY KEY,
    SupplierName VARCHAR(100) NOT NULL,
    Country VARCHAR(50) NOT NULL,
    Rating DECIMAL(3,2) NOT NULL,
    AvgDeliveryDays DECIMAL(4,1) NOT NULL,
    DefectRate DECIMAL(5,4) NOT NULL,
    SupplierRiskIndex DECIMAL(6,2) NOT NULL
);

-- 6. Logistics Carrier Dimension Table
CREATE TABLE IF NOT EXISTS DimLogisticsCarriers (
    CarrierID VARCHAR(20) PRIMARY KEY,
    CarrierName VARCHAR(100) NOT NULL,
    ReliabilityScore DECIMAL(3,2) NOT NULL,
    BaseRatePerKm DECIMAL(6,2) NOT NULL
);

-- 7. Inventory Fact / Snapshot Table
CREATE TABLE IF NOT EXISTS FactInventory (
    InventoryID SERIAL PRIMARY KEY,
    WarehouseID VARCHAR(20) NOT NULL,
    ProductID VARCHAR(20) NOT NULL,
    SKU VARCHAR(50) NOT NULL,
    CurrentStock INT NOT NULL,
    ReorderPoint INT NOT NULL,
    LeadTimeDays INT NOT NULL,
    UnitHoldingCost DECIMAL(8,2) NOT NULL,
    StockoutRiskScore DECIMAL(5,3) NOT NULL
);

-- 8. Fact Orders Table (Central Transaction Table)
CREATE TABLE IF NOT EXISTS FactOrders (
    OrderID VARCHAR(20) PRIMARY KEY,
    OrderDate DATE NOT NULL,
    CustomerID VARCHAR(20) NOT NULL,
    ProductID VARCHAR(20) NOT NULL,
    WarehouseID VARCHAR(20) NOT NULL,
    CarrierID VARCHAR(20) NOT NULL,
    Quantity INT NOT NULL,
    UnitPrice DECIMAL(10,2) NOT NULL,
    UnitCost DECIMAL(10,2) NOT NULL,
    DiscountRate DECIMAL(4,2) NOT NULL,
    GrossRevenue DECIMAL(12,2) NOT NULL,
    NetRevenue DECIMAL(12,2) NOT NULL,
    COGS DECIMAL(12,2) NOT NULL,
    ShippingCost DECIMAL(10,2) NOT NULL,
    Profit DECIMAL(12,2) NOT NULL,
    TransitDays INT NOT NULL,
    PromisedDays INT NOT NULL,
    IsLate INT NOT NULL
);

-- 9. Fact Returns Table
CREATE TABLE IF NOT EXISTS FactReturns (
    ReturnID VARCHAR(20) PRIMARY KEY,
    OrderID VARCHAR(20) NOT NULL,
    ReturnDate DATE NOT NULL,
    ProductID VARCHAR(20) NOT NULL,
    ReturnReason VARCHAR(50) NOT NULL,
    RefundAmount DECIMAL(12,2) NOT NULL,
    RestockFee DECIMAL(10,2) NOT NULL
);
