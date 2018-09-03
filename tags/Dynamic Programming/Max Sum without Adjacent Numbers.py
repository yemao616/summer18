# Given a 2 * N Grid of numbers, choose numbers such that the sum of the numbers
# is maximum and no two chosen numbers are adjacent horizontally, vertically or diagonally, and return it.

# Example:

# Grid:
# 	1 2 3 4
# 	2 3 4 5
# so we will choose
# 3 and 5 so sum will be 3 + 5 = 8


# Note that you can choose more than 2 numbers


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def adjacent(self, A):
        incl = 0
        excl = 0
        for i in range(len(A[0])):
            num = max(A[0][i], A[1][i])
            tmp = max(incl, excl)
            incl = excl + num
            excl = tmp
        return max(excl,incl)