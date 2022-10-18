'''
Write an SQL query to report the number of calls and the total call duration between each pair of distinct persons (person1, person2) where person1 < person2.

Return the result table in any order.

https://leetcode.com/problems/number-of-calls-between-two-persons/
'''

SELECT LEAST(from_id,to_id) as person1,
GREATEST(from_id,to_id) as person2,
COUNT(*) as call_count,
SUM(duration) as total_duration
FROM Calls
GROUP BY person1,person2;

