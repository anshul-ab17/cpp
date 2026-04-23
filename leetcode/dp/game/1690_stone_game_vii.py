from functools import cache

class Solution:
    def stoneGameVII(self, stones):

        pref = [0]
        for s in stones:
            pref.append(pref[-1] + s)

        @cache
        def dfs(l, r):

            if l == r:
                return 0

            remove_left = pref[r+1] - pref[l+1]
            remove_right = pref[r] - pref[l]

            return max(
                remove_left - dfs(l + 1, r),
                remove_right - dfs(l, r - 1)
            )

        return dfs(0, len(stones)-1)
