#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
# https://leetcode.com/problems/combination-sum/description/
#
# algorithms
# Medium (49.22%)
# Likes:    2118
# Dislikes: 65
# Total Accepted:    358K
# Total Submissions: 727.3K
# Testcase Example:  '[2,3,6,7]\n7'
#
# Given a set of candidate numbers (candidates) (without duplicates) and a
# target number (target), find all unique combinations in candidates where the
# candidate numbers sums to target.
# 
# The same repeated number may be chosen from candidates unlimited number of
# times.
# 
# Note:
# 
# 
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# 
# 
# Example 1:
# 
# 
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
# ⁠ [7],
# ⁠ [2,2,3]
# ]
# 
# 
# Example 2:
# 
# 
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
# [2,2,2,2],
# [2,3,3],
# [3,5]
# ]
# 
# 
#
class Solution:
    def back_track(self, start,candidates, current_solution, final_solution, target):
        if sum(current_solution) > target:
            return
        if sum(current_solution) == target:
            final_solution.append(current_solution.copy())
            return
        
        for index in range(start, len(candidates)):
            if target < candidates[index]:
                break
            current_solution.append(candidates[index])
            self.back_track(index, candidates,
                            current_solution.copy(), final_solution, target)  # not i + 1 because we can reuse same elements
            current_solution.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        self.back_track(0, candidates, [], result, target) 
        return result


