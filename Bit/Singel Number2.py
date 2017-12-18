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
        one = two = three = 0
        for i in xrange(len(A)):
            two |= one & A[i];
            one ^= A[i];
            three = one & two;
            one &= ~three;
            two &= ~three;
        return one



    def singleNumber(self, A):
        first = 0
        second = 0
        for n in A:
            # Set the bits to first, if the bits were already set,
            # they are going to get toggled, then we check if they aren't
            # in the second variable by doign a negation of the variable and
            # an and
            first = (first ^ n) & ~second
            # We do another xor in case the first one toggled the bits, and
            # After that we need to check that we don't have any bits set in 
            # the first bitset.
            second = (second ^ n) & ~first
        return first