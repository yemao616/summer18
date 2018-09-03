Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
Note:
1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].




class Solution(object):

    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        if n * k == 0 or k > n:
            return 0
        res = sum(nums[0:k])
        cur = res
        for i in range(k, n):
            cur -= nums[i-k]
            cur += nums[i]
            if cur > res:
                res = cur
        return float(res) / k



    def findMaxAverage(self, nums, k):
        P = [0]
        for x in nums:
            P.append(P[-1] + x)

        ma = max(P[i+k] - P[i] for i in xrange(len(nums) - k + 1))
        return ma / float(k)