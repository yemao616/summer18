# A peak element is an element that is greater than its neighbors.

# Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

# You may imagine that num[-1] = num[n] = -∞.

# For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

# click to show spoilers.

# Note:
# Your solution should be in logarithmic complexity.


class Solution(object):
    def findPeakElement(self, nums):
        """
		Lets say you have a mid number at index x, nums[x]
		if (num[x+1] > nums[x]), that means a peak element HAS to exist on the right half of that array, 
		because (since every number is unique) 1. the numbers keep increasing on the right side, and the peak will be the last element. 
		2. the numbers stop increasing and there is a ‘dip’, or there exists somewhere a number such that nums[y] < nums[y-1], 
		which means number[x] is a peak element.

		This same logic can be applied to the left hand side (nums[x] < nums[x-1]).
        """
        left = 0
        right = len(nums)-1
        while left < right-1:
            mid = (left+right)/2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid
            if nums[mid] < nums[mid+1]:
                left = mid
            else:
                right = mid
        return left if nums[left] >= nums[right] else right
    #handle condition 1 and 2


    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2 or nums[0] > nums[1]:
            return 0
        for i in xrange(1, n):
            if nums[i] > nums[i-1] and (i == n-1 or nums[i] > nums[i+1]):
                return i