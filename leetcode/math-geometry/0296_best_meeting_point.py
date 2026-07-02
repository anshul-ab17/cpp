# Median of row and column positions.
class Solution:
    def minTotalDistance(self, grid):
        rows = [r for r, row in enumerate(grid) for v in row if v == 1]
        cols = [c for row in grid for c, v in enumerate(row) if v == 1]
        cols.sort()

        def cost(arr):
            median = arr[len(arr) // 2]
            return sum(abs(x - median) for x in arr)

        return cost(rows) + cost(cols)
