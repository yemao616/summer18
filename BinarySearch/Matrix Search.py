# Write an efficient algorithm that searches for a value in an m x n matrix.

# This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than or equal to the last integer of the previous row.
# Example:

# Consider the following matrix:

# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# Given target = 3, return 1 ( 1 corresponds to true )

# Return 0 / 1 ( 0 if the element is not present, 1 if the element is present ) for this problem


class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        rows = len(A)
        if rows:
            columns = len(A[0])
            first_row, last_row = 0, rows-1
            while first_row <= last_row: 			# O(logm)
                mid_row = (first_row+last_row)/2
                if A[mid_row][0] < B < A[mid_row][columns-1]:
                    # call binary search
                    return self.binary_search(A[mid_row], B)
                elif A[mid_row][0] == B or A[mid_row][columns-1] == B:
                    return 1
                elif B < A[mid_row][0]:
                    last_row = mid_row-1
                elif B > A[mid_row][columns-1]:
                    first_row = mid_row+1
        return 0
        
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def binary_search(self, A, B): # O(logN)
        low, high = 0, len(A)
        while low <= high:
            mid = (low+high)/2
            if B == A[mid]:
                return 1
            elif B < A[mid]:
                high = mid - 1
            elif B > A[mid]:
                low = mid + 1
        return 0




from bisect import bisect_right, bisect_left
class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        m = len(A)
        for i in xrange(m):  
            if bisect_left(A[i],B) != bisect_right(A[i], B): # O(logN)
                return 1
        return 0