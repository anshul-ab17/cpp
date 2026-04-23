from functools import cache

class Solution:
    def stoneGameII(self, piles):

        suffix = piles[:]

        for i in range(len(piles)-2, -1, -1):
            suffix[i] += suffix[i+1]

        @cache
        def dfs(i, m):

            if i + 2 * m >= len(piles):
                return suffix[i]

            ans = 0

            for x in range(1, 2 * m + 1):
                ans = max(
                    ans,
                    suffix[i] - dfs(i + x, max(m, x))
                )

            return ans

        return dfs(0, 1)
