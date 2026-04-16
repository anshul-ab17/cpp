from functools import cache

class Solution:
    def countArrangement(self, n):

        @cache
        def dfs(pos, mask):
            if pos > n:
                return 1

            ans = 0

            for num in range(1, n + 1):
                if mask & (1 << num):
                    continue

                if num % pos == 0 or pos % num == 0:
                    ans += dfs(pos + 1,
                               mask | (1 << num))

            return ans

        return dfs(1, 0)
