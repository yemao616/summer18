# Given an integer array, return the k-th smallest distance among all the pairs. The distance of a pair (A, B) is defined as the absolute difference between A and B.

# Example 1:
# Input:
# nums = [1,3,1]
# k = 1
# Output: 0 
# Explanation:
# Here are all the pairs:
# (1,3) -> 2
# (1,1) -> 0
# (3,1) -> 2
# Then the 1st smallest distance pair is (1,1), and its distance is 0.
# Note:
# 2 <= len(nums) <= 10000.
# 0 <= nums[i] < 1000000.
# 1 <= k <= len(nums) * (len(nums) - 1) / 2.



class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        n, lo, hi = len(nums), 0, nums[-1]-nums[0]
        res = -1
        while lo <= hi:
            cnt = j = 0
            mid = (lo + hi) / 2
            for i in xrange(n):
                while j < n and abs(nums[j] -nums[i]) <= mid:
                    j += 1
                    cnt += j-i-1
            if cnt >= k:
                res = mid
                hi = mid -1
            else:
                lo = mid + 1
        return res