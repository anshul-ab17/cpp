# Dynamic DSU on grid.
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.count = 0

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.parent[ra] = rb
            self.count -= 1

class Solution:
    def numIslands2(self, m, n, positions):
        dsu = DSU(m * n)
        grid = [[False] * n for _ in range(m)]
        res = []

        for r, c in positions:
            if grid[r][c]:
                res.append(dsu.count)
                continue
            grid[r][c] = True
            dsu.count += 1
            idx = r * n + c
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc]:
                    dsu.union(idx, nr * n + nc)
            res.append(dsu.count)

        return res
