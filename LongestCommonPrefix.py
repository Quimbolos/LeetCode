'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

https://leetcode.com/problems/longest-common-prefix/
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans = ""
        
        for i in range(len(strs[0])):
            for s in strs:
                
                if i == len(s) or s[i] != strs[0][i]:
                    return ans
           
            ans += strs[0][i]
            
        return ans
