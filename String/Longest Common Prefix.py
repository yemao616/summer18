# Write a function to find the longest common prefix string amongst an array of strings.

# Longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1 and S2.

# As an example, longest common prefix of "abcdefgh" and "abcefgh" is "abc".

# Given the array of strings, you need to find the longest S which is the prefix of ALL the strings in the array.

# Example:

# Given the array as:

# [

#   "abcdefgh",

#   "aefghijk",

#   "abcefgh"
# ]
# The answer would be “a”.




class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        if not A:
            return ""
        if len(A) == 1:
            return A[0]
        ans = ""
        for i in xrange(len(A[0])):
            s = A[0][i]
            for j in xrange(1, len(A)):
                if i < len(A[j]) and A[j][i] == s:
                    if j == len(A)-1:
                        ans += s
                else:
                    return ans
        return ans



	def longestCommonPrefix(self, strs):
	        if not strs:
	            return ""

	        for i in xrange(len(strs[0])):
	            for string in strs[1:]:
	                if i >= len(string) or string[i] != strs[0][i]:
	                    return strs[0][:i]
	        return strs[0]
