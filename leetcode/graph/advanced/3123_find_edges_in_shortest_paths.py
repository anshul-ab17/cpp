# Dijkstra from source and destination.
import heapq
from collections import defaultdict

class Solution:
    def findAnswer(self, n, edges):
        graph = defaultdict(list)
        for i, (u, v, w) in enumerate(edges):
            graph[u].append((v, w, i))
            graph[v].append((u, w, i))

        def dijkstra(start):
            dist = [float('inf')] * n
            dist[start] = 0
            heap = [(0, start)]
            while heap:
                d, node = heapq.heappop(heap)
                if d > dist[node]:
                    continue
                for nxt, w, _ in graph[node]:
                    nd = d + w
                    if nd < dist[nxt]:
                        dist[nxt] = nd
                        heapq.heappush(heap, (nd, nxt))
            return dist

        dist_from_0 = dijkstra(0)
        dist_from_n = dijkstra(n - 1)
        total = dist_from_0[n - 1]

        res = [False] * len(edges)
        if total == float('inf'):
            return res

        for i, (u, v, w) in enumerate(edges):
            if dist_from_0[u] + w + dist_from_n[v] == total:
                res[i] = True
            elif dist_from_0[v] + w + dist_from_n[u] == total:
                res[i] = True

        return res
