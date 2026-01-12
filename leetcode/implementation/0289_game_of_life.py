# LC 289. Game of Life | Medium
class Solution:
    def gameOfLife(self, board):
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                live = 0
                for di in (-1, 0, 1):
                    for dj in (-1, 0, 1):
                        if di == 0 and dj == 0: continue
                        ni, nj = i+di, j+dj
                        if 0 <= ni < m and 0 <= nj < n and board[ni][nj] in (1, 2):
                            live += 1
                if board[i][j] == 1 and (live < 2 or live > 3): board[i][j] = 2
                elif board[i][j] == 0 and live == 3: board[i][j] = 3
        for i in range(m):
            for j in range(n): board[i][j] %= 2
