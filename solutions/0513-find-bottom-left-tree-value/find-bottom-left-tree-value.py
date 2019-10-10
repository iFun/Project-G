#
# Given a binary tree, find the leftmost value in the last row of the tree. 
#
#
# Example 1:
#
# Input:
#
#     2
#    / \
#   1   3
#
# Output:
# 1
#
#
#
#   Example 2: 
#
# Input:
#
#         1
#        / \
#       2   3
#      /   / \
#     4   5   6
#        /
#       7
#
# Output:
# 7
#
#
#
# Note:
# You may assume the tree (i.e., the given root node) is not NULL.
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if root is None:
            return

        queue = deque()
        result = -1
        queue.append(root)

        while queue:
            level = len(queue)
            for i in range(level):
                current = queue.popleft()
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

                if i is 0:
                    result = current.val

        return result

