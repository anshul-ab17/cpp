# Prefix Sum + Monotonic Deque.
from collections import deque

class Solution:
    def shortestSubarray(self, nums, k):
        n = len(nums)
        prefix = [0] * (n + 1)
        for i, num in enumerate(nums):
            prefix[i + 1] = prefix[i] + num

        dq = deque()
        best = n + 1

        for i, cur in enumerate(prefix):
            while dq and cur - prefix[dq[0]] >= k:
                best = min(best, i - dq.popleft())
            while dq and prefix[dq[-1]] >= cur:
                dq.pop()
            dq.append(i)

        return best if best <= n else -1
