# Given a binary tree, return all root-to-leaf paths.
#
# Note: A leaf is a node with no children.
#
# Example:
#
#
# Input:
#
#    1
#  /   \
# 2     3
#  \
#   5
#
# Output: ["1->2->5", "1->3"]
#
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, current, tmp, result):
        if not current:
            return
        
        if not current.left and not current.right:
            tmp = tmp + str(current.val)
            result.append(tmp)
            return
        tmp += str(current.val) + '->'
        
        self.dfs(current.left,tmp, result)
        self.dfs(current.right,tmp, result)
    
    
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        if root.left is None and root.right is None:
            return str(root.val)
        
        result = []
        
        self.dfs(root, '', result)
        
        return result
