# Write a function that takes an unsigned integer and returns the number of 1 bits it has.

# Example:

# The 32-bit integer 11 has binary representation

# 00000000000000000000000000001011
# so the function should return 3.

class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        return bin(A).count('1')


    def numSetBits(self, A):
        numbits = 0
        while A:
            numbits += int(A % 2 == 1)
            A = A/2
        return numbits