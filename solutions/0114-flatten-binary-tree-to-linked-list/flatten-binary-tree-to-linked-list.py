# Given a binary tree, flatten it to a linked list in-place.
#
# For example, given the following tree:
#
#
#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
#
#
# The flattened tree should look like:
#
#
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, root):
        if not root:
            return None
        
        leftLastNode = self.dfs(root.left)
        rightLastNode = self.dfs(root.right)

        if leftLastNode:
            #右半边的list接到左边的最后一个的右边(因为linkedlist靠右)
            leftLastNode.right = root.right
            #左边的list挪到右边
            root.right = root.left
            #扔掉左边
            root.left = None
        
        #需要返回右边最后一个node用于连接后面的node
        if rightLastNode:
            return rightLastNode
        if leftLastNode:
            return leftLastNode
        return root

        

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.dfs(root)
        return None
        
