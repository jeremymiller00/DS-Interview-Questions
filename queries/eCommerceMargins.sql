/*
Suppose you're an analyst for an e-commerce store. You’re trying to identify the top selling items (by revenue) that have the highest margins. Using the tables below, can you write a SQL query that pulls the distributor, product_id, total revenue, total cost, total net margin, and number of units sold. Then, can you create additional columns that rank total net margin, total revenue, and total cost from greatest to least?


Table: allProducts

Column Name	Data Type	Description
product_id	integer	id of the product
product_name	string	name of the product
sku	integer	universal stockkeeping unit number
distributor_id	integer	unique id for distributor
Table: orders

Column Name	Data Type	Description
date	string	format is "YYYY-MM-DD"
user_id	integer	user id of purchaser
order_id	integer	unique order number
product_id	integer	id of product
no_units	integer	number of units sold in the order
sell_price	integer	the price the item is sold at
buy_price	integer	the price to procure the item
shipping_id	integer	id of shipping information
region	string	region of shipping id

*/

select
  p.distributor_id
  ,o.product_id
  ,sum((o.sell_price - o.buy_price) * o.no_units) as total_net_margin
  ,sum(o.sell_price * o.no_units) as total_revenue
  ,sum(o.buy_price * o.no_units) as total_cost
  ,sum(o.no_units) as units_sold
  ,RANK() over (order by total_net_margin) as margin_rank
  ,RANK() over (order by total_revenue) as revenue_rank
  ,RANK() over (order by total_cost) as cost_rank
  
from
  allProducts p
join
  orders o
on
  p.product_id = o.product_id
group by
  p.distributor_id, o.product_id