/*
This problem was asked by Snapchat.

Assume you have the below tables on sessions that users have, and a users table. Write a query to get the active user count of daily cohorts, i.e. the counts of users registered each day.

sessions

column_name	type
session_id	integer
user_id	integer
date	datetime


users

column_name	type
user_id	integer
email	string
date	datetime
*/

select datetime, count(user_id) as user_count
from users
group by datetime

