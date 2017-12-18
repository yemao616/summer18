
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Example:

# "A man, a plan, a canal: Panama" is a palindrome.

# "race a car" is not a palindrome.

# Return 0 / 1 ( 0 for false, 1 for true ) for this problem


import string
class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        n = len(A)
        a, b = 0, n-1
        while a < b:
            xa, xb = A[a].lower(), A[b].lower()
            if xa in string.ascii_lowercase or xa in string.digits:
                if xb in string.ascii_lowercase or xb in string.digits:
                    if xa == xb:
                        a +=1
                    else:
                        return 0
                b -= 1
            elif xb in string.ascii_lowercase or xb in string.digits:
                a += 1
            else:
                a +=1
                b -=1
        if a >= b:
            return 1
        else:
            return 0


    def isPalindrome(self, A):
        i = 0
        j = len(A)-1
        while True:
            if i>j: break
            if not A[i].isalpha() and not A[i].isdigit():
                i+=1
                continue
            if not A[j].isalpha() and not A[j].isdigit():
                j-=1
                continue
            if not A[i].lower() == A[j].lower():
                return 0
            i+=1
            j-=1
        return 1



    def isPalindrome(self, A):
        delchars = ''.join(c for c in map(chr, range(256)) if not c.isalnum())
        A = A.translate(None,delchars)
        B=A[::-1]
        if(A.lower()==B.lower()):
            return 1
        else:
            return 0