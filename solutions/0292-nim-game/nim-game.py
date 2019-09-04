# You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.
#
# Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.
#
# Example:
#
#
# Input: 4
# Output: false 
# Explanation: If there are 4 stones in the heap, then you will never win the game;
#              No matter 1, 2, or 3 stones you remove, the last stone will always be 
#              removed by your friend.


#
# @lc app=leetcode id=292 lang=python3
#
# [292] Nim Game
#
# https://leetcode.com/problems/nim-game/description/
#
# algorithms
# Easy (55.71%)
# Likes:    382
# Dislikes: 1174
# Total Accepted:    187K
# Total Submissions: 335.6K
# Testcase Example:  '4'
#
# You are playing the following Nim Game with your friend: There is a heap of
# stones on the table, each time one of you take turns to remove 1 to 3 stones.
# The one who removes the last stone will be the winner. You will take the
# first turn to remove the stones.
#
# Both of you are very clever and have optimal strategies for the game. Write a
# function to determine whether you can win the game given the number of stones
# in the heap.
#
# Example:
#
#
# Input: 4
# Output: false
# Explanation: If there are 4 stones in the heap, then you will never win the
# game;
# No matter 1, 2, or 3 stones you remove, the last stone will always
# be
# removed by your friend.
#


class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0


"""
Basing on explanation you can assume it's your turn. 

1. When there's 1,2 or 3 stones you just win in the first move.
2. When there is 4 stones, you can do anything and villain will win in next move.
3. When there are 5,6 or 7 stones, you can put villain in a situation with 4 stones, so you always win.
4. When there are 8 stones whatever you do, villain will be anle to put you on 4 stones.
5. When there are 9,10 or 11 stones you can put villain in a situation with 8 stones and so on. 

The only losing situation is when there is number of stones divisible by 4. Other way you just put villain in divisible by 4 situation and you win. 
"""

