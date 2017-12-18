# Given a positive integer which fits in a 32 bit signed integer, find if it can be expressed as A^P where P > 1 and A > 0. A and P both should be integers.

# Example

# Input : 4
# Output : True  
# as 2^2 = 4. 


class Solution:
    # @param A : integer
    # @return a boolean
    def isPower(self, A):
        if A ==1: 
        	return True
        for base in xrange(2, int(A**0.5)+1):
            y = A
            while y % base == 0:
                y = y / base
                if y == 1:
                    return True
        return False