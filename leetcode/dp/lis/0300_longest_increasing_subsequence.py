# LC 300. Longest Increasing Subsequence | Medium
import bisect

class Solution:
    # DP - O(n^2)
    def lengthOfLIS_dp(self, nums):
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]: dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

    # Patience sort - O(n log n)
    def lengthOfLIS(self, nums):
        tails = []
        for n in nums:
            pos = bisect.bisect_left(tails, n)
            if pos == len(tails): tails.append(n)
            else: tails[pos] = n
        return len(tails)
