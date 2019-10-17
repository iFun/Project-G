# Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.
#
# Basically, the deletion can be divided into two stages:
#
# Search for a node to remove.
# If the node is found, delete the node.
#
#
#
# Note: Time complexity should be O(height of tree).
#
# Example:
#
# root = [5,3,6,2,4,null,7]
# key = 3
#
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
#
# Given key to delete is 3. So we find the node with value 3 and delete it.
#
# One valid answer is [5,4,6,2,null,null,7], shown in the following BST.
#
#     5
#    / \
#   4   6
#  /     \
# 2       7
#
# Another valid answer is [5,2,6,null,4,null,7].
#
#     5
#    / \
#   2   6
#    \   \
#     4   7
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMinChildOnRightTree(self, cur):
        while cur and cur.left:
            cur = cur.left
        
        return cur

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        if key > root.val:
            #we set root.right because root.right could change
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        # found the node need to be deleted    
        else:
            # case 1 where no children
            if not root.left and not root.right:
                root = None
            # case 2 where there is one child
            elif not root.left and root.right:
                root = root.right
            elif not root.right and root.left:
                root = root.left
            # case 3 where there are two children
            # we place the min node to the current root
            # and we find find the min node delete it (case1 or 2)
            else:
                
                temp = self.findMinChildOnRightTree(root.right)
                root.val = temp.val
                root.right = self.deleteNode(root.right, temp.val)
               
        

        return root

                
