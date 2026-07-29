-- ============================================================================
-- Enterprise Operations Intelligence Suite
-- Database Schema Definition & Setup
-- Target RDBMS: PostgreSQL / Snowflake / MS SQL Server
-- Author: Senior BI Analyst (Amazon Operations Intelligence Team)
-- ============================================================================

CREATE SCHEMA IF NOT EXISTS ops_intelligence;
SET search_path TO ops_intelligence;

-- Schema Description:
-- Star Schema architecture centered around Fact_Orders and Fact_Returns
-- with dimension tables: Dim_Customers, Dim_Products, Dim_Warehouses,
-- Dim_Suppliers, Dim_Logistics_Carriers, Dim_Calendar, and Fact_Inventory.
