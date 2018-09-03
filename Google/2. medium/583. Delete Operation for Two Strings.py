# Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, where in each step you can delete one character in either string.

# Example 1:
# Input: "sea", "eat"
# Output: 2
# Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
# Note:
# The length of given words won't exceed 500.
# Characters in given words can only be lower-case letters.



class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        def lcs(X, Y):      # O(mn)
            m, n = len(X), len(Y)
            L = [[None] * (n + 1) for i in xrange(m + 1)]

            for i in xrange(m + 1):
                for j in xrange(n + 1):
                    if i == 0 or j == 0:
                        L[i][j] = 0
                    elif X[i - 1] == Y[j - 1]:
                        L[i][j] = L[i - 1][j - 1] + 1
                    else:
                        L[i][j] = max(L[i - 1][j], L[i][j - 1])
            return L[m][n]
        
        common = lcs(word1, word2)
        return (len(word1)+len(word2)-2*common)



    def minDistance(word1, word2):
	    L = len(word1)
	    prev = range(L + 1)
	    for c in word2:
	        cur = [0] * (L + 1)
	        cur[0] = prev[0] + 1
	        for i in xrange(L):
	            if c == word1[i]:
	                cur[i + 1] = prev[i]
	            else:
	                cur[i + 1] = min(cur[i], prev[i + 1]) + 1

	        prev = cur

	    return prev[L]