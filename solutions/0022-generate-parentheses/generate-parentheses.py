#
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
#
#
# For example, given n = 3, a solution set is:
#
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
#


#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (55.77%)
# Likes:    2945
# Dislikes: 186
# Total Accepted:    359.8K
# Total Submissions: 645.2K
# Testcase Example:  '3'
#
# 
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
# 
# 
# 
# For example, given n = 3, a solution set is:
# 
# 
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
# 
#
class Solution:
    def back_track(self, size, left, right, current_solution, final_solution):
        if len(current_solution) is size:
            final_solution.append(current_solution)
        
        if left is not 0:
            self.back_track(size, left - 1, right + 1, 
                            current_solution + '(', final_solution)

        if right is not 0:
            self.back_track(size, left, right - 1,
                            current_solution + ')', final_solution)

    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.back_track(n*2, n, 0, '', result)
        return result


