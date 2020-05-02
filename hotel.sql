/*Suppose you're an analyst for a major US hotel chain which has locations all over the US. Your marketing team is planning a promotion focused around loyal customers, and they are trying to forecast how much revenue the promotion will bring in. However, they need help from you to understand how much revenue comes from "loyal" customers to plug into their model. 

A "loyal" customer is defined as (1) having a membership with your company's point system, (2) having >2 stays at each hotel the customer visited, (3) having stayed at 3 different locations throughout the US.

You have a table showing all transactions made in 2017. The schema of the table is below:

Table: customer_transactions

Column Name	Data Type	Description
customer_id	id	id of the customer
hotel_id	integer	unique id for hotel
transaction_id	integer	id of the given transaction
first_night	string	first night of the stay, column format is "YYYY-mm-dd"
number_of_nights	integer	# of nights the customer stayed in hotel
total_spend	integer	total spend for transaction, in USD
is_member	boolean	indicates if the customer is a member of our points system

Given this, can you write a SQL query that calculates percent of revenue loyal customers brought in 2017? */

-- get total from all
-- filter to loyal
-- get total from loyal 

select sum(total_spend) as total 
select sum(total_spend) as loyal_spend
from customer_transactions
where is_member is True

with stays (customer_id, hotel_id, num_stays) as -- condition 2
(
    select customer_id, hotel_id, count(transaction_id) as num_stays
    from customer_transactions
    group by customer_id, hotel_id
    having num_stays > 2
),
locations (customer_id, num_locations) as -- condition 3
(
    select customer_id, count(distinct(hotel_id)) as num_locations
    from customer_transactions
    group by customer_id
)

select sum(ct.total_spend) as loyal_spend
from customer_transactions as ct
inner join stays on ct.customer_id = stays.customer_id
inner join locations on ct.customer_id = locations.customer_id
where ct.is_member is True

select sum(total_spend) as total 

