'''
We define query quality as:

The average of the ratio between query rating and its position.

We also define poor query percentage as:

The percentage of all queries with rating less than 3.

Write an SQL query to find each query_name, the quality and poor_query_percentage.

Both quality and poor_query_percentage should be rounded to 2 decimal places.

Return the result table in any order.

https://leetcode.com/problems/queries-quality-and-percentage/
'''

SELECT
    query_name,
    ROUND(AVG(rating/position), 2) AS quality,
    ROUND(AVG(rating < 3)*100, 2) AS poor_query_percentage
FROM Queries
GROUP BY query_name
