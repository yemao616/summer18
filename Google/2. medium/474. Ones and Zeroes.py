# In the computer world, use restricted resource you have to generate maximum benefit is what we always want to pursue.

# For now, suppose you are a dominator of m 0s and n 1s respectively. On the other hand, there is an array with strings consisting of only 0s and 1s.

# Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.

# Note:
# The given numbers of 0s and 1s will both not exceed 100
# The size of given string array won't exceed 600.
# Example 1:
# Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
# Output: 4

# Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are “10,”0001”,”1”,”0”
# Example 2:
# Input: Array = {"10", "0", "1"}, m = 1, n = 1
# Output: 2

# Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".



# This question is very similar to a 0-1 knapsack, the transition function is

# dp(k, x, y) = max(dp(k-1, x-z, y-o) + 1, dp(k-1, x, y))   (z is zeroes in strs[k], o is ones in strs[k])
# dp(k, x, y) is the maximum strs we can include when we have x zeros, y ones and only the first k strs are considered.

# dp(len(strs), M, N) is the answer we are looking for

# I first implemented a dfs + memoization, which gets MLE, so I created a bottom up style dp.
# With bottom up, we can use something called “rolling array” to optimize space complexity from O(KMN) to O(MN)

class Solution(object):
	def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        def count(s):
            return sum(1 for c in s if c == '0'), sum(1 for c in s if c == '1')
        
        for z, o in [count(s) for s in strs]:
            for x in range(m, -1, -1):
                for y in range(n, -1, -1):
                    if x >= z and y >= o:
                        dp[x][y] = max(1 + dp[x-z][y-o], dp[x][y])
                        
        return dp[m][n]




    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        A = sorted(strs, key = lambda x:(len(x), x))
        #print A
        f = [0] * (1 + len(A))
        r1, r0 = [0] * (1 + len(A)), [0] * (1 + len(A))
        r1[0], r0[0] = n, m # denote the amount after used at i
        # expand
        for i in xrange(1, len(A) + 1):
            n1, n0 = A[i-1].count('1') , A[i-1].count('0')
            for j in xrange(i):
                if r1[j] < n1 or r0[j] < n0: continue
                if f[i] < f[j] + 1 or (f[i] == f[j] + 1 and r1[j] - n1 >= r1[i] and r0[j] - n0 >= r0[i]):
                    f[i] = f[j] + 1
                    r0[i] = r0[j] - n0
                    r1[i] = r1[j] - n1
        return max(f)
                    
                    
                
        