# You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

# Write a function to determine if the starting player can guarantee a win.

# For example, given s = "++++", return true. The starting player can guarantee a win by flipping the middle "++" to become "+--+".

# Follow up:
# Derive your algorithm's runtime complexity.




class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False
        n = len(s)
        memo = dict()
        def win(s):
            if s not in memo:
                memo[s] = False
                for i in xrange(len(s) - 1):
                    if s[i:i+2] == '++':
                        if not win(s[:i] + '--' + s[i+2:]):
                            memo[s] = True
                            break
            return memo[s]
        return win(s)

 """
O(2^(n/2)) time. Explanation: consider worst case with all “+”. Every possible substate(string) is visited only once. 
The number of possible substates is roughly total combinations out of n/2, which equals to 2^(n/2).
"""
class Solution(object):		
    def canWin(self, s):
        memo = {}
        def can(s):
            if s not in memo:
                memo[s] = any(s[i:i+2] == '++' and not can(s[:i] + '-' + s[i+2:])
                              for i in range(len(s)))
            return memo[s]
        return can(s)
