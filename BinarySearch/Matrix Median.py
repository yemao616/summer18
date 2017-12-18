# Given a N cross M matrix in which each row is sorted, find the overall median of the matrix. Assume N*M is odd.

# For example,

# Matrix=
# [1, 3, 5]
# [2, 6, 9]
# [3, 6, 9]

# A = [1, 2, 3, 3, 5, 6, 6, 9, 9]

# Median is 5. So, we return 5.
# Note: No extra memory is allowed.




from bisect import bisect_right
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def findMedian(self, A):
        m, n = len(A), len(A[0])
        low = high = A[0][0]
        for x in xrange(m):
            if A[x][0] < low:
                low = A[x][0]
            if A[x][n-1] > high:
                high = A[x][n-1]
                
        key = (m*n+1)/2
        while low < high:
            p = 0
            mid = (low + high)/2
            for i in xrange(m):
                p += bisect_right(A[i],mid)
            if p < key:
                low = mid+1
            else:
                high = mid
        return high



    def findMedian2(self, A):
        for i in range(1,len(A)):
            A[0].extend(A[i])
            A[i] = None
        A = sorted(A[0])
        return A[len(A)//2]