# Given a collection of distinct integers, return all possible permutations.
#
# Example:
#
#
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
#
#


#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (56.09%)
# Likes:    2180
# Dislikes: 64
# Total Accepted:    401.4K
# Total Submissions: 715.4K
# Testcase Example:  '[1,2,3]'
#
# Given a collection of distinct integers, return all possible permutations.
# 
# Example:
# 
# 
# Input: [1,2,3]
# Output:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
# 
#
class Solution:
    def back_tack(self, nums, current, final):
        if len(nums) is len(current):
            final.append(current.copy())

        for num in nums:
            # num is already in the list skip the num
            if num in current:
                continue
            current.append(num)
            self.back_tack(nums, current.copy(), final)
            current.pop()



    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        self.back_tack(nums,[],result)
        return result


