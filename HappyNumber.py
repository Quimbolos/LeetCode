'''
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

https://leetcode.com/problems/happy-number/
'''

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        l = []
        while(True):
            l.append(n)
            n=str(n)
            a=0
            for i in n:
                a=int(i)**2+a
            if(a==1):
                return True
            if(a in l):
                return False
            n=a
