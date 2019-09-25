# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
#
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
#
# Find the total sum of all root-to-leaf numbers.
#
# Note: A leaf is a node with no children.
#
# Example:
#
#
# Input: [1,2,3]
#     1
#    / \
#   2   3
# Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.
#
# Example 2:
#
#
# Input: [4,9,0,5,1]
#     4
#    / \
#   9   0
#  / \
# 5   1
# Output: 1026
# Explanation:
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->9->1 represents the number 491.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.
#


#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#
# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
#
# algorithms
# Medium (43.81%)
# Likes:    805
# Dislikes: 29
# Total Accepted:    202.2K
# Total Submissions: 461.4K
# Testcase Example:  '[1,2,3]'
#
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path
# could represent a number.
#
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
#
# Find the total sum of all root-to-leaf numbers.
#
# Note: A leaf is a node with no children.
#
# Example:
#
#
# Input: [1,2,3]
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.
#
# Example 2:
#
#
# Input: [4,9,0,5,1]
# ⁠   4
# ⁠  / \
# ⁠ 9   0
# / \
# 5   1
# Output: 1026
# Explanation:
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->9->1 represents the number 491.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def dfs(self, root: TreeNode, tmp: str, result):
        if not root:
            return

        if not root.left and not root.right:
            tmp += str(root.val)
            result.append(int(tmp))
            return

        tmp += str(root.val)
        self.dfs(root.left, tmp, result)
        self.dfs(root.right, tmp, result)
        return

    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0

        result = []

        self.dfs(root, '', result)

        return sum(result)

