'''
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

https://leetcode.com/problems/running-sum-of-1d-array/https://leetcode.com/problems/running-sum-of-1d-array/
'''

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        list = []
        
        for i in range(0,len(nums)):
            
            if len(list)>0:
                list.append(list[i-1]+nums[i])
                
            else:
                list.append(nums[i])
        
        return(list)
