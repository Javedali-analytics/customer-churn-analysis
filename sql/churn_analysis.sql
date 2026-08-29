-- Customer Churn Analysis - SQL Script

CREATE DATABASE IF NOT EXISTS churn_analysis;
USE churn_analysis;

CREATE TABLE IF NOT EXISTS churn_cleaned (
    CustomerID VARCHAR(20) PRIMARY KEY,
    `Count` INT,
    Country VARCHAR(100),
    State VARCHAR(100),
    City VARCHAR(100),
    `Zip Code` INT,
    `Lat Long` VARCHAR(50),
    Latitude DECIMAL(10,6),
    Longitude DECIMAL(10,6),
    Gender VARCHAR(20),
    `Senior Citizen` VARCHAR(10),
    Partner VARCHAR(10),
    Dependents VARCHAR(10),
    `Tenure Months` INT,
    `Phone Service` VARCHAR(10),
    `Multiple Lines` VARCHAR(50),
    `Internet Service` VARCHAR(50),
    `Online Security` VARCHAR(50),
    `Online Backup` VARCHAR(50),
    `Device Protection` VARCHAR(50),
    `Tech Support` VARCHAR(50),
    `Streaming TV` VARCHAR(50),
    `Streaming Movies` VARCHAR(50),
    Contract VARCHAR(50),
    `Paperless Billing` VARCHAR(10),
    `Payment Method` VARCHAR(100),
    `Monthly Charges` DECIMAL(10,2),
    Monthly_Charge_Band VARCHAR(30),
    `Total Charges` DECIMAL(12,2),
    `Churn Label` VARCHAR(10),
    `Churn Value` INT,
    `Churn Score` INT,
    CLTV INT,
    `Churn Reason` VARCHAR(255)
);

-- Basic validation
SELECT COUNT(*) AS total_customers
FROM churn_cleaned;

SELECT CustomerID, COUNT(*) AS duplicate_count
FROM churn_cleaned
GROUP BY CustomerID
HAVING COUNT(*) > 1;

SELECT COUNT(*) AS missing_churn_reason
FROM churn_cleaned
WHERE `Churn Reason` IS NULL OR `Churn Reason` = '';

-- Overall churn
SELECT
    COUNT(*) AS total_customers,
    SUM(`Churn Value`) AS churned_customers,
    ROUND(SUM(`Churn Value`) * 100.0 / COUNT(*), 2) AS churn_rate_percentage
FROM churn_cleaned;

-- Churn by Contract
SELECT
    Contract,
    COUNT(*) AS total_customers,
    SUM(`Churn Value`) AS churned_customers,
    ROUND(SUM(`Churn Value`) * 100.0 / COUNT(*), 2) AS churn_rate_percentage
FROM churn_cleaned
GROUP BY Contract
ORDER BY churn_rate_percentage DESC;

-- Churn by Internet Service
SELECT
    `Internet Service`,
    COUNT(*) AS total_customers,
    SUM(`Churn Value`) AS churned_customers,
    ROUND(SUM(`Churn Value`) * 100.0 / COUNT(*), 2) AS churn_rate_percentage
FROM churn_cleaned
GROUP BY `Internet Service`
ORDER BY churn_rate_percentage DESC;

-- Churn by Payment Method
SELECT
    `Payment Method`,
    COUNT(*) AS total_customers,
    SUM(`Churn Value`) AS churned_customers,
    ROUND(SUM(`Churn Value`) * 100.0 / COUNT(*), 2) AS churn_rate_percentage
FROM churn_cleaned
GROUP BY `Payment Method`
ORDER BY churn_rate_percentage DESC;

-- Churn by Tenure
SELECT
    `Tenure Months`,
    COUNT(*) AS total_customers,
    SUM(`Churn Value`) AS churned_customers,
    ROUND(SUM(`Churn Value`) * 100.0 / COUNT(*), 2) AS churn_rate_percentage
FROM churn_cleaned
GROUP BY `Tenure Months`
ORDER BY `Tenure Months`;

-- Churn by Monthly Charge Band
SELECT
    Monthly_Charge_Band,
    COUNT(*) AS total_customers,
    SUM(`Churn Value`) AS churned_customers,
    ROUND(SUM(`Churn Value`) * 100.0 / COUNT(*), 2) AS churn_rate_percentage
FROM churn_cleaned
GROUP BY Monthly_Charge_Band
ORDER BY churn_rate_percentage DESC;

-- Churn by Online Security
SELECT
    `Online Security`,
    COUNT(*) AS total_customers,
    SUM(`Churn Value`) AS churned_customers,
    ROUND(SUM(`Churn Value`) * 100.0 / COUNT(*), 2) AS churn_rate_percentage
FROM churn_cleaned
GROUP BY `Online Security`
ORDER BY churn_rate_percentage DESC;

-- Churn by Senior Citizen
SELECT
    `Senior Citizen`,
    COUNT(*) AS total_customers,
    SUM(`Churn Value`) AS churned_customers,
    ROUND(SUM(`Churn Value`) * 100.0 / COUNT(*), 2) AS churn_rate_percentage
FROM churn_cleaned
GROUP BY `Senior Citizen`
ORDER BY churn_rate_percentage DESC;

-- High-risk combinations
SELECT
    Contract,
    `Internet Service`,
    `Payment Method`,
    COUNT(*) AS total_customers,
    SUM(`Churn Value`) AS churned_customers,
    ROUND(SUM(`Churn Value`) * 100.0 / COUNT(*), 2) AS churn_rate_percentage
FROM churn_cleaned
GROUP BY Contract, `Internet Service`, `Payment Method`
HAVING COUNT(*) >= 20
ORDER BY churn_rate_percentage DESC;
