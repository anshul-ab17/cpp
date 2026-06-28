class Solution:
    def mirrorPathCount(self, grid: List[str]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        dp = [[[0] * 2 for _ in range(n)] for _ in range(m)]
        dp[0][0][0] = dp[0][0][1] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                if i > 0:
                    if grid[i - 1][j] == '/':
                        dp[i][j][0] += dp[i - 1][j][1]
                    else:
                        dp[i][j][0] += dp[i - 1][j][0]

                if j > 0:
                    if grid[i][j - 1] == '/':
                        dp[i][j][1] += dp[i][j - 1][0]
                    else:
                        dp[i][j][1] += dp[i][j - 1][1]

                dp[i][j][0] %= MOD
                dp[i][j][1] %= MOD

        return (dp[m - 1][n - 1][0] +
                dp[m - 1][n - 1][1]) % MOD
