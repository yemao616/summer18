# You have to paint N boards of length {A0, A1, A2, A3 … AN-1}. There are K painters available and you are also given how much time a painter takes to paint 1 unit of board. You have to get this job done as soon as possible under the constraints that any painter will only paint contiguous sections of board.

# 2 painters cannot share a board to paint. That is to say, a board
# cannot be painted partially by one painter, and partially by another.
# A painter will only paint contiguous boards. Which means a
# configuration where painter 1 paints board 1 and 3 but not 2 is
# invalid.
# Return the ans % 10000003

# Input :
# K : Number of painters
# T : Time taken by painter to paint 1 unit of board
# L : A List which will represent length of each board

# Output:
#      return minimum time to paint all boards % 10000003
# Example

# Input : 
#   K : 2
#   T : 5
#   L : [1, 10]
# Output : 50


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def paint(self, A, B, C):
        start = max(C)
        end = sum(C)
        while start + 1 < end:
            mid = start + (end-start)/2
            required_num = self.getRequiredPainters(C, mid)
            if required_num <= A:
                end = mid
            else:
                start = mid
        if self.getRequiredPainters(C, start) <= A:
            return B * start % 10000003
        else:
            return B * end % 10000003

    def getRequiredPainters(self, l, max_per_painter):
        cur_total = 0
        num_painter = 1
        for i in range(len(l)):
            cur_total += l[i]
            if cur_total > max_per_painter:
                cur_total = l[i]
                num_painter += 1
        return num_painter