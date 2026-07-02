# Prim's MST using Min Heap.
import heapq

class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        visited = [False] * n
        heap = [(0, 0)]
        total = 0
        count = 0

        while count < n:
            cost, node = heapq.heappop(heap)
            if visited[node]:
                continue
            visited[node] = True
            total += cost
            count += 1

            x1, y1 = points[node]
            for j in range(n):
                if not visited[j]:
                    x2, y2 = points[j]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(heap, (dist, j))

        return total
