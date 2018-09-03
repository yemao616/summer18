# Given a binary grid i.e. a 2D grid only consisting of 0’s and 1’s, find the area of the largest rectangle inside the grid such that all the cells inside the chosen rectangle should have 1 in them. You are allowed to permutate the columns matrix i.e. you can arrange each of the column in any order in the final grid. Please follow the below example for more clarity.

# Lets say we are given a binary grid of 3 * 3 size.

# 1 0 1

# 0 1 0

# 1 0 0

# At present we can see that max rectangle satisfying the criteria mentioned in the problem is of 1 * 1 = 1 area i.e either of the 4 cells which contain 1 in it. Now since we are allowed to permutate the columns of the given matrix, we can take column 1 and column 3 and make them neighbours. One of the possible configuration of the grid can be:

# 1 1 0

# 0 0 1

# 1 0 0

# Now In this grid, first column is column 1, second column is column 3 and third column is column 2 from the original given grid. Now, we can see that if we calculate the max area rectangle, we get max area as 1 * 2 = 2 which is bigger than the earlier case. Hence 2 will be the answer in this case.

# ref: https://www.geeksforgeeks.org/find-the-largest-rectangle-of-1s-with-swapping-of-columns-allowed/


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        R, C = len(A), len(A[0])
        hist = [[0 for _ in range(C)] for _ in range(R)]
        hist[0] = A[0]
        
        # Step 1: Fill the auxiliary array hist[][],  O(R * C)
        for i in xrange(C):
            for j in xrange(1, R):
                if A[j][i] == 1:
                    hist[j][i] = hist[j-1][i]+1
     
        # Step 2: Sort rows of hist[][] in non-increasing order,  O(R * (R + C))
        for i in xrange(R):
            count = [0]*(R+1)
            for j in xrange(C):
                count[hist[i][j]] += 1
            col_no = 0
            for j in xrange(R, -1, -1):
                c = count[j]
                for k in xrange(c):
                    hist[i][col_no] = j
                    col_no += 1
     
        # Step 3: Traverse the sorted hist[][] to find maximum area, O(R * C)
        max_area = 0
        for i in xrange(R):
            for j in xrange(C):
                curr_area = (j+1)*hist[i][j]
                if curr_area > max_area:
                    max_area = curr_area
        return max_area

