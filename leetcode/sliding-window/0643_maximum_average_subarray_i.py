class Solution:
    def findMaxAverage(self, nums, k):
        cur = sum(nums[:k]); ans = cur
        for i in range(k, len(nums)):
            cur += nums[i] - nums[i-k]
            ans = max(ans, cur)
        return ans / k
