# Given a number N, find all factors of N.

# Example:

# N = 6 
# factors = {1, 2, 3, 6}
# Make sure the returned array is sorted.


import math
class Solution:
    # @param A : integer
    # @return a list of integers
    def allFactors(self, A):   
        num = []
        if A == 1:
            num.append(1)
        elif A > 1:
            for i in xrange(1, int(math.sqrt(A))+1):
                if i*i == A:
                    num.append(i)
                elif A % i == 0:
                    num.extend([i, A/i])
            num.sort()   # nlog(n)             
        return num

    def allFactors2(self, A):
        num = []
        num1 = []
        if A == 1:
            num.append(1)
        elif A > 1:
            for i in xrange(1, int(math.sqrt(A))+1):
                if A % i == 0:
                    num.append(i)
                    if i*i != A:
                        num1.append(A/i)
            num1.reverse()   # O(n)
            num.extend(num1) # O(n)
        return num