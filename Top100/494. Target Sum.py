"""
Refer: http://bookshadow.com/weblog/2017/01/22/leetcode-target-sum/

~Hint: Dynamic Programming!!
	   dp[k] stores the former information
	   ndp stores the extended information with new number from input

"""

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        dp = collections.Counter()
        dp[0] = 1
        for n in nums:
            ndp = collections.Counter()
            for sgn in (1, -1):
                for k in dp.keys():
                    ndp[k + n * sgn] += dp[k]
            dp = ndp
        return dp[S]