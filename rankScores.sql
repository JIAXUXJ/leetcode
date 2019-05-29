# Write your MySQL query statement below
select 
    s1.Score,
    (select count(distinct s2.Score) from Scores as s2 where s2.Score >= s1.Score) as Rank 
from 
    Scores as s1 
order by Score desc