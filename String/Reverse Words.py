# Given an input string, reverse the string word by word.

# Example:

# Given s = "the sky is blue",

# return "blue is sky the".

# A sequence of non-space characters constitutes a word.
# Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
# If there are multiple spaces between words, reduce them to a single space in the reversed string.

class Solution:
    # @param A : string
    # @return string
    def reverseWords(self, A):
        i = len(A) - 1
        S = ''
        while i >= 0:
            count = 0
            while i >= 0 and A[i] == ' ':
                count += 1
                i -= 1
            
            S += ' '
            j = i
            
            while j >= 0 and A[j] != ' ':
                j -= 1
            
            S += A[j+1:i+1]
            i = j
       	S = S.strip()
        return S