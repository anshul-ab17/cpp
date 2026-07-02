# Offline queries + DSU.
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.parent[ra] = rb

class Solution:
    def distanceLimitedPathsExist(self, n, edgeList, queries):
        edgeList.sort(key=lambda e: e[2])
        indexed_queries = sorted(range(len(queries)), key=lambda i: queries[i][2])

        dsu = DSU(n)
        res = [False] * len(queries)
        i = 0

        for qi in indexed_queries:
            p, q, limit = queries[qi]
            while i < len(edgeList) and edgeList[i][2] < limit:
                u, v, _ = edgeList[i]
                dsu.union(u, v)
                i += 1
            res[qi] = dsu.find(p) == dsu.find(q)

        return res
