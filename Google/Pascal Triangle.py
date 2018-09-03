# Given numRows, generate the first numRows of Pascal’s triangle.

# Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

# Example:

# Given numRows = 5,

# Return

# [
#      [1],
#      [1,1],
#      [1,2,1],
#      [1,3,3,1],
#      [1,4,6,4,1]
# ]



class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):
        res = [[0 for x in xrange(A)] for x in xrange(A)]
        for i in xrange(A):
            for j in xrange(i+1):
                if i == 0 or j == 0 or j == i:
                    res[i][j] = 1
                    continue
                if res[i-1][j] and res[i-1][j-1]:
                    res[i][j] = res[i-1][j] + res[i-1][j-1]
                    
        rs = [res[i][:i+1] for i in xrange(A)]
        return rs