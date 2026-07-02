# Dijkstra maximizing probability.
import heapq
from collections import defaultdict

class Solution:
    def maxProbability(self, n, edges, succProb, start, end):
        graph = defaultdict(list)
        for (u, v), p in zip(edges, succProb):
            graph[u].append((v, p))
            graph[v].append((u, p))

        prob = [0.0] * n
        prob[start] = 1.0
        heap = [(-1.0, start)]

        while heap:
            neg_p, node = heapq.heappop(heap)
            p = -neg_p
            if node == end:
                return p
            if p < prob[node]:
                continue
            for nxt, edge_p in graph[node]:
                new_p = p * edge_p
                if new_p > prob[nxt]:
                    prob[nxt] = new_p
                    heapq.heappush(heap, (-new_p, nxt))

        return 0.0
