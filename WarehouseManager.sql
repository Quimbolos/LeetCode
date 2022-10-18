'''
Write an SQL query to report the number of cubic feet of volume the inventory occupies in each warehouse.

Return the result table in any order.

https://leetcode.com/problems/warehouse-manager/
'''

SELECT Warehouse.name as warehouse_name, 
SUM(Warehouse.units*Products.Width*Products.Length*Products.Height) as volume
FROM Warehouse
LEFT JOIN Products 
ON Warehouse.product_id = Products.product_id
GROUP BY Warehouse.name
