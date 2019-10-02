# Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#
# For example, given a 3-ary tree:
#
#  
#
#
#
#  
#
# We should return its level order traversal:
#
#
# [
#      [1],
#      [3,2,4],
#      [5,6]
# ]
#
#
#  
#
# Note:
#
#
# 	The depth of the tree is at most 1000.
# 	The total number of nodes is at most 5000.
#
#


"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        queue = deque()
        queue.append(root)
        result = []
        
        
        while queue:
            sublist = []
            level = len(queue)
            
            for i in range(0,level):
                current = queue.popleft()
                sublist.append(current.val)
                for child in current.children:
                    queue.append(child)
                    
            result.append(sublist.copy())
        
        return result
        

