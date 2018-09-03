# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

# Find all strobogrammatic numbers that are of length = n.

# For example,
# Given n = 2, return ["11","69","88","96"].



class Solution(object):
    def findStrobogrammatic(self, n):		# O(n)* n/2
        """
        :type n: int
        :rtype: List[str]
        """
        def helper(n, m):
            if n == 0:
                return ['']
            if n == 1:
                return ['0', '1', '8']
            tmp = helper(n-2, m)
            res = []
            for s in tmp:
                if (n != m):        # last round if n==m, 0 can not be the first digit
                    res.append('0' + s + '0')
                res.append('1' + s + '1')
                res.append('6' + s + '9')
                res.append('8' + s + '8')
                res.append('9' + s + '6')
            return res
        
        return helper(n, n)