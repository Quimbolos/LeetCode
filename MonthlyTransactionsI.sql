'''
Write an SQL query to find for each month and country, the number of transactions and their total amount, the number of approved transactions and their total amount.

Return the result table in any order.

https://leetcode.com/problems/monthly-transactions-i/
'''

SELECT DATE_FORMAT(trans_date, '%Y-%m') AS month,
country,
COUNT(id) as trans_count, 
COUNT(IF(state = 'approved', 1, NULL)) as approved_count, 
SUM(amount) as trans_total_amount,
SUM(IF(state='approved', amount, 0)) as approved_total_amount
FROM Transactions
GROUP BY country, MONTH(trans_date);
