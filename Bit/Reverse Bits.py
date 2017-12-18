# Reverse bits of an 32 bit unsigned integer

# Example 1:

# x = 0,

#           00000000000000000000000000000000  
# =>        00000000000000000000000000000000
# return 0

# Example 2:

# x = 3,

#           00000000000000000000000000000011 
# =>        11000000000000000000000000000000
# return 3221225472


class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
    
        result = 0
        n=32
        for i in xrange(n):
            if (A >> i) & 1: result |= 1 << (n - 1 - i)
        return result