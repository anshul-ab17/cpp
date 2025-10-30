class Solution:
    def minOperations(self, nums, x):
        target = sum(nums) - x
        if target < 0: return -1
        l = cur = best = 0
        best = -1
        for r, n in enumerate(nums):
            cur += n
            while cur > target and l <= r:
                cur -= nums[l]; l += 1
            if cur == target: best = max(best, r-l+1)
        return -1 if best == -1 else len(nums)-best
