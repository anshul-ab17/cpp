# Dijkstra + counting shortest paths.
import heapq
from collections import defaultdict

class Solution:
    def countPaths(self, n, roads):
        MOD = 10 ** 9 + 7
        graph = defaultdict(list)
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        dist = [float('inf')] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1
        heap = [(0, 0)]

        while heap:
            d, node = heapq.heappop(heap)
            if d > dist[node]:
                continue
            for nxt, w in graph[node]:
                nd = d + w
                if nd < dist[nxt]:
                    dist[nxt] = nd
                    ways[nxt] = ways[node]
                    heapq.heappush(heap, (nd, nxt))
                elif nd == dist[nxt]:
                    ways[nxt] = (ways[nxt] + ways[node]) % MOD

        return ways[n - 1] % MOD
