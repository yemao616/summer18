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
        ans = []
        tmp = [1]
        for i in xrange(A):
            ans.append(tmp)
            next_tmp = []
            for j in xrange(i+2):
                if j == 0 or j == i+1:
                    next_tmp.append(1)
                else:
                    next_tmp.append(tmp[j-1]+tmp[j])
            tmp = next_tmp

        return ans