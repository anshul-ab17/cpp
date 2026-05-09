# LC 1091. Shortest Path in Binary Matrix | Medium
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]: return -1
        q = deque([(0, 0, 1)]); grid[0][0] = 1
        while q:
            i, j, d = q.popleft()
            if i == n-1 and j == n-1: return d
            for di in (-1,0,1):
                for dj in (-1,0,1):
                    ni, nj = i+di, j+dj
                    if 0 <= ni < n and 0 <= nj < n and not grid[ni][nj]:
                        grid[ni][nj] = 1; q.append((ni, nj, d+1))
        return -1
