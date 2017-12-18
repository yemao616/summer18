# Given a number N >= 0, find its representation in binary.

# Example:

# if N = 6,

# binary form = 110

class Solution:
    # @param A : integer
    # @return a strings
    def findDigitsInBinary1(self, A):
        get_bin = lambda x: format(x, 'b')
        return get_bin(A)


    def findDigitsInBinary2(self, A):
        if A == 0:
        	return 0
        s = ""
        while A:
        	if A & 1 == 1:
        		s += "1"
        	else:
        		s += "0"
        	A /= 2
        return s

    def findDigitsInBinary3(self, A):
    	return bin(A)[2:]


    def findDigitsInBinary4(self, A):
        if A == 0:
            return '0'
        
        s = ''
        while ( A > 0):
            rem = A%2
            s += str(rem)
            A = A/2
            
        return s[::-1] #return reversal of string


    def findDigitsInBinary5(self, A):
        i = 1
        s = 0
        while A > 0:
            rem = A % 2
            s = s + (i * rem)
            A = A / 2
            i = i * 10
        return s