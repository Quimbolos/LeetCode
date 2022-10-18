'''
Write an SQL query to report the difference between the number of apples and oranges sold each day.

Return the result table ordered by sale_date.

https://leetcode.com/problems/apples-oranges/
'''

SELECT sale_date, 
SUM(CASE
    WHEN fruit = 'apples' THEN sold_num
    ELSE -sold_num    
END) as diff
FROM Sales
GROUP BY sale_date;
