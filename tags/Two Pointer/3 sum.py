# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. 
# Return the sum of the three integers.

# Assume that there will only be one solution

# Example: 
# given array S = {-1 2 1 -4}, 
# and target = 1.

# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        A.sort()
        res = 2**31
        for i in xrange(len(A)-2):
            left = i+1
            right = (len(A)-1)
            while left < right:
                s = A[i]+A[left]+A[right]
                if abs(s-B) < abs(res-B):
                    res = s
                if s == B:
                    return B
                elif s < B:
                    left += 1
                else:
                    right -=1
        return res