# DSU + sorting meetings by time.
from collections import defaultdict

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
    def findAllPeople(self, n, meetings, firstPerson):
        dsu = DSU(n)
        dsu.union(0, firstPerson)

        by_time = defaultdict(list)
        for x, y, t in meetings:
            by_time[t].append((x, y))

        for t in sorted(by_time):
            pairs = by_time[t]
            people = set()
            for x, y in pairs:
                dsu.union(x, y)
                people.add(x)
                people.add(y)

            root0 = dsu.find(0)
            for p in people:
                if dsu.find(p) != root0:
                    dsu.parent[p] = p

        root0 = dsu.find(0)
        return [i for i in range(n) if dsu.find(i) == root0]
