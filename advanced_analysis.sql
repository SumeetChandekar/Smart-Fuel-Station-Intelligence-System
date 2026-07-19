/*============================================================
SMART FUEL STATION INTELLIGENCE SYSTEM
ADVANCED SQL ANALYSIS

Author : Sumeet Chandekar
============================================================*/


------------------------------------------------------------
-- 1 Top 10 Revenue Generating Customers
------------------------------------------------------------

SELECT
    c.Customer_Name,
    c.City,
    COUNT(*) AS Visits,
    ROUND(SUM(t.Total_Amount),2) AS Revenue
FROM Transactions t
JOIN Customers c
ON c.Customer_ID=t.Customer_ID
GROUP BY c.Customer_ID
ORDER BY Revenue DESC
LIMIT 10;


------------------------------------------------------------
-- 2 Revenue Rank of Every Station
------------------------------------------------------------

SELECT

Station_ID,

ROUND(SUM(Total_Amount),2) Revenue,

RANK() OVER(

ORDER BY SUM(Total_Amount) DESC

) Revenue_Rank

FROM Transactions

GROUP BY Station_ID;


------------------------------------------------------------
-- 3 Top Employee of Every Station
------------------------------------------------------------

WITH EmployeeRevenue AS
(
SELECT

Station_ID,

Employee_ID,

SUM(Total_Amount) Revenue

FROM Transactions

GROUP BY
Station_ID,
Employee_ID
)

SELECT *

FROM EmployeeRevenue
ORDER BY Revenue DESC;


------------------------------------------------------------
-- 4 Monthly Growth
------------------------------------------------------------

SELECT

strftime('%Y-%m',Transaction_Date) Month,

SUM(Total_Amount) Revenue,

LAG(SUM(Total_Amount))
OVER(
ORDER BY strftime('%Y-%m',Transaction_Date)
)
Previous_Month

FROM Transactions

GROUP BY Month;


------------------------------------------------------------
-- 5 Running Revenue
------------------------------------------------------------

SELECT

Transaction_Date,

SUM(Total_Amount)

OVER(

ORDER BY Transaction_Date

)

Running_Revenue

FROM Transactions;


------------------------------------------------------------
-- 6 Highest Bill Generated
------------------------------------------------------------

SELECT *

FROM Transactions

ORDER BY Total_Amount DESC

LIMIT 20;


------------------------------------------------------------
-- 7 Lowest Bill
------------------------------------------------------------

SELECT *

FROM Transactions

ORDER BY Total_Amount

LIMIT 20;


------------------------------------------------------------
-- 8 Average Revenue Per Station
------------------------------------------------------------

SELECT

Station_ID,

ROUND(AVG(Total_Amount),2)

FROM Transactions

GROUP BY Station_ID;


------------------------------------------------------------
-- 9 Revenue Contribution %
------------------------------------------------------------

SELECT

Fuel_Type,

ROUND(

SUM(Total_Amount)
*100.0/

(

SELECT SUM(Total_Amount)

FROM Transactions

)

,2)

Contribution

FROM Transactions

GROUP BY Fuel_Type;


------------------------------------------------------------
-- 10 Customer Segmentation
------------------------------------------------------------

SELECT

Customer_ID,

SUM(Total_Amount) Spending,

CASE

WHEN SUM(Total_Amount)>=150000
THEN 'Premium'

WHEN SUM(Total_Amount)>=70000
THEN 'Gold'

WHEN SUM(Total_Amount)>=30000
THEN 'Silver'

ELSE 'Regular'

END Customer_Category

FROM Transactions

GROUP BY Customer_ID;


------------------------------------------------------------
-- 11 Revenue by Vehicle Type
------------------------------------------------------------

SELECT

v.Vehicle_Type,

ROUND(SUM(t.Total_Amount),2)

FROM Transactions t

JOIN Vehicles v

ON t.Vehicle_ID=v.Vehicle_ID

GROUP BY v.Vehicle_Type;


------------------------------------------------------------
-- 12 Best Fuel Type
------------------------------------------------------------

SELECT

Fuel_Type,

COUNT(*) Sales,

SUM(Total_Amount) Revenue

FROM Transactions

GROUP BY Fuel_Type

ORDER BY Revenue DESC;


------------------------------------------------------------
-- 13 Peak Hour
------------------------------------------------------------

SELECT

strftime('%H',Transaction_Time) Hour,

COUNT(*) Sales

FROM Transactions

GROUP BY Hour

ORDER BY Sales DESC;


------------------------------------------------------------
-- 14 Top Cities
------------------------------------------------------------

SELECT

s.City,

SUM(t.Total_Amount) Revenue

FROM Transactions t

JOIN Stations s

ON t.Station_ID=s.Station_ID

GROUP BY s.City

ORDER BY Revenue DESC;


------------------------------------------------------------
-- 15 Failed Transactions %
------------------------------------------------------------

SELECT

ROUND(

100.0*

SUM(

CASE

WHEN Transaction_Status='Failed'

THEN 1

ELSE 0

END

)

/

COUNT(*)

,2)

Failure_Percentage

FROM Transactions;