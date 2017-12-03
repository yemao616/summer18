# Given a number N, verify if N is prime or not.

# Return 1 if N is prime, else return 0.

# Example :

# Input : 7
# Output : True

class Solution:
    # @param A : integer
    # @return an integer
    def isPrime(self, A):
        if A == 2 or A == 3:
            return 1
        elif A > 3:
            if A % 2 == 0:
                return 0
            else:
                for i in xrange(3, int(A**0.5)+1, 2): # NOT A**(1/2)!!!
                    if A % i == 0: 
                        return 0
            return 1
        return 0


    def isPrime2(self, A):
        if A < 2: return 0
        upperLimit = int(A**0.5)
        for i in xrange(2, upperLimit + 1):
            if i < A and A % i == 0:
                return 0
        return 1