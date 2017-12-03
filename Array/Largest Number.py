# Given a list of non negative integers, arrange them such that they form the largest number.

# For example:

# Given [3, 30, 34, 5, 9], the largest formed number is 9534330.

# Note: The result may be very large, so you need to return a string instead of an integer.


class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        
        def mycmp(x, y):
            a, b = str(x), str(y)
            ab, ba = a+b, b+a
            if ab == ba:
                return 0
            if ab < ba:
                return -1
            else:
                return 1
        A = list(A)
        A.sort(cmp = mycmp, reverse= True)
        s = ""
        for x in A:
            s += str(x)
        s = int(s)
        return s


    def largestNumber2(self, A):
        maxlen = len(str(max(A)))
        if all(v == 0 for v in A):
            return '0'
        return ''.join(sorted((str(v) for v in A), reverse=True,
                          key=lambda i: i*(maxlen * 2 // len(i))))