# Given a roman numeral, convert it to an integer.

# Input is guaranteed to be within the range from 1 to 3999.

# Read more details about roman numerals at Roman Numeric System

# Example :

# Input : "XIV"
# Return : 14
# Input : "XX"
# Output : 20


class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):
        i, ans = 0, 0
        ref = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        while i<len(A):
            j = i+1
            cur = ref[A[i]]
            if j < len(A):
                nex = ref[A[j]]
                if cur < nex:
                    cur = nex - cur
                    i += 1
            ans += cur
            i +=1
        return ans
                    
                    