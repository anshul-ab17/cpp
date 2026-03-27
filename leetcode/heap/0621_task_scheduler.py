# LC 621. Task Scheduler | Medium
from collections import Counter

class Solution:
    def leastInterval(self, tasks, n):
        freq = list(Counter(tasks).values())
        max_freq = max(freq)
        max_count = freq.count(max_freq)
        return max(len(tasks), (max_freq - 1) * (n + 1) + max_count)
