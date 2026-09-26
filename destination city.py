class Solution:
    def destCity(self, paths):
        start = set()

        for path in paths:
            start.add(path[0])

        for path in paths:
            if path[1] not in start:
                return path[1]
