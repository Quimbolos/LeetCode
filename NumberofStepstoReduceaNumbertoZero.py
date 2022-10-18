'''
Given an integer num, return the number of steps to reduce it to zero.

In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
'''

class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        
        while num > 0:
            
            if num % 2 == 0:
                num = num/2
                
            else:
                num = num-1
            
            count = count +1
            
        return(count)

