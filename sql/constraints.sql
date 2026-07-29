-- ============================================================================
-- Foreign Key Constraints & Data Integrity Checks
-- ============================================================================

ALTER TABLE FactOrders
    ADD CONSTRAINT fk_orders_customer FOREIGN KEY (CustomerID) REFERENCES DimCustomers(CustomerID),
    ADD CONSTRAINT fk_orders_product FOREIGN KEY (ProductID) REFERENCES DimProducts(ProductID),
    ADD CONSTRAINT fk_orders_warehouse FOREIGN KEY (WarehouseID) REFERENCES DimWarehouses(WarehouseID),
    ADD CONSTRAINT fk_orders_carrier FOREIGN KEY (CarrierID) REFERENCES DimLogisticsCarriers(CarrierID);

ALTER TABLE FactInventory
    ADD CONSTRAINT fk_inventory_warehouse FOREIGN KEY (WarehouseID) REFERENCES DimWarehouses(WarehouseID),
    ADD CONSTRAINT fk_inventory_product FOREIGN KEY (ProductID) REFERENCES DimProducts(ProductID);

ALTER TABLE FactReturns
    ADD CONSTRAINT fk_returns_order FOREIGN KEY (OrderID) REFERENCES FactOrders(OrderID),
    ADD CONSTRAINT fk_returns_product FOREIGN KEY (ProductID) REFERENCES DimProducts(ProductID);
