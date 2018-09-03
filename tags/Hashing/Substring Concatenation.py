# You are given a string, S, and a list of words, L, that are all of the same length.

# Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.

# Example :

# S: "barfoothefoobarman"
# L: ["foo", "bar"]
# You should return the indices: [0,9].
# (order does not matter).


class Solution:
    # @param A : string
    # @param B : tuple of strings
    # @return a list of integers
    def findSubstring(self, A, B):
        d = {}
        res = []
        windowLen = len(B) * len(B[0])
        wordLen = len(B[0])
        i = 0
        while i < (len(A)-windowLen+1):
            found = True
            d = {}
            for word in B:
                if word in d:
                    d[word] +=1
                else:    
                    d[word] = 1
                 
            for j in range(i, i+windowLen, wordLen):
                w = A[j:j+wordLen]
                if w not in d or (w in d and d[w] == 0):
                    found = False
                    break
                else:
                    d[w] -= 1
            if found:
                res.append(i)
            i += 1
        return res 