# Given a string, determine if a permutation of the string could form a palindrome.

# For example,
# "code" -> False, "aab" -> True, "carerac" -> True.


class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False
        setS = set(s)
        l = [s.count(i) % 2 for i in setS]
        if l.count(1) > 1:
            return False
        return True



    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == s[::-1]:
            return True
        cnt = collections.Counter(s)
        c = 0
        for key in cnt:
            if cnt[key]%2 > 0:
                c += 1
            if c > 1:
                return False
        return True
        