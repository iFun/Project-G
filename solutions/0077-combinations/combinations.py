# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
#
# Example:
#
#
# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
#
#


#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#
# https://leetcode.com/problems/combinations/description/
#
# algorithms
# Medium (48.48%)
# Likes:    823
# Dislikes: 48
# Total Accepted:    211.7K
# Total Submissions: 436.6K
# Testcase Example:  '4\n2'
#
# Given two integers n and k, return all possible combinations of k numbers out
# of 1 ... n.
# 
# Example:
# 
# 
# Input: n = 4, k = 2
# Output:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
# 
# 
#
class Solution:

    def back_track(self, n, k, start, result, tmp_list):
        if k is 0:
            result.append(tmp_list.copy())
            return

        #need to inlcude n as well
        for number in range(start, n + 1):
            tmp_list.append(number)            
            self.back_track(n, k - 1, number + 1, result, tmp_list.copy())
            tmp_list.pop()




    def combine(self, n: int, k: int) -> List[List[int]]:
        if k is 0 or n is 0:
            return None
        result = []
        #start from 1
        self.back_track(n,k,1,result,[])
        return result


