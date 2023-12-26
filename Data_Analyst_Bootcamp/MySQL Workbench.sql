SELECT * FROM pizza_sales.pizza_sales;

 -- Total Reveune a KPI
SELECT SUM(total_price) AS Total_Revenue FROM pizza_sales.pizza_sales;

-- Average Order Value
SELECT (SUM(total_price) / COUNT (DISTINCT order_id)) AS Avg_Order_Value
FROM pizza_sales; 