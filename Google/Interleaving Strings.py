# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

# Example,
# Given:

# s1 = "aabcc",
# s2 = "dbbca",
# When s3 = "aadbbcbcac", return true.
# When s3 = "aadbbbaccc", return false.

# Return 0 / 1 ( 0 for false, 1 for true ) for this problem


class Solution:
    # @param A : string
    # @param B : string
    # @param C : string
    # @return an integer
    def isInterleave(self, A, B, C):
        # O(m*n) space
        s1, s2, s3 = A, B, C
        r, c, l= len(s1), len(s2), len(s3)
        if r+c != l:
            return 0
        dp = [[True for _ in xrange(c+1)] for _ in xrange(r+1)]
        for i in xrange(1, r+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for j in xrange(1, c+1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        for i in xrange(1, r+1):
            for j in xrange(1, c+1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i-1+j]) or \
                   (dp[i][j-1] and s2[j-1] == s3[i-1+j])
        return int(dp[-1][-1])