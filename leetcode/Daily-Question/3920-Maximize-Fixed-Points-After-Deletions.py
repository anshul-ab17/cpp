class Solution:
    def maxFixedPoints(self, nums: list[int], k: int) -> int:
        n = len(nums)

        dp = [[-1] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            val = nums[i - 1]

            for j in range(k + 1):
                if dp[i - 1][j] != -1:
                    fixed = 1 if val == i - j else 0
                    dp[i][j] = max(dp[i][j], dp[i - 1][j] + fixed)

                if j > 0 and dp[i - 1][j - 1] != -1:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1])

        return max(dp[n])
