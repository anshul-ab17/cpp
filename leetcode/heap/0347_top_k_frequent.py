# LC 347. Top K Frequent Elements | Medium
from collections import Counter

class Solution:
    def topKFrequent_sort(self, nums, k):
        return [x for x, _ in Counter(nums).most_common(k)]

    # Bucket sort - O(n)
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items(): buckets[freq].append(num)
        res = []
        for i in range(len(buckets)-1, -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k: return res
        return res
