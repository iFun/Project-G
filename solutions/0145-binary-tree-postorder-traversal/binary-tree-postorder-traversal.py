# Given a binary tree, return the postorder traversal of its nodes' values.
#
# Example:
#
#
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# Output: [3,2,1]
#
#
# Follow up: Recursive solution is trivial, could you do it iteratively?
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def postorder(self, root, result):
        if root is None:
            return

        self.postorder(root.left, result)
        self.postorder(root.right, result)
        result.append(root.val)
        return

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        result = []

        self.postorder(root, result)

        return result
