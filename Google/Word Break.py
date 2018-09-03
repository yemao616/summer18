# Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

# For example, given

# s = "myinterviewtrainer",
# dict = ["trainer", "my", "interview"].
# Return 1 ( corresponding to true ) because "myinterviewtrainer" can be segmented as "my interview trainer".

# Return 0 / 1 ( 0 for false, 1 for true ) for this problem


class Solution:
    # @param A : string
    # @param B : list of strings
    # @return an integer
    def wordBreak(self, s, wordDict):
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(1,n+1):
            for w in wordDict:
                if i >= len(w) and dp[i-len(w)] and s[i-len(w):i]== w:
                    dp[i]=True
                    break
        return int(dp[-1])