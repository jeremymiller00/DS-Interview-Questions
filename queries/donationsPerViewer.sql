/*
Twitch content creators
SQL Database Querying

You are working for a company like Twitch.tv. Twitch.tv is a live streaming platform, where content creators (e.g. the people creating content on the live streams) can get donations from viewers for producing content they support.

Your company is trying to launch a new product that will benefit content creators that get a large amount of donations per streaming session. You are given the following tables:

Table: all_donations

Column Name	Data Type	Description
creator_id	integer	unique id of content creator
viewer_id	integer	unique id of viewer
session_id	integer	unique session id of stream
date	string	format is "YYYY-MM-DD"
donation_amount	integer	amount donated in USD

Table: sessions_info

Column Name	Data Type	Description
creator_id	integer	unique id of content creator
session_id	integer	unique id of viewer
date	string	format is "YYYY-MM-DD", date of session
length	integer	length of session

Table: session_viewers

Column Name	Data Type	Description
creator_id	integer	unique id of content creator
viewer_id	integer	unique id of viewer
date	string	format is "YYYY-MM-DD"
session_id	integer	unique session id of stream
mins_viewed	integer	total number of the viewer watched the stream

Given this, write a SQL query to find the top 10 content creators in 2018 that have the highest average donations per viewer.
*/
with tmp (creator_id, viewer_id, sum_donations) as (
  select creator_id, viewer_id, sum(donation_amount)
  from all_donations
  group by creator_id, viewer_id
)

select creator_id,
  avg(sum_donations) over (partition by creator_id) as avg_don_per_viewer
from tmp
order by avg_don_per_viewer desc
limit 10