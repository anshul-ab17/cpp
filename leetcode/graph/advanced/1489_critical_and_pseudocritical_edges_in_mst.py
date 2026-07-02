# Kruskal multiple times.
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.count = n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        self.parent[ra] = rb
        self.count -= 1
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        indexed = [(u, v, w, i) for i, (u, v, w) in enumerate(edges)]
        indexed.sort(key=lambda e: e[2])

        def mst_weight(skip=-1, force=None):
            dsu = DSU(n)
            weight = 0
            if force is not None:
                u, v, w, _ = indexed[force]
                dsu.union(u, v)
                weight += w
            for i, (u, v, w, idx) in enumerate(indexed):
                if i == skip or i == force:
                    continue
                if dsu.union(u, v):
                    weight += w
            return weight if dsu.count == 1 else float('inf')

        base = mst_weight()
        critical, pseudo = [], []

        for i in range(len(indexed)):
            idx = indexed[i][3]
            if mst_weight(skip=i) > base:
                critical.append(idx)
            elif mst_weight(force=i) == base:
                pseudo.append(idx)

        return [critical, pseudo]
