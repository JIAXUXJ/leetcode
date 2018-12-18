# Write your MySQL query statement below, a little bit slower than without exists 
SELECT 
    name, population, area 
from 
    World 
WHERE EXISTS(
    SELECT population, area WHERE area > 3000000 OR population > 25000000
);
