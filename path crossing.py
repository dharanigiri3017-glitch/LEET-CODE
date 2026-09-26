class Solution:
    def isPathCrossing(self, path):
        x, y = 0, 0
        visited = {(0, 0)}

        for ch in path:
            if ch == 'N':
                y += 1
            elif ch == 'S':
                y -= 1
            elif ch == 'E':
                x += 1
            else:
                x -= 1

            if (x, y) in visited:
                return True

            visited.add((x, y))

        return False
