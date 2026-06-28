class Solution:
    def minPartitionScore(self, nums: list[int], k: int) -> int:
        n = len(nums)

        pref = [0] * (n + 1)

        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        def cost(l, r):
            s = pref[r] - pref[l]
            return s * (s + 1) // 2

        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for j in range(1, k + 1):
            for i in range(j, n + 1):
                for p in range(j - 1, i):
                    dp[i][j] = min(
                        dp[i][j],
                        dp[p][j - 1] + cost(p, i)
                    )

        return dp[n][k]
