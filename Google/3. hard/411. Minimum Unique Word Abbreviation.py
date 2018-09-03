# A string such as "word" contains the following abbreviations:

# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
# Given a target string and a set of strings in a dictionary, find an abbreviation of this target string with the smallest possible length such that it does not conflict with abbreviations of the strings in the dictionary.

# Each number or letter in the abbreviation is considered length = 1. For example, the abbreviation "a32bc" has length = 4.

# Note:
# In the case of multiple answers as shown in the second example below, you may return any one of them.
# Assume length of target string = m, and dictionary size = n. You may assume that m ≤ 21, n ≤ 1000, and log2(n) + m ≤ 20.
# Examples:
# "apple", ["blade"] -> "a4" (because "5" or "4e" conflicts with "blade")

# "apple", ["plain", "amber", "blade"] -> "1p3" (other valid answers include "ap3", "a3e", "2p2", "3le", "3l1").




"""
Words in dictionary can be converted to numbers using bit manipulation.

For example, if target is apple, a dictionary word amble could be converted to a binary number bin(10011), by determining whether the letters in the same position between target and word are equal or not.

a p p l e
a m b l e
1 0 0 1 1
Abbrviation can also be converted to binary number. The letters in abbr could be converted to binary one, and the digits could be converted to zeros.
For example, one of the abbriviations of word manipulation is m2ip6n, could be converted to binary number bin(100110000001)

m a n i p u l a t i o n
m  2  i p      6      n
1 0 0 1 1 0 0 0 0 0 0 1
We can use bitwise and operator to test whether an abbreviation abbr matched some words in the dictionary. If abbr & word == abbr, then abbr matched word.
"""
class Solution(object):
    def minAbbreviation(self, target, dictionary):
        """
        :type target: str
        :type dictionary: List[str]
        :rtype: str
        """
        self.size = len(target)
        self.wlist = [self.toNumber(target, d) for d in dictionary if len(d) == self.size]
        self.ans = (1 << self.size) - 1
        self.length = self.size
        self.dfs(0, 0, 0)
        return self.toWord(self.ans, target)
    
    def dfs(self, number, depth, length):
        if length >= self.length: return
        if depth == self.size:
            if not any(number & w == number for w in self.wlist):
                self.ans = number
                self.length = length
            return
        self.dfs((number << 1) + 1, depth + 1, length + 1)
        if length == 0 or number & 1:
            for x in range(2, self.size - depth + 1):
                self.dfs(number << x, depth + x, length + 1)

    def toNumber(self, target, word):
        ans = 0
        for x in range(self.size):
            ans <<= 1
            ans += target[x] == word[x]
        return ans

    def toWord(self, number,target):
        ans = ''
        cnt = 0
        for x in range(self.size):
            if number & (1 << self.size - x - 1):
                if cnt:
                    ans += str(cnt)
                    cnt = 0
                ans += target[x]
            else:
                cnt += 1
        return ans + str(cnt or '')