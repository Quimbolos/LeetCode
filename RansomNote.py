'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

https://leetcode.com/problems/ransom-note/
'''

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        for i in ransomNote:
            
            if i not in magazine:
                return (False)
            
            
            if i in magazine:
                location  = magazine.index(i)
                magazine = magazine[:location] + magazine[location + 1:]
            
        return (True)
            
