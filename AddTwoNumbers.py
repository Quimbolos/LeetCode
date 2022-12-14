'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

https://leetcode.com/problems/add-two-numbers/
'''

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        current_node = l1
        current_node2 = l2
        
        vals1 = []
        vals2 = []
        
        num1 = ''
        num2 = ''
        
        while current_node != None:
            vals1.append(current_node.val)
            current_node = current_node.next
            
        while current_node2 != None:
            vals2.append(current_node2.val)
            current_node2 = current_node2.next
            
        for i in range(len(vals1)):
            vals1[i] = str(vals1[i])
            
        for i in range(len(vals2)):
            vals2[i] = str(vals2[i])
            
        for i in range(1,len(vals1)+1):
            num1 = num1 + vals1[-1*i]
            
        for i in range(1,len(vals2)+1):
            num2 = num2 + vals2[-1*i]
            
        ans_ = str(int(num1) + int(num2))

        ans = []

        for i in range(1,len(ans_)+1):
            ans.append(int(ans_[-1*i]))
        
        # Random code to convert a List into a Linked list
        
        cur = dummy = ListNode(0)
        for e in ans:
            cur.next = ListNode(e)
            cur = cur.next
            
        return (dummy.next)
                          
