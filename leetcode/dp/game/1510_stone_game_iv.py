from functools import cache

class Solution:
    def winnerSquareGame(self, n):

        @cache
        def dfs(rem):
            if rem == 0:
                return False

            i = 1
            while i * i <= rem:
                if not dfs(rem - i * i):
                    return True
                i += 1

            return False

        return dfs(n)
