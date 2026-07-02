# Two min heaps / one heap with candidates from both ends.
import heapq

class Solution:
    def totalCost(self, costs, k, candidates):
        n = len(costs)
        left, right = 0, n - 1
        left_heap, right_heap = [], []
        total = 0

        for _ in range(k):
            while len(left_heap) < candidates and left <= right:
                heapq.heappush(left_heap, costs[left])
                left += 1
            while len(right_heap) < candidates and left <= right:
                heapq.heappush(right_heap, costs[right])
                right -= 1

            if left_heap and (not right_heap or left_heap[0] <= right_heap[0]):
                total += heapq.heappop(left_heap)
            else:
                total += heapq.heappop(right_heap)

        return total
