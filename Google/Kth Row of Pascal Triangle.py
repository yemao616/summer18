# Given an index k, return the kth row of the Pascal’s triangle.

# Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

# Example:

# Input : k = 3

# Return : [1,3,3,1]
#  NOTE : k is 0 based. k = 0, corresponds to the row [1]. 
# Note:Could you optimize your algorithm to use only O(k) extra space?



class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        prev = [1]
        curr = [1]
        for x in xrange(1, A+1):
            for y in xrange(x):
                if y == x-1:
                    curr.append(1)
                    prev, curr = curr, [1]
                else:
                    curr.append(prev[y]+prev[y+1])
        return prev        



# Follow up: O(n) time, O(n) space
# x[line, i] = line! / (line-i)! * i!
# x[line, i-1] = line! / (line-i+1)! * (i-1)!
    def getRow(self, A):
        if A == 0:
            return [1]
        x = [1] * (A + 1)
        for i in range(1, A):
            x[i] = x[i - 1] * (A + 1 - i) / i
        return x


    def getRow(self, A):
        arr = []
        for i in range(0,A+1):
            d = math.factorial(A)/(math.factorial(i)*math.factorial(A-i))
            arr.append(d)
        return arr  