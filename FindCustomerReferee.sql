'''
Write an SQL query to report the names of the customer that are not referred by the customer with id = 2.

Return the result table in any order.

https://leetcode.com/problems/find-customer-referee/
'''

SELECT name
FROM customer
WHERE referee_id != 2 OR referee_id IS NULL;
            
            
