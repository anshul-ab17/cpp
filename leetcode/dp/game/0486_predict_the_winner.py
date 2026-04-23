from functools import cache

class Solution:
    def PredictTheWinner(self, nums):

        @cache
        def dfs(l, r):
            if l == r:
                return nums[l]

            return max(
                nums[l] - dfs(l + 1, r),
                nums[r] - dfs(l, r - 1)
            )

        return dfs(0, len(nums) - 1) >= 0
