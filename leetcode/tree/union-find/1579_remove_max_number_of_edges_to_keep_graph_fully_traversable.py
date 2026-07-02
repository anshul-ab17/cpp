# Two DSUs for Alice and Bob.
class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
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
    def maxNumEdgesToRemove(self, n, edges):
        alice, bob = DSU(n), DSU(n)
        used = 0

        for t, u, v in edges:
            if t == 3:
                a = alice.union(u, v)
                b = bob.union(u, v)
                if a or b:
                    used += 1

        for t, u, v in edges:
            if t == 1:
                if alice.union(u, v):
                    used += 1
            elif t == 2:
                if bob.union(u, v):
                    used += 1

        if alice.count != 1 or bob.count != 1:
            return -1

        return len(edges) - used
