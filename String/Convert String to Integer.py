# Implement atoi to convert a string to an integer.

# Example :

# Input : "9 2704"
# Output : 9
# Note: There might be multiple corner cases here. Clarify all your doubts using “See Expected Output”.

#  Questions: Q1. Does string contain whitespace characters before the number?
# A. Yes Q2. Can the string have garbage characters after the number?
# A. Yes. Ignore it. Q3. If no numeric character is found before encountering garbage characters, what should I do?
# A. Return 0. Q4. What if the integer overflows?
# A. Return INT_MAX if the number is positive, INT_MIN otherwise. 
# Warning : DO NOT USE LIBRARY FUNCTION FOR ATOI.
# If you do, we will disqualify your submission retroactively and give you penalty points.


class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
        s = A.strip() # strips all spaces on left and right
        if not s: 
            return 0
        sign = -1 if s[0] == '-' else 1
        val, index = 0, 0
        if s[0] in ['+', '-']: 
            index = 1
        while index < len(s) and s[index].isdigit():
            val = 10*val + int(s[index])
            index += 1
        #return sign*val
        return max(-2**31, min(sign * val,2**31-1))
