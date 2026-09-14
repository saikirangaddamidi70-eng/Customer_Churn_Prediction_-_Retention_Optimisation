# Creating Database 
CREATE DATABASE customer_churn;
USE customer_churn;
#Creating table 
CREATE TABLE customers(
        Customer_ID VARCHAR(20),
        Age INT,
        Gender VARCHAR(20),
        Location VARCHAR(50),
        Tenure INT,
        Contract_Type VARCHAR(30),
        Subscription_Plan VARCHAR(30),
        Monthly_Charges DECIMAL(10,2),
        Total_Charges DECIMAL(12,2),
        Payment_method VARCHAR(30),
        Internet_Service VARCHAR(30),
        Login_Frequency INT,
        Support_Tickets INT,
        COmplaints INT,
        Avg_Session_Duration DECIMAL(10,2),
        Churn INT);
# Basic SQL Analysis
SELECT COUNT(*) AS Total_Customers FROM customers; 
SELECT COUNT(*) AS Churned_Customers FROM customers WHERE Churn = 1;
SELECT COUNT(*) AS Stayed_Customers FROM customers WHERE Churn = 0;
SELECT AVG(Churn) * 100 AS Churn_Rate FROM customers;
# Churn by Contract 
SELECT Contract_Type, COUNT(*) AS Total_Customers, SUM(Churn) AS Churned_Customers, AVG(Churn) * 100 AS Churn_Rate
FROM customers GROUP BY Contract_Type ORDER BY Churn_Rate DESC;
# Churn by Payment method 
SELECT Payment_Method,COUNT(*) AS Customers,AVG(Churn) * 100 AS Churn_Rate FROM customers
GROUP BY Payment_Method ORDER BY Churn_Rate DESC;
# Churn by Tenure
SELECT
    CASE
        WHEN Tenure <= 6 THEN '0-6 Months'
        WHEN Tenure <= 12 THEN '7-12 Months'
        WHEN Tenure <= 24 THEN '13-24 Months'
        ELSE '25+ Months'
    END AS Tenure_Group,
    COUNT(*) AS Customers,
    AVG(Churn) * 100 AS Churn_Rate
FROM customers
GROUP BY
    CASE
        WHEN Tenure <= 6 THEN '0-6 Months'
        WHEN Tenure <= 12 THEN '7-12 Months'
        WHEN Tenure <= 24 THEN '13-24 Months'
        ELSE '25+ Months'
    END
ORDER BY Churn_Rate DESC;
# High-Value Customers
SELECT Customer_ID,Monthly_Charges,Churn FROM customers WHERE Monthly_Charges > 1000;
SELECT Customer_ID,Monthly_Charges,Total_Charges,Churn FROM customers
WHERE Monthly_Charges > 1000 AND Churn = 1;
# Support tickets Vs Churn
SELECT Support_Tickets,COUNT(*) AS Customers,AVG(Churn) * 100 AS Churn_Rate FROM customers
GROUP BY Support_Tickets ORDER BY Support_Tickets;
# Customer-level SQL Analysis
CREATE VIEW customer_churn_analysis AS
SELECT
    Customer_ID,
    Age,
    Gender,
    Location,
    Tenure,
    Contract_Type,
    Subscription_Plan,
    Monthly_Charges,
    Total_Charges,
    Payment_Method,
    Internet_Service,
    Login_Frequency,
    Support_Tickets,
    Complaints,
    Avg_Session_Duration,
    Churn
FROM customers;
SELECT *
FROM customer_churn_analysis;
