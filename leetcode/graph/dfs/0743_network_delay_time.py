import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times, n, k):
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))

        pq = [(0,k)]
        seen = set()
        t = 0

        while pq:
            cost,node = heapq.heappop(pq)
            if node in seen: continue
            seen.add(node)
            t = cost

            for nei,w in graph[node]:
                heapq.heappush(pq,(cost+w,nei))

        return t if len(seen)==n else -1
