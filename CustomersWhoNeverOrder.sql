'''
Write an SQL query to report all customers who never order anything.

Return the result table in any order.

https://leetcode.com/problems/customers-who-never-order/
'''

SELECT name AS 'Customers'
FROM customers
WHERE id NOT IN (SELECT customerId FROM orders);
