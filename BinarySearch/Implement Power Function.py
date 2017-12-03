
# Implement pow(x, n) % d.

# In other words, given x, n and d,

# find (xn % d)

# Note that remainders on division cannot be negative. 
# In other words, make sure the answer you return is non negative.

# Input : x = 2, n = 3, d = 3
# Output : 2

# 2^3 % 3 = 8 % 3 = 2.



class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        if x == 0:
            return 0
        if n == 0:
            return 1%d
        ans=1
        square=x
        while n:
            if n%2:
                ans *= square
            square = (square*square)%d
            n = n/2
            ans=ans%d
        return ans

    def pow2(self, x, n, d):
        if n == 0:
            return 1%d
        temp = self.pow(x, n/2, d)
        return (temp*temp)%d if n%2==0 else (x*temp*temp)%d