# Given two words A and B, find the minimum number of steps required to convert A to B. (each operation is counted as 1 step.)

# You have the following 3 operations permitted on a word:

# Insert a character
# Delete a character
# Replace a character
# Example : 
# edit distance between
# "Anshuman" and "Antihuman" is 2.

# Operation 1: Replace s with t.
# Operation 2: Insert i.


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def minDistance(self, A, B):		# O(m*n)
        m, n = len(A), len(B)
        dp = [[0 for j in xrange(n+1)] for i in xrange(m+1)]
        for i in xrange(m+1):
            dp[i][0] = i
        for j in xrange(n+1):
            dp[0][j] = j
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1]+1, dp[i-1][j]+1, dp[i-1][j-1]+1)
        return dp[m][n]


    def minDistance(self, A, B):
        prev, curr = range(len(A)+1), [len(A)]
        for i, bi in enumerate(B):
            curr = [i+1]
            for j, aj in enumerate(A):
                if aj == bi:
                    val = prev[j]
                else:
                    val = min(prev[j], prev[j+1], curr[j])+1
                curr.append(val)
            #print(prev, curr)
            prev = curr
        #print([prev])
        return curr[-1]
