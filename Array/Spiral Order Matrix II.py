# Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

# Example:

# Given n = 3,

# You should return the following matrix:

# [
#   [ 1, 2, 3 ],
#   [ 8, 9, 4 ],
#   [ 7, 6, 5 ]
# ]




class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        a = c = 0
        b = d = A
        dirc = 0
        num = 1
        res = [[0 for x in range(A)] for y in range(A)]
        while a < b and c < d:
            if dirc == 0:
                for i in xrange(c, d):
                    res[a][i] = num
                    num += 1
                a += 1
                dirc = 1
            if dirc == 1:
                for i in xrange(a, b):
                    res[i][d-1] = num
                    num += 1
                d -= 1
                dirc = 2
                
            if dirc == 2:
                for i in xrange(d-1, c-1, -1):
                    res[b-1][i] = num
                    num += 1
                b -= 1
                dirc = 3
                
            if dirc == 3:
                for i in xrange(b-1, a-1, -1):
                    res[i][c] = num
                    num += 1
                c += 1
                dirc = 0
        return res