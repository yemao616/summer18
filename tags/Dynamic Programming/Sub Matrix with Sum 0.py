# Given a 2D matrix, find the number non-empty sub matrices, such that the sum of the elements inside the sub matrix is equal to 0. (note: elements might be negative).

# Example:

# Input

# -8 5  7
# 3  7 -8
# 5 -8  9
# Output
# 2

# Explanation
# -8 5 7
# 3 7 -8
# 5 -8 9

# -8 5 7
# 3 7 -8
# 5 -8 9



class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        m, n = len(A), len(A[0])
        total = 0
        
        for i in xrange(n):
            cur_sum = [0]*m
            for j in xrange(i, n):
                for k in xrange(m):
                    cur_sum[k] += A[k][j]
                   
                last_sum = 0
                ref = {0:0}
               
                for k in xrange(m):
                    last_sum += cur_sum[k]
                    if last_sum in ref:
                        ref[last_sum] += 1
                        total += ref[last_sum]
                    else:
                        ref[last_sum] = 0
        return total