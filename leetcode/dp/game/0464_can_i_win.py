from functools import cache

class Solution:
    def canIWin(self, maxChoosableInteger, desiredTotal):

        if desiredTotal <= 0:
            return True

        total = maxChoosableInteger * (maxChoosableInteger + 1) // 2

        if total < desiredTotal:
            return False

        @cache
        def dfs(mask, remain):

            for num in range(1, maxChoosableInteger + 1):

                if mask & (1 << num):
                    continue

                if num >= remain:
                    return True

                if not dfs(mask | (1 << num),
                           remain - num):
                    return True

            return False

        return dfs(0, desiredTotal)
