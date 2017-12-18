# Hamming distance between two non-negative integers is defined as the number of positions at which the corresponding bits are different.

# For example,

# HammingDistance(2, 7) = 2, as only the first and the third bit differs in the binary representation of 2 (010) and 7 (111).

# Given an array of N non-negative integers, find the sum of hamming distances of all pairs of integers in the array.
# Return the answer modulo 1000000007.

# Example

# Let f(x, y) be the hamming distance defined above.

# A=[2, 4, 6]

# We return,
# f(2, 2) + f(2, 4) + f(2, 6) + 
# f(4, 2) + f(4, 4) + f(4, 6) +
# f(6, 2) + f(6, 4) + f(6, 6) = 

# 0 + 2 + 1
# 2 + 0 + 1
# 1 + 1 + 0 = 8


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def hammingDistance(self, A):    # O(n^2) Not Efficient
        s = 0
        for i in xrange(len(A)-1):
            for j in xrange(i+1, len(A)):
                s += bin(A[i]^A[j]).count('1')
        return 2*s


    def hammingDistance2(self, A):
        s = 0
        n = len(A)
        for i in xrange(32):
            count = 0
            for x in A:
                if (x & (1 << i)):
                    count += 1
            s = s + count*(n-count)*2
        return s%1000000007
