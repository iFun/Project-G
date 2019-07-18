#
# Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
#
# Note:
#
#
# 	All numbers will be positive integers.
# 	The solution set must not contain duplicate combinations.
#
#
# Example 1:
#
#
# Input: k = 3, n = 7
# Output: [[1,2,4]]
#
#
# Example 2:
#
#
# Input: k = 3, n = 9
# Output: [[1,2,6], [1,3,5], [2,3,4]]
#
#


#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#
# https://leetcode.com/problems/combination-sum-iii/description/
#
# algorithms
# Medium (52.09%)
# Likes:    627
# Dislikes: 31
# Total Accepted:    126.8K
# Total Submissions: 243.3K
# Testcase Example:  '3\n7'
#
# 
# Find all possible combinations of k numbers that add up to a number n, given
# that only numbers from 1 to 9 can be used and each combination should be a
# unique set of numbers.
# 
# Note:
# 
# 
# All numbers will be positive integers.
# The solution set must not contain duplicate combinations.
# 
# 
# Example 1:
# 
# 
# Input: k = 3, n = 7
# Output: [[1,2,4]]
# 
# 
# Example 2:
# 
# 
# Input: k = 3, n = 9
# Output: [[1,2,6], [1,3,5], [2,3,4]]
# 
# 
#
class Solution:
    def back_track(self, k, n, start, current, result):
        if sum(current) > n:
            return 
        if len(current) is k:
            if sum(current) is n:
                result.append(current.copy())
            return
        
        for num in range(start, 10):

            # add the current number
            current.append(num)
            self.back_track(k,n,num + 1, current.copy(), result)
            
            #skip the current number
            current.pop()
            


    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n < 2:
            if k is not 1:
                return []
            return [[1]]
        result = []

        self.back_track(k,n,1,[],result)
        return result


