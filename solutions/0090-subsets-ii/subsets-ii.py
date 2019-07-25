# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
#
# Input: [1,2,2]
# Output:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]
#
#


#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#
# https://leetcode.com/problems/subsets-ii/description/
#
# algorithms
# Medium (42.92%)
# Likes:    941
# Dislikes: 49
# Total Accepted:    210.7K
# Total Submissions: 491K
# Testcase Example:  '[1,2,2]'
#
# Given a collection of integers that might contain duplicates, nums, return
# all possible subsets (the power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# Example:
# 
# 
# Input: [1,2,2]
# Output:
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
# 
# 
#
class Solution:
    # bascailly for each new number there is two choices
    # add number or skip number
    # keep doing this choice until the index number is reached to
    # the end of the list and append that list to the final list
    def backtrack(self, start, nums, tmp_list, final_list):
        final_list.append(tmp_list.copy())
        for index in range(start, len(nums)):
            #skip dup
            if index > start and nums[index] == nums[index - 1]:
                continue
            tmp_list.append(nums[index])
            self.backtrack(index + 1, nums, tmp_list, final_list)
            tmp_list.pop()
    

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        cur = []
        nums.sort()
        self.backtrack(0, nums, cur, result)
        return result


