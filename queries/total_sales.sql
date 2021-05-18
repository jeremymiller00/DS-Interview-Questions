/*
You are given the below tables, showing Store, Product, and Sales information for a chain of grocery stores. The columns are labeled in such a way that you should be able to interpret what each field is showing.

Store

store_id	location
91110	New York
99525	Los Angeles
37340	Tokyo
32016	Detroit
57507	London
Product

product_id	product_name	price_usd
31331	Apples	2
34611	Lettuce	3
49760	Chicken	5
26583	Lemons	1
20267	Bread	2
Sales

sale_id	product_id	store_id	date
1	31331	91110	02/20/2020
1	31331	91110	02/20/2020
2	34611	57507	02/20/2020
3	26583	37340	02/20/2020
3	34611	32016	02/20/2020
3	20267	99525	02/21/2020
4	31331	99525	02/21/2020
5	49760	99525	02/21/2020
6	34611	57507	02/21/2020
7	31331	91110	02/21/2020

Using the tables above, write a SQL query to return total sales (in dollars) by store location by product. If total sales are null for a given store location / product combination, set them to 0.

Your output should return the following columns:

store_id	product_id	total_sales
X	Y	Z
A	B	C
*/

with all_data(product_id, store_id, date, price_usd) as (
  select product_id, store_id, date
  from sales
  join (select product_id, price_usd from product)
  on product_id
)

select store_id, product_id, sum(price_usd) as total_sales
from all_data
group by store_id, product_id