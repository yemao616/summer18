# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in linear time complexity.
# Note that when the count of a character C in T is N, then the count of C in minimum window in S should be at least N.

# Example :

# S = "ADOBECODEBANC"
# T = "ABC"
# Minimum window is "BANC"

#  Note:
# If there is no such window in S that covers all characters in T, return the empty string ''.
# If there are multiple such windows, return the first occurring minimum window ( with minimum start index ).


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need, missing = collections.Counter(t), len(t)
        i = I = J = 0
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or j - i <= J - I:
                    I, J = i, j
        return s[I:J]