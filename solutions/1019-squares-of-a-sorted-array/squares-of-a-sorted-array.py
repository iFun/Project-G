# Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.
#
#  
#
#
# Example 1:
#
#
# Input: [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
#
#
#
# Example 2:
#
#
# Input: [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
#
#
#  
#
# Note:
#
#
# 	1 <= A.length <= 10000
# 	-10000 <= A[i] <= 10000
# 	A is sorted in non-decreasing order.
#
#
#


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        if len(A) is 1:
            return [A[0]*A[0]]
        left = 0
        right = len(A) - 1
        result = []
        while (left <= right):
            if A[left]*A[left] > A[right] * A[right]:
                result.append(A[left]*A[left])
                left += 1
            else:
                result.append(A[right]*A[right])
                right -= 1
        result.reverse()
        return result
        
