# Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

# Example:
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output:  [1,2,4,7,5,3,6,8,9]
# Explanation:

# Note:
# The total number of elements of the given matrix will not exceed 10,000.



class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        entries = [(i+j, (j, i)[(i^j)&1], val)
           for i, row in enumerate(matrix)
           for j, val in enumerate(row)]
        return [e[2] for e in sorted(entries)]



class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if not matrix:
            return res
        dirs = [[-1, 1], [1, -1]]
        d = 0
        m ,n = len(matrix), len(matrix[0])
        x, y = 0, 0
        for k in xrange(m*n):
            res.append(matrix[x][y])
            x, y = x+dirs[d][0], y+dirs[d][1]
            if x < 0 or y < 0 or x >= m or y >= n:
                d = 1-d
                if x >= m:
                    x -= 1
                    y += 2
                if y >= n:
                    x += 2
                    y -= 1
                if x < 0:
                    x += 1
                if y < 0:
                    y += 1
        return resw