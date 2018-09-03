# Given a sorted array of integers, find the starting and ending position of a given target value.

# Your algorithm’s runtime complexity must be in the order of O(log n).

# If the target is not found in the array, return [-1, -1].

# Example:

# Given [5, 7, 7, 8, 8, 10]

# and target value 8,

# return [3, 4].


class Solution:
    def binarysearch(self, A, B, flag):
        start, end = 0, len(A) - 1
        ind = -1
        while start <= end:
            mid = (start + end) / 2
            if B == A[mid]:
                ind = mid
                if flag:
                    end = mid-1
                else:
                    start = mid +1
            elif B < A[mid]:
                end = mid-1
            else:
                start = mid+1
        return ind

    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        high = low = self.binarysearch(A, B, True)
        if low > -1:
            high = self.binarysearch(A, B, False)
        return [low, high]