
class Solution:
    def matrixReshape(self, mat, r, c):
        m = len(mat)
        n = len(mat[0])

        # Check if reshape is possible
        if m * n != r * c:
            return mat

        result = [[0] * c for _ in range(r)]

        # Flatten and fill in row order
        elements = []
        for row in mat:
            for value in row:
                elements.append(value)

        index = 0

        for i in range(r):
            for j in range(c):
                result[i][j] = elements[index]
                index += 1

        return result

