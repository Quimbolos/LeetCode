'''
If the customer's preferred delivery date is the same as the order date, then the order is called immediate; otherwise, it is called scheduled.

Write an SQL query to find the percentage of immediate orders in the table, rounded to 2 decimal places.

https://leetcode.com/problems/immediate-food-delivery-i/
'''

SELECT
    ROUND((COUNT(*)*100/(SELECT COUNT(*) FROM Delivery)),2) as immediate_percentage
FROM Delivery
WHERE order_date = customer_pref_delivery_date
