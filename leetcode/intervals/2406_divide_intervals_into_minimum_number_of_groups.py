# Similar to Meeting Rooms II using Min Heap.
import heapq

class Solution:
    def minGroups(self, intervals):
        intervals.sort()
        heap = []

        for start, end in intervals:
            if heap and heap[0] < start:
                heapq.heapreplace(heap, end)
            else:
                heapq.heappush(heap, end)

        return len(heap)
