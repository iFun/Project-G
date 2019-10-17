# Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.
#
# Example 1:
#
#
# Input: 
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
#
# Target = 9
#
# Output: True
#
#
#  
#
# Example 2:
#
#
# Input: 
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
#
# Target = 28
#
# Output: False
#
#
#  
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def helper(self, current, contain, k):
        if not current:
            return
        if current.val in contain:
            return True

        sub = k - current.val

        contain.add(sub)

        return self.helper(current.left, contain, k) or self.helper(current.right, contain, k)

    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False
        contain = set()

        return self.helper(root, contain, k)
