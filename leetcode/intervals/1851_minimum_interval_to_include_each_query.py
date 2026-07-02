# Sort intervals and queries + Min Heap.
import heapq

class Solution:
    def minInterval(self, intervals, queries):
        intervals.sort()
        indexed_queries = sorted(range(len(queries)), key=lambda i: queries[i])
        res = [-1] * len(queries)

        heap = []
        i = 0
        n = len(intervals)

        for qi in indexed_queries:
            q = queries[qi]
            while i < n and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(heap, (r - l + 1, r))
                i += 1
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            if heap:
                res[qi] = heap[0][0]

        return res
