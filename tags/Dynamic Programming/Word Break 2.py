# Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

# Return all such possible sentences.

# For example, given

# s = "catsanddog",
# dict = ["cat", "cats", "and", "sand", "dog"].
# A solution is

# [
#   "cat sand dog", 
#   "cats and dog"
# ]


class Solution:
    # @param A : string
    # @param B : list of strings
    # @return a list of strings
    def wordBreak(self, s, wordDict):
        memo = {len(s): ['']}
        def sentences(i):
            if i not in memo:
                memo[i] = [s[i:j] + (tail and ' ' + tail)
                           for j in range(i+1, len(s)+1)
                           if s[i:j] in wordDict
                           for tail in sentences(j)]
            return memo[i]
        return sentences(0)