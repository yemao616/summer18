# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

# For "(()", the longest valid parentheses substring is "()", which has length = 2.

# Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.


class Solution:
    # @param A : string
    # @return an integer
    def longestValidParentheses(self, A):
        stack = []
        for i, el in enumerate(A):
            if el == '(':
                stack.append(i)
            elif stack and A[stack[-1]] == '(':
                stack.pop()
            else:
                stack.append(i)
        if not stack:
            return len(A)
        longest = y = 0
        x = len(A)
        while stack:
            y = stack.pop()
            longest = max(longest, x - y - 1)
            x = y
        return max(longest, x)



    def longestValidParentheses(self, s):
        stack = [0]
        for x in s:
            if x == '(':
                stack.append(1)
            elif stack[-1] & 1 == 1:
                a = stack.pop()
                stack[-1] += a + 1
            else:
                stack.append(0)

        return max(i for i in stack)//2 * 2