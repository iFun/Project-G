# Given two arrays, write a function to compute their intersection.
#
# Example 1:
#
#
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
#
#
#
# Example 2:
#
#
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
#
#
# Note:
#
#
# 	Each element in the result must be unique.
# 	The result can be in any order.
#
#
#  
#


# This is a Facebook interview question.
# They ask for the intersection, which has a trivial solution using a hash or a set.

# Then they ask you to solve it under these constraints:
# O(n) time and O(1) space (the resulting array of intersections is not taken into consideration).
# You are told the lists are sorted.

# Cases to take into consideration include:
# duplicates, negative values, single value lists, 0's, and empty list arguments.
# Other considerations might include
# sparse arrays.

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort() #assume sorted
        nums2.sort() #assume sorted
        
        intersections = []
        
        x = 0
        y = 0
        
        
        while x < len(nums1) and y < len(nums2):
            x_num = nums1[x]
            y_num = nums2[y]
            
            # intersected
            if x_num == y_num:
                intersections.append(x_num)
                # skip duplocate
                while x < len(nums1) and x_num == nums1[x]:
                    x += 1
                while  y < len(nums2) and y_num == nums2[y]:
                    y += 1
                # skip this loop
                continue;
            
            if (y_num > x_num):
                # this line will at least +1 to the x, if there is
                # duplicate it will keep increament
                while x < len(nums1) and x_num == nums1[x]:
                    x += 1
            else:
                while  y < len(nums2) and y_num == nums2[y]:
                    y += 1
        
        return intersections
                

            
            
            
            
            
            
