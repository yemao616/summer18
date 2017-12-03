# Determine whether an integer is a palindrome. Do this without extra space.

# A palindrome integer is an integer x for which reverse(x) = x where reverse(x) is x with its digit reversed.
# Negative numbers are not palindromic.

# Example :

# Input : 12121
# Output : True

# Input : 123
# Output : False


class Solution:
    # @param A : integer
    # @return a boolean value ( True / False )
    def isPalindrome(self, A):
        if A < 0:
            return False
        elif A < 10:
            return True
        else:
            s = ''
            n = A
            while n:
                red = n % 10
                n = n / 10
                s = s+str(red)
            return int(s)==A



    def isPalindrome2(A):
        if A < 0: 
            return False
        A = str(A)
        return A == A[::-1]



    def isPalindrome3(self, A):
        A=str(A)
        l=len(A)-1
        for i in range(int(len(A)/2)):
            if A[i]==A[l]:
                l-=1
            else:
                return False
        return True