# Given an integer matrix, find the length of the longest increasing path.

# From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

# Example 1:

# nums = [
#   [9,9,4],
#   [6,6,8],
#   [2,1,1]
# ]
# Return 4
# The longest increasing path is [1, 2, 6, 9].

# Example 2:

# nums = [
#   [3,4,5],
#   [3,2,6],
#   [2,2,1]
# ]
# Return 4
# The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.





class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix: 
            return 0
        self.directions = [(1,0),(-1,0),(0,1),(0,-1)]
        m, n = len(matrix), len(matrix[0])
        cache = [[-1 for _ in range(n)] for _ in range(m)]
        res = 0 
        for i in xrange(m):
            for j in xrange(n):
                res = max(res, self.dfs(matrix, i, j, cache, m, n))
        return res
        
    def dfs(self, matrix, i, j, cache, m, n):
        if cache[i][j] != -1:
            return cache[i][j]
        res = 1
        for x, y in self.directions:
            x, y = x+i, y+j
            if x < 0 or x>=m or y < 0 or y >=n or matrix[x][y] <= matrix[i][j]:
                continue
            length = 1 + self.dfs(matrix, x, y, cache, m, n)
            res = max(res, length)
        cache[i][j] = res
        return res