# Given a string S, find the longest palindromic substring in S.

# Substring of string S:

# S[i...j] where 0 <= i <= j < len(S)

# Palindrome string:

# A string which reads the same backwards. More formally, S is palindrome if reverse(S) = S.

# Incase of conflict, return the substring which occurs first ( with the least starting index ).

# Example :

# Input : "aaaabaaa"
# Output : "aaabaaa"


class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):
        n = len(A)
        ans = ''
        c = 0
        for i in xrange(n):
            j = n
            while j > i:
                s = A[i:j]
                r = s[::-1]
                if s == r and j-i > c:
                    c = j-i
                    ans = s
                j -= 1
        return ans



    def longestPalindrome(self, A):
        l = len(A)
        while l > 0:
            for i in xrange(0, len(A) - l + 1):
                half = int(l / 2)
                left = A[i : i + half]
                right = A[i+l-half: i+l]
                right = right[::-1]
                if left == right:
                    return A[i:i+l]
            l -= 1
        return None