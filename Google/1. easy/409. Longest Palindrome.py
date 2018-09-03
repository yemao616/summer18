# Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

# This is case sensitive, for example "Aa" is not considered a palindrome here.

# Note:
# Assume the length of given string will not exceed 1,010.

# Example:

# Input:
# "abccccdd"

# Output:
# 7

# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.


import collections
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = collections.Counter(s)
        res = 0
        flag = 0
        for key in cnt:
            tmp = cnt[key]
            res += tmp
            if tmp % 2 != 0:
                res -= 1
                flag = 1
        
        return res+flag