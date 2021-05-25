/*
Assume you are given the below tables for the session activity of users. Write a query to assign ranks to users by the total session duration for the different session types they have had between a start date (2020-01-01) and an end date (2020-02-01).

Sessions

column_name	type
session_id	integer
user_id	integer
session_type	string
duration	integer
start_time	datetime
*/


with temp (  
  user_id,
  session_type,
  total_duration
) as 
(
select
  user_id,
  session_type,
  sum(duration) as total_duration

from Sessions
where start_time > '2020-01-01' and
start_time < '2020-02-01'
group by user_id, session_type
)

select
  user_id,
  session_type
  RANK() over (partition by session_type order by total_duration desc)
from
  temp
;
