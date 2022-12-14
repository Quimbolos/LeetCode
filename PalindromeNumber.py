'''
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.

https://leetcode.com/problems/palindrome-number/
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        num = str(x)
        
        if (len(num) % 2) == 0:
            length = len(num)//2
            
        else:
            length = (len(num)-1)//2
        
        if len(num) == 1:
            return(True)
        for i in range(length):
            if num[i] == num[-i-1]:
                result = True
            elif num[i] != num[-i-1]:
                result = False
                break
                
        return result
                          
