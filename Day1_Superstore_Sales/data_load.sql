USE superstore;

LOAD DATA LOCAL INFILE '/Users/prabhavihemachandra/Desktop/Day1_Project/Superstore_clean.csv'
INTO TABLE superstore_sales 
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(row_id, order_id, @order_date, @ship_date, ship_mode, customer_id, customer_name, 
segment, country, city, state, postal_code, region, product_id, category, 
subcategory, product_name, sales, quantity, discount, profit)
SET 
order_date = STR_TO_DATE(@order_date, '%m/%d/%Y'),
ship_date = STR_TO_DATE(@ship_date, '%m/%d/%Y');

