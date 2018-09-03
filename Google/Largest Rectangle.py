# Given n non-negative integers representing the histogram’s bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

# Largest Rectangle in Histogram: Example 1

# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

# Largest Rectangle in Histogram: Example 2

# The largest rectangle is shown in the shaded area, which has area = 10 unit.

# For example,
# Given height = [2,1,5,6,2,3],
# return 10.


class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, A):
        stack = []
        area, i = 0, 0
        while i < len(A):
            x = A[i]
            if not stack or x >= A[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                ind = stack.pop()
                if stack:
                    wid = i-stack[-1]-1   # handle unsorted array to get the true width
                else:
                    wid = i
                area = max(area, A[ind]*wid)
                
        while stack:
            ind = stack.pop()
            if stack:
                wid = i-stack[-1]-1  
            else:
                wid = i
            area = max(area, A[ind]*wid)
        return area