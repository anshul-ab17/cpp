# Dijkstra + DP.
import heapq
from collections import defaultdict

class Solution:
    def countRestrictedPaths(self, n, edges):
        MOD = 10 ** 9 + 7
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        dist = [float('inf')] * (n + 1)
        dist[n] = 0
        heap = [(0, n)]

        while heap:
            d, node = heapq.heappop(heap)
            if d > dist[node]:
                continue
            for nxt, w in graph[node]:
                nd = d + w
                if nd < dist[nxt]:
                    dist[nxt] = nd
                    heapq.heappush(heap, (nd, nxt))

        memo = {}

        def dfs(node):
            if node == n:
                return 1
            if node in memo:
                return memo[node]
            total = 0
            for nxt, _ in graph[node]:
                if dist[nxt] < dist[node]:
                    total = (total + dfs(nxt)) % MOD
            memo[node] = total
            return total

        return dfs(1)
