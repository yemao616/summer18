# Given a string, find the rank of the string amongst its permutations sorted lexicographically. 
# Note that the characters might be repeated. If the characters are repeated, we need to look at the rank in unique permutations. 
# Look at the example for more details.

# Example :

# Input : 'aba'
# Output : 2

# The order permutations with letters 'a', 'a', and 'b' : 
# aab
# aba
# baa
# The answer might not fit in an integer, so return your answer % 1000003


from collections import Counter
mod = 1000003

class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, A):
        perm = list(A)
        rank = 1
        suffix_perms = 1
        n = len(perm)
        ctr = Counter()
        for i in range(n):
            x = perm[(n-1)-i]
            ctr[x] += 1
            inv = pow(ctr[x], mod - 2, mod)    # (1/A) % MOD = A ^ (MOD - 2) % MOD
            for y in ctr:
                if y<x:
                    rank = (rank + suffix_perms * ctr[y] * inv) % mod
            suffix_perms = (suffix_perms * (i+1) * inv) % mod
        return rank 