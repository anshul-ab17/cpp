# LC 51. N-Queens | Hard
class Solution:
    def solveNQueens(self, n):
        res, cols, diag, anti = [], set(), set(), set()
        board = [['.']*n for _ in range(n)]
        def bt(row):
            if row == n: res.append([''.join(r) for r in board]); return
            for col in range(n):
                if col in cols or (row-col) in diag or (row+col) in anti: continue
                cols.add(col); diag.add(row-col); anti.add(row+col)
                board[row][col] = 'Q'; bt(row+1); board[row][col] = '.'
                cols.remove(col); diag.remove(row-col); anti.remove(row+col)
        bt(0); return res
