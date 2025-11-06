class Solution:
    def searchMatrix(self, matrix, target):
        rows, cols = len(matrix), len(matrix[0])

        l, r = 0, rows * cols - 1

        while l <= r:
            m = (l + r) // 2

            # convert 1D index -> 2D index
            val = matrix[m // cols][m % cols]

            if val == target:
                return True
            elif val < target:
                l = m + 1
            else:
                r = m - 1

        return False
