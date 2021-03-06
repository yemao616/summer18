# You are given an array of N non-negative integers, A0, A1 ,…, AN-1.
# Considering each array element Ai as the edge length of some line segment, count the number of triangles which you can form using these array values.

# Notes:

# You can use any value only once while forming each triangle. Order of choosing the edge lengths doesn’t matter. Any triangle formed should have a positive area.

# Return answer modulo 109 + 7.

# For example,

# A = [1, 1, 1, 2, 2]

# Return: 4


class Solution:
    # @param A : list of integers
    # @return an integer
    def nTriang(self, A):
        A.sort()
        count = 0
        for i in xrange(len(A) - 2):
            right = i+2
            for j in xrange(i+1, len(A)-1):
                while right < len(A) and A[i] + A[j] > A[right]:
                    right += 1
                count += right-1-j
        return count % (10**9 + 7)