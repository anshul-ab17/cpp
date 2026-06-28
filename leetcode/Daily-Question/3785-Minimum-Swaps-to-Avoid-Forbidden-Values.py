from collections import Counter
import math

class Solution:
    def minSwaps(self, nums: list[int], forbidden: list[int]) -> int:
        n = len(nums)

        freq_nums = Counter(nums)
        freq_forbidden = Counter(forbidden)

        for val, cnt in freq_nums.items():
            allowed = n - freq_forbidden[val]
            if cnt > allowed:
                return -1

        conflicts = 0
        conflict_freq = Counter()

        for i in range(n):
            if nums[i] == forbidden[i]:
                conflicts += 1
                conflict_freq[nums[i]] += 1

        if conflicts == 0:
            return 0

        mx = max(conflict_freq.values(), default=0)

        return max(mx, math.ceil(conflicts / 2))
