# Dijkstra on grid.
import heapq

class Solution:
    def minimumEffortPath(self, heights):
        rows, cols = len(heights), len(heights[0])
        effort = [[float('inf')] * cols for _ in range(rows)]
        effort[0][0] = 0
        heap = [(0, 0, 0)]

        while heap:
            e, r, c = heapq.heappop(heap)
            if r == rows - 1 and c == cols - 1:
                return e
            if e > effort[r][c]:
                continue
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    diff = abs(heights[nr][nc] - heights[r][c])
                    new_e = max(e, diff)
                    if new_e < effort[nr][nc]:
                        effort[nr][nc] = new_e
                        heapq.heappush(heap, (new_e, nr, nc))

        return 0
