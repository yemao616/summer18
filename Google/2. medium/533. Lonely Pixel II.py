
# Given a picture consisting of black and white pixels, and a positive integer N, find the number of black pixels located at some specific row R and column C that align with all the following rules:

# Row R and column C both contain exactly N black pixels.
# For all rows that have a black pixel at column C, they should be exactly the same as row R
# The picture is represented by a 2D char array consisting of 'B' and 'W', which means black and white pixels respectively.

# Example:
# Input:                                            
# [['W', 'B', 'W', 'B', 'B', 'W'],    
#  ['W', 'B', 'W', 'B', 'B', 'W'],    
#  ['W', 'B', 'W', 'B', 'B', 'W'],    
#  ['W', 'W', 'B', 'W', 'B', 'W']] 

# N = 3
# Output: 6
# Explanation: All the bold 'B' are the black pixels we need (all 'B's at column 1 and 3).
#         0    1    2    3    4    5         column index                                            
# 0    [['W', 'B', 'W', 'B', 'B', 'W'],    
# 1     ['W', 'B', 'W', 'B', 'B', 'W'],    
# 2     ['W', 'B', 'W', 'B', 'B', 'W'],    
# 3     ['W', 'W', 'B', 'W', 'B', 'W']]    
# row index

# Take 'B' at row R = 0 and column C = 1 as an example:
# Rule 1, row R = 0 and column C = 1 both have exactly N = 3 black pixels. 
# Rule 2, the rows have black pixel at column C = 1 are row 0, row 1 and row 2. They are exactly the same as row R = 0.


class Solution(object):
    def findBlackPixel(self, picture, N):		# O(m*n)
        """
        :type picture: List[List[str]]
        :type N: int
        :rtype: int
        """
        ctr = collections.Counter(map(tuple, picture))
        cols = [col.count('B') for col in zip(*picture)]
        return sum(N * zip(row, cols).count(('B', N))      # check number of columns in such rows
                   for row, count in ctr.items()
                   if count == N == row.count('B'))			# check requirements for row



def findBlackPixel(self, picture, N):
    """
    :type picture: List[List[str]]
    :type N: int
    :rtype: int
    """
    count = 0
    for c in zip(*picture):
        if c.count('B') != N: continue
        first_row = picture[c.index('B')]
        if first_row.count('B') != N: continue
        if picture.count(first_row) != N: continue
        count += 1
    return count*N