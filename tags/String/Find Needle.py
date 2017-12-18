# Please Note:

# Another question which belongs to the category of questions which are intentionally stated vaguely. 
# Expectation is that you will ask for correct clarification or you will state your assumptions before you start coding.

# Implement strStr().

#  strstr - locate a substring ( needle ) in a string ( haystack ). 
# Try not to use standard library string functions for this question.

# Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

#  NOTE: Good clarification questions:
# What should be the return value if the needle is empty?
# What if both haystack and needle are empty?
# For the purpose of this problem, assume that the return value should be -1 in both cases.





class Solution:
    # @param haystack : string
    # @param needle : string
    # @return an integer
    def strStr(self, haystack, needle):
        if not needle or not haystack or not needle in haystack:
            return -1
        m, n = len(haystack), len(needle)
        for i in xrange(m):
            if haystack[i] == needle[0]:
                if haystack[i:i+n] == needle:
                    return i
                elif m-i+1 < n:
                    return -1
            

	 def strStr(self, haystack, needle):
        if not haystack or not needle:
            return -1
        else:
            x = haystack.split(needle)
            if len(x[0]) == len(haystack):
                return -1
            else:
                return len(x[0])