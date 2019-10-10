# You need to find the largest value in each row of a binary tree.
#
# Example:
#
# Input: 
#
#           1
#          / \
#         3   2
#        / \   \  
#       5   3   9 
#
# Output: [1, 3, 9]
#
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = deque()
        result = []
        queue.append(root)

        while queue:
            level_size = len(queue)
            tmp = -999999999999
            for _ in range(0, level_size):
                current = queue.popleft()
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
                tmp = max(tmp, current.val)

            result.append(tmp)

        return result


