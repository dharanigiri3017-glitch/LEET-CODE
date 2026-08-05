class Solution(object):
    def islandPerimeter(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    perimeter += 4

                    # Shared edge with cell below
                    if i + 1 < rows and grid[i + 1][j] == 1:
                        perimeter -= 2

                    # Shared edge with cell to the right
                    if j + 1 < cols and grid[i][j + 1] == 1:
                        perimeter -= 2

        return perimeter
