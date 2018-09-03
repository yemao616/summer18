# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

# Return 0 / 1 ( 0 for false, 1 for true ) for this problem

# PROBLEM APPROACH :

# Complete solution in hints.


class Solution:
    # @param A : string
    # @return an integer
    def isValid(self, A):
        stack = []
        for x in A:
            if x == '(' or x == '{' or x == '[':
                stack.append(x)
            elif len(stack)>0 and abs(ord(x) - ord(stack[-1])) < 3:
                stack.pop()
            else:
                return 0
        return int(not stack)



    def isValid(self, A):    # wrong when A="[(])"
        my_map = {'(':1, '{':1000, '[':1000000, ')':-1, '}':-1000, ']':-1000000}
        total_sum=0
        for x in A:
            total_sum=total_sum+my_map[x]
        if total_sum!=0:
            return 0
        else:
            return 1
