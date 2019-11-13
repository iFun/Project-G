# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
#
#


#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (44.25%)
# Likes:    11020
# Dislikes: 372
# Total Accepted:    1.9M
# Total Submissions: 4.2M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
# 
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
# 
# Example:
# 
# 
# Given nums = [2, 7, 11, 15], target = 9,
# 
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
# 
# 
#
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) < 2:
            return nums

        hashtable = {}
        count = 0
        for number in nums:
            if target - number not in hashtable:
                hashtable[number] = count
            else:
                return [hashtable[target - number] , count]
            count += 1
        return []

