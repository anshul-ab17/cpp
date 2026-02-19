# LC 215. Kth Largest Element in an Array | Medium
import heapq

class Solution:
    def findKthLargest_sort(self, nums, k): return sorted(nums, reverse=True)[k-1]
    def findKthLargest(self, nums, k): return heapq.nlargest(k, nums)[-1]
