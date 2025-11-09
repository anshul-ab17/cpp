# LC 36. Valid Sudoku | Medium | Apple
class Solution:
    def isValidSudoku(self, board):
        rows, cols, boxes = [set() for _ in range(9)], [set() for _ in range(9)], [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.': continue
                d = board[i][j]; b = (i//3)*3 + j//3
                if d in rows[i] or d in cols[j] or d in boxes[b]: return False
                rows[i].add(d); cols[j].add(d); boxes[b].add(d)
        return True
