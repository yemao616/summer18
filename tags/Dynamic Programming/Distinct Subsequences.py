# Given two sequences S, T, count number of unique ways in sequence S, to form a subsequence that is identical to the sequence T.

#  Subsequence : A subsequence of a string is a new string which is formed from the original string by deleting some (can be none ) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not). 
# Example :

# S = "rabbbit" 
# T = "rabbit"
# Return 3. And the formations as follows:

# S1= "ra_bbit" 
# S2= "rab_bit" 
# S3="rabb_it"
# "_" marks the removed character.


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def numDistinct(self, A, B):
        A = list(A)
        m, n = len(A), len(B)
        end = 0
        for i in xrange(m):
            each = A[i]
            if each in B:
                A[end] = each
                end += 1
        m = end
        dp = [[0 for j in xrange(n+1)] for i in xrange(m+1)]
        for i in xrange(m+1):
            dp[i][0] = 1
            for j in xrange(1, n+1):
                if not i or j > i:
                    break
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[m][n]
                

    # O(n) space  
    def numDistinct(self, s, t):
        l1, l2 = len(s)+1, len(t)+1
        cur = [0] * l2
        cur[0] = 1
        for i in xrange(1, l1):
            pre = cur[:]
            for j in xrange(1, l2):
                cur[j] = pre[j] + pre[j-1]*(s[i-1] == t[j-1])
        return cur[-1]