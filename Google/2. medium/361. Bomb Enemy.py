# Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
# The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
# Note that you can only put the bomb at an empty cell.

# Example:
# For the given grid

# 0 E 0 0
# E 0 W E
# 0 E 0 0

# return 3. (Placing a bomb at (1,1) kills 3 enemies)



class Solution(object):
    def maxKilledEnemies(self, grid):		# O(mn)
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        max_hits = 0
        nums = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        
        #From Left
        for i in range(len(grid)):
            row_hits = 0
            for j in range(len(grid[0])):
                if grid[i][j] == 'E':
                    row_hits += 1
                elif grid[i][j] == 'W':
                    row_hits = 0
                else:
                    nums[i][j] = row_hits
                
            row_hits = 0
            for j in range(len(grid[0])-1, -1, -1):
                if grid[i][j] == 'W':
                    row_hits = 0
                elif grid[i][j] == 'E':
                    row_hits +=1
                else:
                    nums[i][j] += row_hits

        for i in range(len(nums[0])):
            col_hits = 0
            for col in range(len(nums)):
                if grid[col][i] == 'E':
                    col_hits += 1
                elif grid[col][i] == 'W':
                    col_hits = 0
                else:
                    nums[col][i] += col_hits

            col_hits = 0
            for col in range(len(nums)-1, -1, -1):
                if grid[col][i] == 'E':
                    col_hits +=1
                elif grid[col][i] == 'W':
                    col_hits = 0
                else:
                    nums[col][i] += col_hits
                    max_hits = max(max_hits, nums[col][i])


        return max_hits