class Solution:
    def maxSubArray(self, nums):
        cur = best = nums[0]

        for i in range(1, len(nums)):
            # Either extend or start fresh
            cur = max(nums[i], cur + nums[i])
            best = max(best, cur)

        return best
