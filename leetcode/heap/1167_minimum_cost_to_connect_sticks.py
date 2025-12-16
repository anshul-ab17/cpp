import heapq
class Solution:
    def connectSticks(self, sticks):
        heapq.heapify(sticks)
        cost = 0
        while len(sticks) > 1:
            a = heapq.heappop(sticks)
            b = heapq.heappop(sticks)
            cost += a + b
            heapq.heappush(sticks, a + b)
        return cost
