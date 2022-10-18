'''
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

https://leetcode.com/problems/palindrome-linked-list/
'''

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        vals = []
        current_node = head
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
            
        return vals == vals[::-1]
