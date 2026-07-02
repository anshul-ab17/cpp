# Build 2D prefix sum and query each block in O(1).
class Solution:
    def matrixBlockSum(self, mat, k):
        rows, cols = len(mat), len(mat[0])
        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(rows):
            for c in range(cols):
                prefix[r + 1][c + 1] = (
                    mat[r][c] + prefix[r][c + 1] + prefix[r + 1][c] - prefix[r][c]
                )

        res = [[0] * cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                r1, c1 = max(0, r - k), max(0, c - k)
                r2, c2 = min(rows, r + k + 1), min(cols, c + k + 1)
                res[r][c] = (
                    prefix[r2][c2] - prefix[r1][c2] - prefix[r2][c1] + prefix[r1][c1]
                )

        return res
