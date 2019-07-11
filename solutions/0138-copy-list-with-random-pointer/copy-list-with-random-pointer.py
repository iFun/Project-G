# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
#
# Return a deep copy of the list.
#
#  
#
# Example 1:
#
#
#
#
# Input:
# {"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}
#
# Explanation:
# Node 1's value is 1, both of its next and random pointer points to Node 2.
# Node 2's value is 2, its next pointer points to null and its random pointer points to itself.
#
#
#  
#
# Note:
#
#
# 	You must return the copy of the given head as a reference to the cloned list.
#
#


#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#
# https://leetcode.com/problems/copy-list-with-random-pointer/description/
#
# algorithms
# Medium (27.38%)
# Likes:    1586
# Dislikes: 425
# Total Accepted:    251.2K
# Total Submissions: 917.2K
# Testcase Example:  '{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}'
#
# A linked list is given such that each node contains an additional random
# pointer which could point to any node in the list or null.
# 
# Return a deep copy of the list.
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input:
# 
# {"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}
# 
# Explanation:
# Node 1's value is 1, both of its next and random pointer points to Node 2.
# Node 2's value is 2, its next pointer points to null and its random pointer
# points to itself.
# 
# 
# 
# 
# Note:
# 
# 
# You must return the copy of the given head as a reference to the cloned
# list.
# 
# 
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # edge case
        if head is None:
            return head


        #duplciate every node in the list
        current = head
        
        while current is not None:
            nextNode = current.next
            current.next = Node(current.val, None, None)
            current.next.next = nextNode
            current = nextNode


        #link every random node in the list for the copy node
        current = head
        while current is not None:
            if current.random is not None:
                # current.next is the copied node
                # current.random.next is the copied "random" node 
                current.next.random = current.random.next
            current = current.next.next

        #split the copied node from the original linklist
        current = head
        fakeHead = Node(0, None, None)
        copy = fakeHead
        copyIter = fakeHead
        
        while current is not None:
            nextNode = current.next.next
            copy = current.next
            copyIter.next = copy
            copyIter = copy

            current.next = nextNode
            current = nextNode

        return fakeHead.next

