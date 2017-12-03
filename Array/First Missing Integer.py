# Given an unsorted integer array, find the first missing positive integer.

# Example:

# Given [1,2,0] return 3,

# [3,4,-1,1] return 2,

# [-8, -7, -6] returns 1

# Your algorithm should run in O(n) time and use constant space.


def firstMissingPositive(self, A):
        n = len(A)
        for i in xrange(n):
            if A[i] <0: 
            	A[i] = n+1
        for x in A:
            if abs(x) < n+1: 
               A[abs(x)-1] = -A[abs(x)-1]
        for i in xrange(n):
            if A[i] > 0:
               return i+1
        return n+1