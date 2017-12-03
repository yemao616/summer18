# You’re given a read only array of n integers. Find out if any integer occurs more than n/3 times in the array in linear time and constant additional space.

# If so, return the integer. If not, return -1.

# If there are multiple solutions, return any one.

# Example :

# Input : [1 2 3 1 1]
# Output : 1 
# 1 occurs 3 times which is more than 5/3 times. 

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        c1 = c2 = 0
        e1 = e2 = None
        for x in A:
            if x == e1:
                c1 += 1
            elif x == e2:
                c2 += 1
            elif c1 == 0:
                e1, c1 = x, 1
            elif c2 == 0:
                e2, c2 = x, 1
            else:
                c1, c2 = c1-1, c2-1  
        for n in (e1, e2):
            if n is not None and A.count(n)>len(A)/3:
                return n
        return -1