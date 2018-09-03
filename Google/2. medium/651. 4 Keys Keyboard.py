"""We can prove that the operations can be simplified into two types:

[1 move] Add one A.
[k+1 moves] Multiply the number of A’s by K
Say best[k] is the maximum number of A’s that can be printed after k moves. The last (simplified) operation must have been addition or multiplication. 
Thus, best[k] = max(best[k-1] + 1, best[k-2] * 1, best[k-3] * 2, best[k-4] * 3, ...)."""


class Solution(object):
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        dp=range(N+1)
        for i in xrange(3,N+1):
            dp[i]=dp[i-1]+1

            for j in xrange(i-1):
                dp[i]=max(dp[i],dp[j]*(i-j-1))
                
        return dp[-1]