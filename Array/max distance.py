# Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].

# If there is no solution possible, return -1.

# Example :

# A : [3 5 4 2]

# Output : 2 
# for the pair (3, 4)


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):     # O(n)
        dis, n = -1, len(A)
        left = [0]*n
        right = [0]*n
        left[0], right[n-1] = A[0], A[n-1]
        for i in xrange(1, n):
            left[i] = min(A[i], left[i-1])
        for i in xrange(n-2,-1,-1):
            right[i] = max(A[i], right[i+1])
        i = j = 0
        while i < n and j < n:
            if right[j] >= left[i]:
                dis = max(j-i, dis)
                j += 1
            else:
                i += 1
        return dis