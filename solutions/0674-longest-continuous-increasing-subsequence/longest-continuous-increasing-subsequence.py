#
# Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).
#
#
# Example 1:
#
# Input: [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
# Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 
#
#
#
# Example 2:
#
# Input: [2,2,2,2,2]
# Output: 1
# Explanation: The longest continuous increasing subsequence is [2], its length is 1. 
#
#
#
# Note:
# Length of the array will not exceed 10,000.
#


#
# @lc app=leetcode id=674 lang=python3
#
# [674] Longest Continuous Increasing Subsequence
#
# https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/
#
# algorithms
# Easy (44.80%)
# Likes:    494
# Dislikes: 101
# Total Accepted:    76.8K
# Total Submissions: 171.4K
# Testcase Example:  '[1,3,5,4,7]'
#
#
# Given an unsorted array of integers, find the length of longest continuous
# increasing subsequence (subarray).
#
#
# Example 1:
#
# Input: [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5], its
# length is 3.
# Even though [1,3,5,7] is also an increasing subsequence, it's not a
# continuous one where 5 and 7 are separated by 4.
#
#
#
# Example 2:
#
# Input: [2,2,2,2,2]
# Output: 1
# Explanation: The longest continuous increasing subsequence is [2], its length
# is 1.
#
#
#
# Note:
# Length of the array will not exceed 10,000.
#
#


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) < 2:
            return 1

        prev = -999999999999
        result = 1
        tmp = 0

        for num in nums:
            if num > prev:
                tmp += 1
                result = max(tmp, result)
            else:
                tmp = 1

            prev = num

        return result

