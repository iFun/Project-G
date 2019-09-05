#
# Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.
#
#
#
# We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).
#
#
# Example 1:
#
# Input: [4,2,3]
# Output: True
# Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
#
#
#
# Example 2:
#
# Input: [4,2,1]
# Output: False
# Explanation: You can't get a non-decreasing array by modify at most one element.
#
#
#
# Note:
# The n belongs to [1, 10,000].
#


#
# @lc app=leetcode id=665 lang=python3
#
# [665] Non-decreasing Array
#
# https://leetcode.com/problems/non-decreasing-array/description/
#
# algorithms
# Easy (19.49%)
# Likes:    1201
# Dislikes: 271
# Total Accepted:    61.7K
# Total Submissions: 316.7K
# Testcase Example:  '[4,2,3]'
#
#
# Given an array with n integers, your task is to check if it could become
# non-decreasing by modifying at most 1 element.
#
#
#
# We define an array is non-decreasing if array[i]  holds for every i (1
#
# Example 1:
#
# Input: [4,2,3]
# Output: True
# Explanation: You could modify the first 4 to 1 to get a non-decreasing
# array.
#
#
#
# Example 2:
#
# Input: [4,2,1]
# Output: False
# Explanation: You can't get a non-decreasing array by modify at most one
# element.
#
#
#
# Note:
# The n belongs to [1, 10,000].
#
#


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:

        p = None
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i+1]:
                if p is not None:
                    return False
                else:
                    p = i
        # True if p is at position where it cannot cause
        # the list to be false(at begining or at the very end)
        # if not check the value before p and after p to see if its good or not
        return p == 0 or p is None or p == len(nums) - 2 or nums[p-1] <= nums[p+1] or nums[p] <= nums[p+2]

