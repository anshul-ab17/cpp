# DSU connected components on grid.
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            if self.size[ra] < self.size[rb]:
                ra, rb = rb, ra
            self.parent[rb] = ra
            self.size[ra] += self.size[rb]

class Solution:
    def largestIsland(self, grid):
        n = len(grid)
        dsu = DSU(n * n)

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    idx = r * n + c
                    if r > 0 and grid[r - 1][c] == 1:
                        dsu.union(idx, idx - n)
                    if c > 0 and grid[r][c - 1] == 1:
                        dsu.union(idx, idx - 1)

        best = max((dsu.size[dsu.find(i)] for i in range(n * n) if grid[i // n][i % n] == 1), default=0)

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    roots = set()
                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                            roots.add(dsu.find(nr * n + nc))
                    total = 1 + sum(dsu.size[root] for root in roots)
                    best = max(best, total)

        return best if best else n * n
