# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given the below binary tree and sum = 22,
#
#
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \    / \
# 7    2  5   1
#
#
# Return:
#
#
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
#
#


#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#
# https://leetcode.com/problems/path-sum-ii/description/
#
# algorithms
# Medium (42.27%)
# Likes:    1074
# Dislikes: 39
# Total Accepted:    257.7K
# Total Submissions: 609.6K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
#
# Given a binary tree and a sum, find all root-to-leaf paths where each path's
# sum equals the given sum.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given the below binary tree and sum = 22,
#
#
# ⁠     5
# ⁠    / \
# ⁠   4   8
# ⁠  /   / \
# ⁠ 11  13  4
# ⁠/  \    / \
# 7    2  5   1
#
#
# Return:
#
#
# [
# ⁠  [5,4,11,2],
# ⁠  [5,8,4,5]
# ]
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

    def dfs(self, root: TreeNode, target: int, tmp: List[int], result):
        if not root:
            return

        if not root.left and not root.right and root.val == target:
            tmp.append(root.val)
            result.append(tmp.copy())
            return

        target -= root.val
        tmp.append(root.val)
        self.dfs(root.left, target, tmp.copy(), result)
        self.dfs(root.right, target, tmp.copy(), result)
        return

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []

        result = []
        self.dfs(root, sum, [], result)

        return result

