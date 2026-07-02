# Max Heap simulation.
import heapq
from math import ceil

class Solution:
    def maxKelements(self, nums, k):
        heap = [-x for x in nums]
        heapq.heapify(heap)
        score = 0

        for _ in range(k):
            top = -heapq.heappop(heap)
            score += top
            heapq.heappush(heap, -ceil(top / 3))

        return score
