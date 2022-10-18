'''
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

https://leetcode.com/problems/richest-customer-wealth/
'''

class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        
        max_wealth = 0
        
        for i in accounts:
            wealth = sum(i)
            
            if wealth > max_wealth:
                max_wealth = wealth
            
        return(max_wealth)

