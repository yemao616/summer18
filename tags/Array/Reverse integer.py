# Reverse digits of an integer.

# Example1:

# x = 123,

# return 321
# Example2:

# x = -123,

# return -321

# Return 0 if the result overflows and does not fit in a 32 bit signed integer


class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        f = ''
        if A < 0:
            A = -A
            f += '-'
        A = str(A)
        ans = int(f+A[::-1])
        if ans >=-2**31 and ans < 2**31:
            ans = 0
        return ans


    def reverse(self, A):
        
        if -10 < A < 10:
            return A
        
        ans = int(str(A).lstrip('-')[::-1])
        ans = -1 * ans if A < 0 else ans 
        
        if not (-2147483648 < ans < 2147483647):
            return 0 
        else:
            return ans 