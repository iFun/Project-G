# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
#
#
#
# Example:
#
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = []
        num2 = []
        
        while l1:
            num1.append(l1.val)
            l1 = l1.next
        while l2:
            num2.append(l2.val)
            l2 = l2.next
        ll = ListNode(0)
        
        value = 0
        while len(num1) > 0 or len(num2) > 0:

            if len(num1) > 0:
                value += num1.pop()
            if len(num2) > 0:
                value += num2.pop()
            ll.val = value % 10
            head = ListNode(value // 10)
            head.next = ll
            ll = head
            value //= 10
        
        if ll.val is 0:
            return ll.next
        else:
            return ll
