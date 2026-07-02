# Fix two rows and reduce to LC 560.
# Time: O(rows^2 * cols)
from collections import defaultdict

class Solution:
    def numSubmatrixSumTarget(self, matrix, target):
        rows, cols = len(matrix), len(matrix[0])
        count = 0

        for top in range(rows):
            col_sum = [0] * cols
            for bottom in range(top, rows):
                for c in range(cols):
                    col_sum[c] += matrix[bottom][c]

                prefix_count = defaultdict(int)
                prefix_count[0] = 1
                cur = 0
                for c in range(cols):
                    cur += col_sum[c]
                    count += prefix_count[cur - target]
                    prefix_count[cur] += 1

        return count
