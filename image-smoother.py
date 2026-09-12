class Solution:
    def imageSmoother(self, img):
        m = len(img)
        n = len(img[0])

        result = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                total = 0
                count = 0

                for x in range(i - 1, i + 2):
                    for y in range(j - 1, j + 2):

                        if 0 <= x < m and 0 <= y < n:
                            total += img[x][y]
                            count += 1

                result[i][j] = total // count

        return result
