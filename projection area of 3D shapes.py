class Solution:
    def projectionArea(self, grid):
        top = 0
        front = 0
        side = 0

        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] > 0:
                    top += 1

            front += max(grid[i])

        for j in range(len(grid)):
            maximum = 0
            for i in range(len(grid)):
                maximum = max(maximum, grid[i][j])
            side += maximum

        return top + front + side
