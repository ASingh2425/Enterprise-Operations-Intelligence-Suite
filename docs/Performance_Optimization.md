# Performance Optimization & VertiPaq Tuning Guide

## 1. Power BI VertiPaq Column Encoding
- High-cardinality floating-point numbers (`GrossRevenue`, `NetRevenue`) rounded to 2 decimal places to maximize dictionary encoding efficiency.
- Auto date/time hierarchy generation disabled globally in Power BI options to reduce hidden metadata model overhead.

## 2. DAX Optimization Rules
- Replaced `FILTER(ALL(FactOrders), ...)` statements with targeted `KEEPFILTERS` and `REMOVEFILTERS`.
- Replaced iterative `SUMX` logic with column-level vector arithmetic where feasible.

## 3. SQL Query Tuning
- Primary and Foreign Key indexes created on all join columns.
- Analytical views aggregate transactional data to monthly grains for high-level executive summaries.
