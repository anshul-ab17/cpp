from collections import deque

class Solution:
    def shortestPathLength(self, graph):
        n = len(graph)

        q = deque()

        seen = set()

        for i in range(n):
            q.append((i, 1 << i, 0))
            seen.add((i, 1 << i))

        final_mask = (1 << n) - 1

        while q:
            node, mask, dist = q.popleft()

            if mask == final_mask:
                return dist

            for nei in graph[node]:
                nxt = mask | (1 << nei)

                if (nei, nxt) not in seen:
                    seen.add((nei, nxt))
                    q.append((nei, nxt, dist + 1))
