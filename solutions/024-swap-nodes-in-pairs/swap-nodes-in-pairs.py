# Given a linked list, swap every two adjacent nodes and return its head.
#
# You may not modify the values in the list's nodes, only nodes itself may be changed.
#
#  
#
# Example:
#
#
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: 'ListNode') -> 'ListNode':
        if head is None or head.next is None:
            return head
        newHead = head.next
        
        prev = head
        cur = head
        nextNode = head.next
        tmpNext = nextNode.next
        cur.next = tmpNext
        nextNode.next = cur
        cur = tmpNext
        if tmpNext:
            nextNode = tmpNext.next
        

        while cur and nextNode:
            curNext = nextNode.next
            nextNode.next = cur
            cur.next = curNext
            prev.next = nextNode
            prev = cur
            cur = curNext
            if curNext:
                nextNode = curNext.next
            
        return newHead
