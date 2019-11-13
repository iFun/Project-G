# Given a binary tree
#
#
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
#
#
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.
#
#  
#
# Example:
#
#
#
#
# Input: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":null,"next":null,"right":{"$id":"6","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}
#
# Output: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,"next":{"$id":"5","left":null,"next":null,"right":null,"val":7},"right":null,"val":5},"right":null,"val":4},"next":{"$id":"6","left":null,"next":null,"right":{"$ref":"5"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"6"},"val":1}
#
# Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B.
#
#
#  
#
# Note:
#
#
# 	You may only use constant extra space.
# 	Recursive approach is fine, implicit stack space does not count as extra space for this problem.
#


"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        queue = deque()

        queue.append(root)

        while queue:
            level = len(queue)
            prev = None
            for i in range(0, level):
                current = queue.popleft()
                if prev:
                    prev.next = current
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
                prev = current

            current.next = None

        return root
