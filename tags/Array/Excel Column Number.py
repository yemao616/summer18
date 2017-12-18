# Given a column title as appears in an Excel sheet, return its corresponding column number.

# Example:

#     A -> 1
    
#     B -> 2
    
#     C -> 3
    
#     ...
    
#     Z -> 26
    
#     AA -> 27
    
#     AB -> 28 

class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        n = len(A)
        s = 0
        for i in xrange(len(A)):
            s += (ord(A[i])-ord('A')+1)*(26**(n-i-1))
        return s