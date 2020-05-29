/*Below are two table schemas for a popular music streaming application:

Table 1: user_song_log

Column Name	Data Type	Description
user_id	    id	        id of the streaming user
timestamp	integer	    timestamp of when the user started listening to the song, epoch seconds
song_id	    integer	    id of the song
artist_id	integer	    id of the artist

Table 2: song_info

Column Name	Data Type	Description
song_id	    integer	    id of the song
artist_id	integer	    id of the artist
song_length	integer	    length of song in seconds

Question: Given the above, can you write a SQL query to estimate the average number of hours a user spends listening to music daily? You can assume that once a given user starts a song, they listen to it in its entirety.
*/

with t as (user_id, day, total_length) as
(select
    user_id,
    day,
    sum(song_length) / 3600 as total_length
from
    (select 
        usl.user_id, 
        usl.extract(date) from timestamp as day, 
        usl.song_id,
        si.song_length
    from
        user_song_log usl
    join
        song_info si
    using
        song_id)
group by
    user_id, day)

select
    avg(total_length)
from
    t

