import heapq

class Solution:
    def minThresholdPath(
        self,
        n: int,
        edges: list[list[int]],
        src: int,
        dst: int,
        k: int
    ) -> int:

        adj = [[] for _ in range(n)]

        for u, v, w, heavy in edges:
            adj[u].append((v, w, heavy))
            adj[v].append((u, w, heavy))

        dist = [[float('inf')] * (k + 1) for _ in range(n)]
        dist[src][0] = 0

        pq = [(0, src, 0)]

        while pq:
            d, u, used = heapq.heappop(pq)

            if d > dist[u][used]:
                continue

            if u == dst:
                return d

            for v, w, heavy in adj[u]:
                nxt = used + (1 if heavy else 0)

                if nxt <= k and d + w < dist[v][nxt]:
                    dist[v][nxt] = d + w
                    heapq.heappush(pq, (d + w, v, nxt))

        ans = min(dist[dst])
        return ans if ans != float('inf') else -1
