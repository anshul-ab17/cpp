# Sort + Min Heap for top k sums.
import heapq

class Solution:
    def maxScore(self, nums1, nums2, k):
        pairs = sorted(zip(nums2, nums1), reverse=True)
        heap = []
        total = 0
        best = 0

        for n2, n1 in pairs:
            heapq.heappush(heap, n1)
            total += n1
            if len(heap) > k:
                total -= heapq.heappop(heap)
            if len(heap) == k:
                best = max(best, total * n2)

        return best
