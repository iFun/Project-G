# Given a non-empty array of integers, return the k most frequent elements.
#
# Example 1:
#
#
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
#
#
#
# Example 2:
#
#
# Input: nums = [1], k = 1
# Output: [1]
#
#
# Note: 
#
#
# 	You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# 	Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
#
#


#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (55.46%)
# Likes:    1626
# Dislikes: 99
# Total Accepted:    216.9K
# Total Submissions: 391K
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# Given a non-empty array of integers, return the k most frequent elements.
# 
# Example 1:
# 
# 
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [1], k = 1
# Output: [1]
# 
# 
# Note: 
# 
# 
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is
# the array's size.
# 
# 
#
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums) # same as couting freqeuncy in the list
        return heapq.nlargest(k, count.keys(), key=count.get) 


