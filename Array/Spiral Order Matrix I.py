# Given a matrix of m * n elements (m rows, n columns), return all elements of the matrix in spiral order.

# Example:

# Given the following matrix:

# [
#     [ 1, 2, 3 ],
#     [ 4, 5, 6 ],
#     [ 7, 8, 9 ]
# ]
# You should return

# [1, 2, 3, 6, 9, 8, 7, 4, 5]



class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        result = []
        ## Actual code to populate result
        a = 0
        b = len(A)
        c = 0
        d = len(A[0])
        dir = 0
        while a<b and c<d:
            if dir == 0:
                for i in xrange(c, d):
                    result.append(A[a][i])
                a +=1
                dir = 1
            elif dir == 1:
                for i in xrange(a, b):
                    result.append(A[i][d-1])
                d -=1
                dir = 2
            elif dir == 2:
                for i in xrange(d-1, c-1, -1):
                    result.append(A[b-1][i])
                b -=1
                dir = 3
            else:
                for i in xrange(b-1, a-1, -1):
                    result.append(A[i][c])
                c +=1
                dir = 0
        
        return result