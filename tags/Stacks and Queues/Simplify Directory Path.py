# Given an absolute path for a file (Unix-style), simplify it.

# Examples:

# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"
# Note that absolute path always begin with ‘/’ ( root directory )
# Path will not have whitespace characters.

class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):
        stack = []
        A = A.split('/')
        for a in A:
            if a == '..':
                if len(stack) > 0:
                    stack.pop()
            elif a == '.':
                continue
            elif len(a) != 0:
                stack.append(a)
        return '/'+'/'.join(stack)S