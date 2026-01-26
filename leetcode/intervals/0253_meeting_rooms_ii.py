import heapq
class Solution:
    def minMeetingRooms(self, intervals):
        intervals.sort()
        heap = []

        for s, e in intervals:
            if heap and heap[0] <= s:
                heapq.heappop(heap)
            heapq.heappush(heap, e)

        return len(heap)
