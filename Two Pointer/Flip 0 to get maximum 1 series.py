# You are given with an array of 1s and 0s. And you are given with an integer M, which signifies number of flips allowed.
# Find the position of zeros which when flipped will produce maximum continuous series of 1s.

# For this problem, return the indices of maximum continuous series of 1s in order.

# Example:

# Input : 
# Array = {1 1 0 1 1 0 0 1 1 1 } 
# M = 1

# Output : 
# [0, 1, 2, 3, 4] 

# If there are multiple possible solutions, return the sequence which has the minimum start index.


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def maxone(self, A, B):
        n = len(A)
        wl = wr = best_l = best_window = count = 0
        while wr < n:
            if count <= B:
                if A[wr] == 0:
                    count += 1
                wr += 1
            if count > B:
                if A[wl] == 0:
                    count -= 1
                wl += 1
            
            if count <= B and wr -wl + 1> best_window:
                best_window = wr - wl + 1
                best_l = wl
        return range(best_l, best_l+best_window-1)