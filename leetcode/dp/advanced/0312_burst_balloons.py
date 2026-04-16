class Solution:
    def maxCoins(self, nums):
        nums = [1] + nums + [1]

        from functools import cache

        @cache
        def dfs(l, r):
            if l > r:
                return 0

            ans = 0

            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]

                ans = max(ans,
                          coins +
                          dfs(l, i - 1) +
                          dfs(i + 1, r))

            return ans

        return dfs(1, len(nums) - 2)
