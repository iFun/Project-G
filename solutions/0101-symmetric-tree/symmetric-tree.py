# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#
#
#  
#
# But the following [1,2,2,null,3,null,3] is not:
#
#
#     1
#    / \
#   2   2
#    \   \
#    3    3
#
#
#  
#
# Note:
# Bonus points if you could solve it both recursively and iteratively.
#


#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#
# https://leetcode.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (43.92%)
# Likes:    2439
# Dislikes: 51
# Total Accepted:    433.1K
# Total Submissions: 985.8K
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric
# around its center).
# 
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
# 
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
# 
# 
# 
# 
# But the following [1,2,2,null,3,null,3] is not:
# 
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
# 
# 
# 
# 
# Note:
# Bonus points if you could solve it both recursively and iteratively.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isSym(left,right):
            if not left and not right:
                return True
            
            if left and right and left.val == right.val:
                return isSym(left.right, right.left) and isSym(left.left, right.right)
            return False
        
        return isSym(root,root)

