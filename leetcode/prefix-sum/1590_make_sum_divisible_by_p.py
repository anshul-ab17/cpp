# Prefix modulo + hashmap.
class Solution:
    def minSubarray(self, nums, p):
        total = sum(nums) % p
        if total == 0:
            return 0

        n = len(nums)
        seen = {0: -1}
        cur = 0
        best = n

        for i, num in enumerate(nums):
            cur = (cur + num) % p
            need = (cur - total) % p
            if need in seen:
                best = min(best, i - seen[need])
            seen[cur] = i

        return best if best < n else -1
