# Given an integer n, return the number of trailing zeroes in n!.

# Note: Your solution should be in logarithmic time complexity.

# Example :

# n = 5
# n! = 120 
# Number of trailing zeros = 1
# So, return 1



class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        ans, d = 0, 5
        while d <= A:
            ans += A/d
            d *= 5
        return ans