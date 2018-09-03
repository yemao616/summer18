# Implement pow(A, B) % C.

# In other words, given A, B and C, 
# find (AB)%C.

# Input : A = 2, B = 3, C = 3
# Return : 2 
# 2^3 % 3 = 8 % 3 = 2


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def Mod(self, A, B, C):
        if B == 0:
            return 1%C
        elif B % 2 == 0:
            x = self.Mod(A, B/2, C)
            return (x*x)% C
        else:
            return (A%C)*self.Mod(A, B-1, C)%C