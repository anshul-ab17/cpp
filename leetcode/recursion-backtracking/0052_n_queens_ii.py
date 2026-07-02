# Same as LC 51; return count only.
class Solution:
    def totalNQueens(self, n):
        cols, diag, anti = set(), set(), set()
        count = 0

        def backtrack(row):
            nonlocal count
            if row == n:
                count += 1
                return
            for col in range(n):
                if col in cols or (row - col) in diag or (row + col) in anti:
                    continue
                cols.add(col); diag.add(row - col); anti.add(row + col)
                backtrack(row + 1)
                cols.remove(col); diag.remove(row - col); anti.remove(row + col)

        backtrack(0)
        return count
