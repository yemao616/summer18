# Given a set of digits (A) in sorted order, find how many numbers of length B are possible whose value is less than number C.

#  NOTE: All numbers can only have digits from the given set. 
# Examples:

# 	Input:
# 	  3 0 1 5  
# 	  1  
# 	  2  
# 	Output:  
# 	  2 (0 and 1 are possible)  

# 	Input:
# 	  4 0 1 2 5  
# 	  2  
# 	  21  
# 	Output:
# 	  5 (10, 11, 12, 15, 20 are possible)
# Constraints:

#     1 <= B <= 9, 0 <= C <= 1e9 & 0 <= A[i] <= 9

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        if not A: return 0
        sc = str(C)
        na, nc = len(A), len(sc)
        if nc < B:
            return 0
        if nc > B:
            if B == 1:
                return na
            if A.count(0):
                return (na-1)*(na**(B-1))
            return na**B
        if nc==B:
            num = 0
            lower = [0]*B
            equal = [0]*B
            for i in xrange(B):
                y = int(sc[i])
                for x in A:
                    if x < y:
                        if x == 0:
                            if i == 0:
                                if B > 1:
                                    continue
                        lower[i] += 1
                    elif x == y:
                        equal[i] += 1
            for i in xrange(B):
                num += lower[i]*(na**(B-1-i))
                if equal[i]:    
                    continue
                else:
                    break
            return num