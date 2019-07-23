# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
#
# Example:
#
#
# Input: [1,1,2]
# Output:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]
#
#


#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#
# https://leetcode.com/problems/permutations-ii/description/
#
# algorithms
# Medium (41.19%)
# Likes:    1078
# Dislikes: 45
# Total Accepted:    255.1K
# Total Submissions: 619K
# Testcase Example:  '[1,1,2]'
#
# Given a collection of numbers that might contain duplicates, return all
# possible unique permutations.
# 
# Example:
# 
# 
# Input: [1,1,2]
# Output:
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
# 
# 
#
class Solution:
    def back_track(self,nums,used,current,final):
        if len(current) is len(nums):
            final.append(current.copy())
            return

        for index in range(0,len(nums)):
            # avoid duplicate
            if used[index] or (index > 0 and nums[index] is nums[index - 1 ] and not used[index - 1]):
                continue
            used[index] = True
            current.append(nums[index])
            self.back_track(nums,used.copy(),current.copy(),final)
            used[index] = False
            current.pop()
        


    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        used = [False] * len(nums)
        result = []
        nums.sort()
        self.back_track(nums,used,[],result)
        return result


