class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1: return 0
        prod = 1; l = ans = 0
        for r, x in enumerate(nums):
            prod *= x
            while prod >= k:
                prod //= nums[l]; l += 1
            ans += r - l + 1
        return ans
