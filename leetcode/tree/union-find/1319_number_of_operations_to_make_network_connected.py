class Solution:
    def makeConnected(self, n, connections):
        if len(connections) < n-1:
            return -1

        dsu = DSU(n)
        for u,v in connections:
            dsu.union(u,v)

        return len({dsu.find(i) for i in range(n)}) - 1
