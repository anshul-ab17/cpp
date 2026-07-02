# 3x Dijkstra.
import heapq
from collections import defaultdict

class Solution:
    def minimumWeight(self, n, edges, src1, src2, dest):
        graph = defaultdict(list)
        rgraph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            rgraph[v].append((u, w))

        def dijkstra(g, start):
            dist = [float('inf')] * n
            dist[start] = 0
            heap = [(0, start)]
            while heap:
                d, node = heapq.heappop(heap)
                if d > dist[node]:
                    continue
                for nxt, w in g[node]:
                    nd = d + w
                    if nd < dist[nxt]:
                        dist[nxt] = nd
                        heapq.heappush(heap, (nd, nxt))
            return dist

        d1 = dijkstra(graph, src1)
        d2 = dijkstra(graph, src2)
        d3 = dijkstra(rgraph, dest)

        best = min(
            (d1[i] + d2[i] + d3[i] for i in range(n)
             if d1[i] < float('inf') and d2[i] < float('inf') and d3[i] < float('inf')),
            default=-1,
        )
        return best
