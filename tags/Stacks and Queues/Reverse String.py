# Given a string S, reverse the string using stack.

# Example :

# Input : "abc"
# Return "cba"
# PROBLEM APPROACH :

# Complete solution in hints.


class Solution:
    # @param A : string
    # @return a strings
    def reverseString(self, A):
        stack = []
        for each in A:
            stack.append(each)
        return ''.join(stack[::-1])