# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

# For example,
# Given the following matrix:

# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# You should return [1,2,3,6,9,8,7,4,5].



# Let the array have \text{R}R rows and \text{C}C columns. \text{seen[r][c]}seen[r][c] denotes that the cell on the\text{r}r-th row and \text{c}c-th column was previously visited. Our current position is \text{(r, c)}(r, c), facing direction \text{di}di, and we want to visit \text{R}R x \text{C}C total cells.

# As we move through the matrix, our candidate next position is \text{(cr, cc)}(cr, cc). If the candidate is in the bounds of the matrix and unseen, then it becomes our next position; otherwise, our next position is the one after performing a clockwise turn.
class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix: return []
        R, C = len(matrix), len(matrix[0])
        seen = [[False] * C for _ in matrix]
        ans = []
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = di = 0
        for _ in range(R * C):
            ans.append(matrix[r][c])
            seen[r][c] = True
            cr, cc = r + dr[di], c + dc[di]
            if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]:
                r, c = cr, cc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        return ans



class Solution(object):
    def spiralOrder(self, A):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
    
        if not A:
            return []
        result = []
        a, b, c, d  = 0, len(A), 0, len(A[0])
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