
# Given a string, find the rank of the string amongst its permutations sorted lexicographically. 
# Assume that no characters are repeated.

# Example :

# Input : 'acb'
# Output : 2

# The order permutations with letters 'a', 'c', and 'b' : 
# abc
# acb
# bac
# bca
# cab
# cba
# The answer might not fit in an integer, so return your answer % 1000003



class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, A):
        s = list(A)
        s.sort()
        n = len(A)
        rank = 1
        for j in xrange(n):
            r = s.index(A[j])
            if r:
                for i in xrange(2, n-j):
                    r *= i
                rank += r
            s = [x for x in s if x != A[j]]
        return rank%1000003


    def findRank2(self, A):
        perm = list(A)
        rank = 1
        suffixperms = 1
        ctr = Counter()
        for i in xrange(len(perm)):
            x = perm[((len(perm) - 1) - i)]
            ctr[x] = (ctr[x] + 1) % MOD
            for y in ctr:
                if y < x:
                    rank = (rank + ((suffixperms * ctr[y]) // ctr[x]) % MOD) % MOD
            suffixperms = ((suffixperms * (i + 1)) // ctr[x]) % MOD
        return rank