# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
#
# 	The left subtree of a node contains only nodes with keys less than the node's key.
# 	The right subtree of a node contains only nodes with keys greater than the node's key.
# 	Both the left and right subtrees must also be binary search trees.
#
#
#  
#
# Example 1:
#
#
#     2
#    / \
#   1   3
#
# Input: [2,1,3]
# Output: true
#
#
# Example 2:
#
#
#     5
#    / \
#   1   4
#      / \
#     3   6
#
# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
#
#


#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#
# https://leetcode.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (25.95%)
# Likes:    2083
# Dislikes: 311
# Total Accepted:    428K
# Total Submissions: 1.6M
# Testcase Example:  '[2,1,3]'
#
# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
#
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.
#
#
#
#
# Example 1:
#
#
# ⁠   2
# ⁠  / \
# ⁠ 1   3
#
# Input: [2,1,3]
# Output: true
#
#
# Example 2:
#
#
# ⁠   5
# ⁠  / \
# ⁠ 1   4
# / \
# 3   6
#
# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
#
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# upper and lower bound of current node
# to check see if the current node is the correct one in the entire tree


class Solution:
    def dfs(self, node, lower, upper):
        if not node:
            return True
        val = node.val
        if val <= lower or val >= upper:
            return False
        if not self.dfs(node.right, val, upper):
            return False
        if not self.dfs(node.left, lower, val):
            return False

        return True

    def isValidBST(self, root: TreeNode) -> bool:
        return self.dfs(root, -float("inf"), float("inf"))

