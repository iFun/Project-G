# Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.
#
# Example:
#
#
# Input:
#
#    1
#     \
#      3
#     /
#    2
#
# Output:
# 1
#
# Explanation:
# The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
#
#
#  
#
# Note: There are at least two nodes in this BST.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def findMin(self, root, result, tmp):
        if not root:
            return None
        self.findMin(root.left, result, tmp)
        if len(tmp) > 0:
            if len(tmp) > 1:
                tmp[0] = tmp[1]
                tmp[1] = root.val
            else:
                tmp.append(root.val)

            result[0] = min(tmp[1] - tmp[0], result[0])
        else:
            tmp.append(root.val)
        self.findMin(root.right, result, tmp)
        return None

    def getMinimumDifference(self, root: TreeNode) -> int:
        result = [9999999999999]

        self.findMin(root, result, [])

        return result[0]
