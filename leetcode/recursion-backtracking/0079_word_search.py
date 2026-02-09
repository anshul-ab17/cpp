# LC 79. Word Search | Medium
class Solution:
    def exist(self, board, word):
        m, n = len(board), len(board[0])
        def dfs(i, j, k):
            if k == len(word): return True
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]: return False
            tmp, board[i][j] = board[i][j], '#'
            found = any(dfs(i+di, j+dj, k+1) for di, dj in [(0,1),(0,-1),(1,0),(-1,0)])
            board[i][j] = tmp; return found
        return any(dfs(i, j, 0) for i in range(m) for j in range(n))
