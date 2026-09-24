class Solution:
    def surfaceArea(self, grid):
        area = 0
        n = len(grid)

        for i in range(n):
            for j in range(n):
                h = grid[i][j]

                if h == 0:
                    continue

                # Top and bottom
                area += 2

                # Front
                if i == 0:
                    area += h
                else:
                    area += max(0, h - grid[i - 1][j])

                # Back
                if i == n - 1:
                    area += h
                else:
                    area += max(0, h - grid[i + 1][j])

                # Left
                if j == 0:
                    area += h
                else:
                    area += max(0, h - grid[i][j - 1])

                # Right
                if j == n - 1:
                    area += h
                else:
                    area += max(0, h - grid[i][j + 1])

        return area
