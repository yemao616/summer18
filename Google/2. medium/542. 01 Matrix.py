# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

# The distance between two adjacent cells is 1.
# Example 1: 
# Input:

# 0 0 0
# 0 1 0
# 0 0 0
# Output:
# 0 0 0
# 0 1 0
# 0 0 0
# Example 2: 
# Input:

# 0 0 0
# 0 1 0
# 1 1 1
# Output:
# 0 0 0
# 0 1 0
# 1 2 1
# Note:
# The number of elements of the given matrix will not exceed 10,000.
# There are at least one 0 in the given matrix.
# The cells are adjacent in only four directions: up, down, left and right.




class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        answer = [[10000 * x for x in row] for row in matrix]
        for loop in range(4):
            for row in answer:
                for j in range(1, len(row)):
                    row[j] = min(row[j], row[j-1] + 1)
            answer = map(list, zip(*answer[::-1]))  # rotate 90 degree
        return answer


class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return matrix
        m, n = len(matrix), len(matrix[0])
        def whether_levelup(y, x, level):           # check four direction
            if y - 1 >= 0 and matrix[y-1][x] < level: return False
            if y + 1 < m and matrix[y+1][x] < level: return False
            if x - 1 >= 0 and matrix[y][x-1] < level: return False
            if x + 1 < n and matrix[y][x+1] < level: return False
            return True
        dq = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1: dq.append((i, j))
        level = 1
        while dq:
            level_up = []        
            for r, c in dq:
                if whether_levelup(r, c, level):
                    level_up.append((r, c))
            for r, c in level_up:
                matrix[r][c] = level + 1
            level += 1
            dq = level_up
        return matrix