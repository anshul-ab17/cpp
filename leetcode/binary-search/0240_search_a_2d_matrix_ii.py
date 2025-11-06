class Solution:
    def searchMatrix(self, matrix, target):
        r, c = 0, len(matrix[0]) - 1

        # start from top-right
        while r < len(matrix) and c >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                c -= 1
            else:
                r += 1

        return False
