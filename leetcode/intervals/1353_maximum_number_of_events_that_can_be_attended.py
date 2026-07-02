# Greedy + Min Heap.
import heapq

class Solution:
    def maxEvents(self, events):
        events.sort()
        heap = []
        i = 0
        n = len(events)
        day = 0
        count = 0

        while i < n or heap:
            if not heap:
                day = events[i][0]
            while i < n and events[i][0] <= day:
                heapq.heappush(heap, events[i][1])
                i += 1
            heapq.heappop(heap)
            count += 1
            day += 1
            while heap and heap[0] < day:
                heapq.heappop(heap)

        return count
