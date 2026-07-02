# Sort tasks by enqueue time + Min Heap by processing time.
import heapq

class Solution:
    def getOrder(self, tasks):
        indexed = sorted((enq, proc, i) for i, (enq, proc) in enumerate(tasks))
        heap = []
        res = []
        i = 0
        n = len(indexed)
        time = indexed[0][0]

        while i < n or heap:
            while i < n and indexed[i][0] <= time:
                enq, proc, idx = indexed[i]
                heapq.heappush(heap, (proc, idx))
                i += 1
            if not heap:
                time = indexed[i][0]
                continue
            proc, idx = heapq.heappop(heap)
            time += proc
            res.append(idx)

        return res
