/*
Suppose you're provided two tables, as shown below. One table contains the price for a given product in a given region, while another contains sales for the past week. Given the two tables, write a SQL query to pull the total earnings for each product/region combination.

Table: product_pricing

region	product	price
Americas	Pepsi	$2.2
EMEA	Pepsi	$1.8
APAC	Pepsi	$1.5
Americas	Coke	$2.5
EMEA	Coke	$2.0
APAC	Coke	$1.8
Table: product_sales

region	product	num_sales
Americas	Pepsi	20
EMEA	Pepsi	25
APAC	Pepsi	22
Americas	Coke	30
EMEA	Coke	10
APAC	Coke	13
*/

select
  a.region
  ,a.product
  ,a.price * b.num_sales as revenue

from product_pricing a 
join product_sales b
on a.region = b.region
and a.product = b.product