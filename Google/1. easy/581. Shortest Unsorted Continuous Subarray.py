# Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

# You need to find the shortest such subarray and output its length.

# Example 1:
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.



class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        start, end = -1, -2
        high, low = nums[0], nums[n-1]
        for i in xrange(1, n):
            high = max(high, nums[i])
            low = min(low, nums[n-i-1])
            if nums[i] < high:
                end = i
            if nums[n-i-1] > low:
                start = n-i-1
        return end-start+1