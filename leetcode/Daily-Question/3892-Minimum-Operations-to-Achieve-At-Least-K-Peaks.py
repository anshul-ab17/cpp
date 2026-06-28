class Solution:
    def minOpsForPeaks(self, nums: list[int], k: int) -> int:
        n = len(nums)

        if k == 0:
            return 0

        if n < 3:
            return -1

        dp = [[[float('inf')] * 2 for _ in range(k + 1)]
              for _ in range(n)]

        dp[0][0][0] = 0
        dp[1][0][0] = 0

        for i in range(1, n - 1):
            for j in range(k + 1):

                dp[i][j][0] = min(
                    dp[i - 1][j][0],
                    dp[i - 1][j][1]
                )

                if j > 0:
                    need_left = max(0, nums[i - 1] + 1 - nums[i])
                    need_right = max(0, nums[i + 1] + 1 - nums[i])

                    cost = need_left + need_right

                    if dp[i - 1][j - 1][0] != float('inf'):
                        dp[i][j][1] = (
                            dp[i - 1][j - 1][0] + cost
                        )

        ans = min(
            min(dp[i][k][0], dp[i][k][1])
            for i in range(1, n - 1)
        )

        return ans if ans != float('inf') else -1
