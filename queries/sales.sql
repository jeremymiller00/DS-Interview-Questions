/*
You are given the following dataset of daily sales from a company's sales team. You can assume the table is called DailySales. Given this, write a SQL query to return the top sales person on each given day.

Column Name	    Column Type	    Short description
Date	        string  	    Date of sales summary
Name	        string	        Name of sales person.
Num_Sales	    int	            Total number of sales

*/

select
Date, Name

from
    ( select Date, Name, 
        dense_rank() over
            ( partition by Date order by Num_Sales desc) as ranking )
    
where ranking = 1;