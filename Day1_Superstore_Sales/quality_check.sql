SELECT DISTINCT region FROM superstore_sales;

SELECT DISTINCT  category FROM superstore_sales;

SELECT DISTINCT country FROM superstore_sales;

SELECT 
    SUM(CASE WHEN sales IS NULL THEN 1 ELSE 0 END) AS null_sales,
    SUM(CASE WHEN profit IS NULL THEN 1 ELSE 0 END) AS null_profit,
    SUM(CASE WHEN category IS NULL THEN 1 ELSE 0 END) AS null_category,
    SUM(CASE WHEN region IS NULL THEN 1 ELSE 0 END) AS null_region
FROM superstore_sales;

/*  
Count how many NULL (empty) values exist in each of these 4 columns
Look at every row in the sales column. If the value IS NULL (empty) — count it as 1. If it has a value — count it as 0. 
Then add all those 1s and 0s together

*/