# Given a set of distinct integers, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
#
# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
#


#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (53.70%)
# Likes:    2082
# Dislikes: 53
# Total Accepted:    384.4K
# Total Submissions: 715.8K
# Testcase Example:  '[1,2,3]'
#
# Given a set of distinct integers, nums, return all possible subsets (the
# power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# Example:
# 
# 
# Input: nums = [1,2,3]
# Output:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
# 
#
class Solution:

    # bascailly for each new number there is two choices
    # add number or skip number
    # keep doing this choice until the index number is reached to 
    # the end of the list and append that list to the final list
    def backtrack(self, index, nums, tmp_list, final_list):
        if index is len(nums):
            final_list.append(tmp_list.copy())
            return
        
        # skip the current number
        self.backtrack(index + 1, nums, tmp_list.copy(), final_list)
        
        # add the current number
        tmp_list.append(nums[index])
        self.backtrack(index + 1, nums, tmp_list.copy(), final_list)
   

            


    def subsets(self, nums: List[int]) -> List[List[int]]:
        if nums is None or len(nums) is 1:
            return [[],nums]
        result = []
        self.backtrack(0, nums, [], result)
        return result


