#
# Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.
#
#
# Example 1:
#
# Given tree s:
#
#      3
#     / \
#    4   5
#   / \
#  1   2
#
# Given tree t:
#
#    4 
#   / \
#  1   2
#
# Return true, because t has the same structure and node values with a subtree of s.
#
#
# Example 2:
#
# Given tree s:
#
#      3
#     / \
#    4   5
#   / \
#  1   2
#     /
#    0
#
# Given tree t:
#
#    4
#   / \
#  1   2
#
# Return false.
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# convert binary tree to string and then compare


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        string_s = self.traverse_tree(s)
        string_t = self.traverse_tree(t)
        if string_t in string_s:
            return True
        return False

    def traverse_tree(self, s):
        if s:
            return f"#{s.val} {self.traverse_tree(s.left)} {self.traverse_tree(s.right)}"
        return None
