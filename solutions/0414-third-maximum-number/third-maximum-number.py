# Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).
#
# Example 1:
#
# Input: [3, 2, 1]
#
# Output: 1
#
# Explanation: The third maximum is 1.
#
#
#
# Example 2:
#
# Input: [1, 2]
#
# Output: 2
#
# Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
#
#
#
# Example 3:
#
# Input: [2, 2, 3, 1]
#
# Output: 1
#
# Explanation: Note that the third maximum here means the third maximum distinct number.
# Both numbers with value 2 are both considered as second maximum.
#
#


#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#
# https://leetcode.com/problems/third-maximum-number/description/
#
# algorithms
# Easy (29.38%)
# Likes:    420
# Dislikes: 781
# Total Accepted:    102.7K
# Total Submissions: 349.4K
# Testcase Example:  '[3,2,1]'
#
# Given a non-empty array of integers, return the third maximum number in this
# array. If it does not exist, return the maximum number. The time complexity
# must be in O(n).
#
# Example 1:
#
# Input: [3, 2, 1]
#
# Output: 1
#
# Explanation: The third maximum is 1.
#
#
#
# Example 2:
#
# Input: [1, 2]
#
# Output: 2
#
# Explanation: The third maximum does not exist, so the maximum (2) is returned
# instead.
#
#
#
# Example 3:
#
# Input: [2, 2, 3, 1]
#
# Output: 1
#
# Explanation: Note that the third maximum here means the third maximum
# distinct number.
# Both numbers with value 2 are both considered as second maximum.
#
#
#


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) is 1:
            return nums[0]
        if len(nums) is 2:
            return nums[0] if nums[0] > nums[1] else nums[1]

        maxNums = [-99999999999] * 3

        for num in nums:
            if num not in maxNums and num > maxNums[2]:
                if num > maxNums[0]:
                    tmp = maxNums[0]
                    maxNums[0] = num
                    maxNums[2] = maxNums[1]
                    maxNums[1] = tmp
                elif num > maxNums[1]:
                    maxNums[2] = maxNums[1]
                    maxNums[1] = num
                else:
                    maxNums[2] = num

        if maxNums[2] == -99999999999:
            return maxNums[0]

        return maxNums[2]

