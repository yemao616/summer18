# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

# Example:

# [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]

# Answer: 16
# Explanation: The perimeter is the 16 yellow stripes in the image below:


class Solution(object):
    def islandPerimeter(self, grid):
        grid_ext = ['0' + ''.join(str(x) for x in row) + '0' for row in grid]
        grid_trans = list(map(list, zip(*grid)))
        grid_ext += [ '0' + ''.join(str(x) for x in row) + '0' for row in grid_trans ]                
        return sum(row.count('01') + row.count('10') for row in grid_ext)



    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        
        perimeter = 0
        height = len(grid)
        width = len(grid[0])
        for i in range(height):
            for j in range(width):
                if grid[i][j]:
                    perimeter += 4
                    if i >= 1 and grid[i-1][j]:
                        perimeter -= 2
                    if j >= 1 and grid[i][j-1]:
                        perimeter -= 2
        return perimeter