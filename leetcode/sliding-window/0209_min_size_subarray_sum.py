# LC 209. Minimum Size Subarray Sum | Medium
class Solution:
    # Sliding window - O(n)
    def minSubArrayLen(self, target, nums):
        l, s, res = 0, 0, float('inf')
        for r in range(len(nums)):
            s += nums[r]
            while s >= target:
                res = min(res, r - l + 1)
                s -= nums[l]; l += 1
        return res if res != float('inf') else 0
