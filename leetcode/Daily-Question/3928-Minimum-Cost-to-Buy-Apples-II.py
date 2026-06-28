import heapq

class Solution:
    def minAppleCosts(
        self,
        n: int,
        edges: list[list[int]],
        appleCosts: list[int],
        k: int
    ) -> list[int]:

        adj = [[] for _ in range(n + 1)]

        for u, v, w in edges:
            w *= (k + 1)
            adj[u].append((v, w))
            adj[v].append((u, w))

        dist = [float('inf')] * (n + 1)
        pq = []

        for i in range(1, n + 1):
            dist[i] = appleCosts[i - 1]
            heapq.heappush(pq, (dist[i], i))

        while pq:
            cost, u = heapq.heappop(pq)

            if cost > dist[u]:
                continue

            for v, w in adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))

        return dist[1:]
