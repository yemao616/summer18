# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.



class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        MIN = 1999999999
        ab = "abcdefghijklmnopqrstuvwxyz"
        for x in ab:
            idx = s.find(x)
            if idx != -1:
                if idx == s.rfind(x): # ONLY ONCE
                    if idx < MIN:
                        MIN = idx
                        
        return -1 if MIN == 1999999999 else MIN



    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters='abcdefghijklmnopqrstuvwxyz'
        index=[s.index(l) for l in letters if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1