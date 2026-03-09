# LC 994. Rotting Oranges | Medium
from collections import deque

class Solution:
    def orangesRotting(self, grid):
        m, n = len(grid), len(grid[0]); q = deque(); fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2: q.append((i, j))
                elif grid[i][j] == 1: fresh += 1
        time = 0
        while q and fresh:
            time += 1
            for _ in range(len(q)):
                i, j = q.popleft()
                for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                        grid[ni][nj] = 2; fresh -= 1; q.append((ni, nj))
        return time if fresh == 0 else -1
