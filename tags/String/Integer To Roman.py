# Given an integer, convert it to a roman numeral, and return a string corresponding to its roman numeral version

# Input is guaranteed to be within the range from 1 to 3999.

# Example :

# Input : 5
# Return : "V"

# Input : 14
# Return : "XIV"
#  Note : This question has a lot of scope of clarification from the interviewer. Please take a moment to think of all the needed clarifications and see the expected response using “See Expected Output” For the purpose of this question, https://projecteuler.net/about=roman_numerals has very detailed explanations. 



class Solution:
    # @param A : integer
    # @return a strings
    def intToRoman(self, A):
        Str = ["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"][::-1]
        Values = [1,4,5,9,10,40,50,90,100,400,500,900,1000][::-1]
        
        # Result
        roman, r = "", A
        while (r > 0):
            # iterate through units from largest to smallest
            for i in xrange(len(Values)):
                # find how many units fits into remaining
              u = Values[i]
              m = r / u
              # Can these units fit?
              if m > 0:
                s = Str[i]
                roman += s * m # append s of m
                # reduce remaining
                r -= u * m
        return roman