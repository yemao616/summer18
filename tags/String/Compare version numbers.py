# Compare two version numbers version1 and version2.

# If version1 > version2 return 1,
# If version1 < version2 return -1,
# otherwise return 0.
# You may assume that the version strings are non-empty and contain only digits and the . character.
# The . character does not represent a decimal point and is used to separate number sequences.
# For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

# Here is an example of version numbers ordering:

# 0.1 < 1.1 < 1.2 < 1.13 < 1.13.4



class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def compareVersion(self, A, B):
        x = A.split('.')
        y = B.split('.')
        while len(x)<len(y):
            x.append(0)
        while len(y)<len(x):
            y.append(0)
            
        for i in xrange(len(x)):
            a, b = int(x[i]), int(y[i])
            if a > b:
                return 1
            elif a < b:
                return -1
        return 0


    def compareVersion(self, A, B):
        v1 = A.split('.')
        v2 = B.split('.')
        
        if len(v1) < len(v2):
            while len(v1) < len(v2):
                v1.append('0')
        elif len(v2) < len(v1):
            while len(v2) < len(v1):
                v2.append('0')
                
        for x,y in zip(v1,v2):
            if int(x) < int(y):
                return -1
            if int(y) < int(x):
                return 1
        return 0