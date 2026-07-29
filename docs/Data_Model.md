# Data Model Architecture & Relationship Diagram

## 1. Schema Design Pattern
The data model uses a optimized **Star Schema** pattern designed for high-performance Power BI VertiPaq engine compression.

```
                   +------------------+
                   |   DimCalendar    |
                   +------------------+
                            | (1)
                            | 
                            | (*)
+------------------+       +------------------+       +------------------+
|   DimCustomers   |-------|    FactOrders    |-------|   DimProducts    |
+------------------+ (1)(*)+------------------+(*)(1) +------------------+
                            | (*)        | (*)
                            |            |
                        (1) |        (1) |
       +------------------+            +-----------------------+
       |  DimWarehouses   |            | DimLogisticsCarriers  |
       +------------------+            +-----------------------+
```

## 2. Cardinality & Cross Filtering
- All relationships between Fact and Dimension tables are **1-to-Many (1:*)**.
- Cross-filter direction is enforced as **Single Direction** (Dimension filters Fact) to preserve DAX measure execution speed and eliminate bidirectional ambiguity.
