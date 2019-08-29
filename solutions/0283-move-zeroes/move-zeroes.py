# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Example:
#
#
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
#
# Note:
#
#
# 	You must do this in-place without making a copy of the array.
# 	Minimize the total number of operations.
#


#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
# https://leetcode.com/problems/move-zeroes/description/
#
# algorithms
# Easy (54.63%)
# Likes:    2133
# Dislikes: 79
# Total Accepted:    486.4K
# Total Submissions: 890.4K
# Testcase Example:  '[0,1,0,3,12]'
#
# Given an array nums, write a function to move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.
#
# Example:
#
#
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
#
# Note:
#
#
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
#
#


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return None
        fast = 0
        slow = 0

        while (fast < len(nums)):

            # move number that is not zero to the front
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        while (slow < len(nums)):
            nums[slow] = 0
            slow += 1

