# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
#
# Find the minimum element.
#
# You may assume no duplicate exists in the array.
#
# Example 1:
#
#
# Input: [3,4,5,1,2] 
# Output: 1
#
#
# Example 2:
#
#
# Input: [4,5,6,7,0,1,2]
# Output: 0
#
#




class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) is 1:
            return nums[0]

        left = 0
        right = len(nums) - 1
        first = nums[0]
        if nums[right] > nums[0]:
            return nums[0]

        while left < right:
            mid = int((left + right) / 2)
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[mid] > first:
                left = mid + 1
            else:
                right = mid - 1

        return -1
