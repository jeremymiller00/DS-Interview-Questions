/*
Suppose your team interviews undergraduate candidates across many different colleges. You are looking to check which candidates scored the highest from each college.

Given the below tables, write a SQL query (using a window function) to show which candidates scored the highest from each college.


college_id	candidate_name
123456	john_smith
123456	sarah_daniels
123457	tim_cook
123457	lisa_perelli
123457	jenny_west
123457	karl_tran
123457	tammy_turner


interview_id	candidate_name	interview_score
12	john_smith	4
22	sarah_daniels	3
23	tim_cook	3
25	lisa_perelli	5
26	jenny_west	2
27	karl_tran	2
28	tammy_turner	4
*/

-- join tables together: college_id, name, score
with scores (college_id, candidate_name, interview_score) as (
  select a.college_id, a.candidate_name, b.interview_score
  from candidateColleges as a
  inner join candidateInterviews b 
  on a.candidate_name = b.candidate_name
)

select candidate_name, college_id,
rank() over (partition by college_id order by interview_score desc) as ranking
where ranking = 1