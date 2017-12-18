# You are given a string. The only operation allowed is to insert characters in the beginning of the string. How many minimum characters are needed to be inserted to make the string a palindrome string

# Example:
# Input: ABC
# Output: 2
# Input: AACECAAAA
# Output: 2


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        i = n = len(A)
        while i > 0:
            s = A[:i]
            r = s[::-1]
            if s == r:
                return n-i
            i -= 1