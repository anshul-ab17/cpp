class Solution:
    def maxFrequency(self, nums, k):
        nums.sort(); l = total = ans = 0
        for r, x in enumerate(nums):
            total += x
            while x * (r-l+1) - total > k:
                total -= nums[l]; l += 1
            ans = max(ans, r-l+1)
        return ans
