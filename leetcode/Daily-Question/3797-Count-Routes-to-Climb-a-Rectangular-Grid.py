import math

class Solution:
    def countRoutes(self, grid: list[str], d: int) -> int:
        MOD = 10**9 + 7
        n = len(grid)
        m = len(grid[0])

        dp = [[0, 0] for _ in range(m)]

        for c in range(m):
            if grid[n - 1][c] == '.':
                dp[c][0] = 1

        def process_horizontal(row, cur):
            nxt = [x[:] for x in cur]

            for c1 in range(m):
                if grid[row][c1] == '#' or cur[c1][0] == 0:
                    continue

                for c2 in range(m):
                    if c1 == c2 or grid[row][c2] == '#':
                        continue

                    if abs(c1 - c2) <= d:
                        nxt[c2][1] = (nxt[c2][1] + cur[c1][0]) % MOD

            return nxt

        dp = process_horizontal(n - 1, dp)

        for r in range(n - 2, -1, -1):
            nxt = [[0, 0] for _ in range(m)]

            for c1 in range(m):
                total = (dp[c1][0] + dp[c1][1]) % MOD
                if total == 0:
                    continue

                for c2 in range(m):
                    if grid[r][c2] == '#':
                        continue

                    if 1 + (c1 - c2) ** 2 <= d * d:
                        nxt[c2][0] = (nxt[c2][0] + total) % MOD

            dp = process_horizontal(r, nxt)

        return sum((dp[c][0] + dp[c][1]) % MOD
                   for c in range(m) if grid[0][c] == '.') % MOD
