# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# Example 1:
#
#
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
#
#
# Example 2:
#
#
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
#
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ array's length.
#


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) is 1:
            return nums[0]
        
        heap = []
        
        # because python3 heapq is a min heap so store the -1 * num
        for num in nums:
            heapq.heappush(heap, -1 * num)
        result = 0
        for _ in range(0,k):
            result = heapq.heappop(heap) * -1
            
        return result
        
