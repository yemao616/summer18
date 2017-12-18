# Given a sorted array of integers, find the number of occurrences of a given target value.
# Your algorithm’s runtime complexity must be in the order of O(log n).
# If the target is not found in the array, return 0

# **Example : **
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return 2.



class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def binarysearch(self, A, B, flag): # True to indicate find the first index
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
        return ind+1

    def findCount(self, A, B):
        low = self.binarysearch(A, B, True) 
        if low:
            high = self.binarysearch(A, B, False)
            return high-low+1
        return low