'''
Write an SQL query to find the percentage of the users registered in each contest rounded to two decimals.

Return the result table ordered by percentage in descending order. In case of a tie, order it by contest_id in ascending order.

https://leetcode.com/problems/percentage-of-users-attended-a-contest/
'''

SELECT contest_id, 
    ROUND(COUNT(contest_id)*100/(SELECT COUNT(*) FROM Users),2) as percentage
FROM Register 
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC

