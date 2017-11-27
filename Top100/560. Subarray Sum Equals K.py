"""
Refer: http://bookshadow.com/weblog/2017/04/30/leetcode-subarray-sum-equals-k/

~Hint: Counters!!

 """

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s = ans = 0
        cnt = collections.Counter()
        for i in range(len(nums)):
            cnt[s] += 1
            s += nums[i]
            ans += cnt[s-k]
        return ans