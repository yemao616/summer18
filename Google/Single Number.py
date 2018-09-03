# Given an array of integers, every element appears thrice except for one which occurs once.

# Find that element which does not appear thrice.

# Note: Your algorithm should have a linear runtime complexity.

# Could you implement it without using extra memory?

# Example :

# Input : [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
# Output : 4


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        one = two = three = 0    # one: occur only once, two: only twice
        for i in xrange(len(A)):
            two |= one & A[i];
            one ^= A[i];
            three = one & two;
            one &= ~three;
            two &= ~three;
        return one