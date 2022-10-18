'''
Write an SQL query to find the ids of products that are both low fat and recyclable.

Return the result table in any order.

https://leetcode.com/problems/recyclable-and-low-fat-products/
'''

SELECT product_id
FROM products
WHERE low_fats='Y' AND recyclable= 'Y';
