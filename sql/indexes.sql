-- ============================================================================
-- Analytical Database Performance Indexes
-- Designed for High-Throughput Aggregations & Joins
-- ============================================================================

CREATE INDEX idx_orders_orderdate ON FactOrders(OrderDate);
CREATE INDEX idx_orders_customer ON FactOrders(CustomerID);
CREATE INDEX idx_orders_product ON FactOrders(ProductID);
CREATE INDEX idx_orders_warehouse ON FactOrders(WarehouseID);
CREATE INDEX idx_orders_carrier ON FactOrders(CarrierID);
CREATE INDEX idx_orders_is_late ON FactOrders(IsLate);

CREATE INDEX idx_inventory_product ON FactInventory(ProductID);
CREATE INDEX idx_inventory_warehouse ON FactInventory(WarehouseID);
CREATE INDEX idx_returns_order ON FactReturns(OrderID);
