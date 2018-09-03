# Implement wildcard pattern matching with support for '?' and '*'.

# '?' : Matches any single character.
# '*' : Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).

# The function prototype should be:

# int isMatch(const char *s, const char *p)
# Examples :

# isMatch("aa","a") → 0
# isMatch("aa","aa") → 1
# isMatch("aaa","aa") → 0
# isMatch("aa", "*") → 1
# isMatch("aa", "a*") → 1
# isMatch("ab", "?*") → 1
# isMatch("aab", "c*a*b") → 0
# Return 1/0 for this problem.


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def isMatch(self, s, p):
        s_cur = p_cur = 0
        star = match = -1
        while s_cur < len(s):
            if p_cur < len(p) and (s[s_cur] == p[p_cur] or p[p_cur] == '?'):
                s_cur += 1
                p_cur += 1
            elif p_cur < len(p) and p[p_cur] == '*':
                p_cur += 1
                star = p_cur
                match = s_cur 
            elif star != -1:
                p_cur = star
                match += 1
                s_cur = match
            else:
                return 0
        while p_cur < len(p) and p[p_cur] == '*':
            p_cur += 1
        return int(p_cur == len(p))