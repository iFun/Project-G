# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
#
# Example 1:
#
#
# Input: [3,0,1]
# Output: 2
#
#
# Example 2:
#
#
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
#
#
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?


#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#
# https://leetcode.com/problems/missing-number/description/
#
# algorithms
# Easy (49.16%)
# Likes:    1078
# Dislikes: 1469
# Total Accepted:    312.4K
# Total Submissions: 635.5K
# Testcase Example:  '[3,0,1]'
#
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find
# the one that is missing from the array.
#
# Example 1:
#
#
# Input: [3,0,1]
# Output: 2
#
#
# Example 2:
#
#
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
#
#
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement
# it using only constant extra space complexity?
#


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = (1 + len(nums)) * len(nums) / 2

        for num in nums:
            total = total - num

        return int(total)

