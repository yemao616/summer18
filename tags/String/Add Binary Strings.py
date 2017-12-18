# Given two binary strings, return their sum (also a binary string).

# Example:

# a = "100"

# b = "11"
# Return a + b = “111”.



class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
        A = list(A[::-1])
        B = list(B[::-1])
        while len(A)<len(B):
            A.append(0)
        while len(B)<len(A):
            B.append(0)  
        m, up = len(A), 0
        for i in xrange(m):
            total = int(A[i])+int(B[i])+up
            up = total/2
            A[i] = str(total%2)
        if up:
            A.append(str(up))
        return "".join(A[::-1])



    def addBinary(self, A, B):
        a = int(A,2)
        b = int(B,2)
        c = bin(a+b)[2:]
        return c