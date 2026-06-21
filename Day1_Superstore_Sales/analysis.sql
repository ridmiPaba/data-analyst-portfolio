-- Query 1: Total Sales and Profit by Category

SELECT
 category,
 ROUND(SUM(sales)) AS total_sales,
 ROUND(SUM(profit)) AS total_profit
FROM superstore_sales
GROUP BY category
ORDER BY total_profit DESC



-- Query 2: Total Sales and Profit by Region

SELECT
region,
ROUND(SUM(sales)) AS total_sales,
ROUND(SUM(profit)) AS total_profit
FROM superstore_sales
GROUP BY region
ORDER BY total_profit DESC

-- Query 3: Top 10 Loss Making Products

SELECT
    product_name,
    ROUND(SUM(profit),2) AS total_profit
FROM superstore_sales
GROUP BY product_name
HAVING SUM(profit) < 0
ORDER BY total_profit ASC
LIMIT 10

-- Query 4: All Loss Making Products
SELECT
    product_name,
    ROUND(SUM(profit),2) AS total_profit
FROM superstore_sales
GROUP BY product_name
HAVING SUM(profit) < 0
ORDER BY total_profit ASC

-- Query 5: Bottom 10 Loss Making Products

SELECT
    product_name,
    ROUND(SUM(profit),2) AS total_profit
FROM superstore_sales
GROUP BY product_name
HAVING SUM(profit) < 0
ORDER BY total_profit DESC
LIMIT 10