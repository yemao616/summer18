# Given a string s, partition s such that every string of the partition is a palindrome.

# Return all possible palindrome partitioning of s.

# For example, given s = "aab",
# Return

#   [
#     ["a","a","b"]
#     ["aa","b"],
#   ]
#  Ordering the results in the answer : Entry i will come before Entry j if :
# len(Entryi[0]) < len(Entryj[0]) OR
# (len(Entryi[0]) == len(Entryj[0]) AND len(Entryi[1]) < len(Entryj[1])) OR
# *
# *
# *
# (len(Entryi[0]) == len(Entryj[0]) AND … len(Entryi[k] < len(Entryj[k]))
# In the given example,
# ["a", "a", "b"] comes before ["aa", "b"] because len("a") < len("aa")


class Solution:
    # @param A : string
    # @return a list of list of strings
    def partition(self, A):
        res = []
        self.dfs(A, [], res)
        return res
    
    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s)+1):
            if self.isPal(s[:i]):
                self.dfs(s[i:], path+[s[:i]], res)
        
    def isPal(self, s):
        return s == s[::-1]