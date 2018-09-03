

# Given a 2D binary matrix filled with 0’s and 1’s, find the largest rectangle containing all ones and return its area.

# Bonus if you can solve it in O(n^2) or less.

# Example :

# A : [  1 1 1
#        0 1 1
#        1 0 0 
#     ]

# Output : 4 

# As the max area rectangle is created by the 2x2 rectangle created by (0,1), (0,2), (1,1) and (1,2)




class Solution:
    # @param A : list of list of integers
    # @return an integer
    def maximalRectangle(self, matrix):
        heights = [0]*(len(matrix[0])+1) # why +1 here
        max_area = 0
        for row in matrix:
            for i in xrange(len(matrix[0])):
                heights[i] = heights[i]+1 if row[i] else 0
            stack = []
            for i in xrange(len(heights)):
                while stack and heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1 if stack else i
                    max_area = max(max_area, h*w)
                stack.append(i)
        return max_area