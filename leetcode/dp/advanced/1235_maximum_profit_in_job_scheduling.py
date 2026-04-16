from bisect import bisect_left
from functools import cache

class Solution:
    def jobScheduling(self, start, end, profit):
        jobs = sorted(zip(start, end, profit))

        starts = [s for s, _, _ in jobs]

        @cache
        def dfs(i):
            if i == len(jobs):
                return 0

            nxt = bisect_left(starts, jobs[i][1])

            skip = dfs(i + 1)
            take = jobs[i][2] + dfs(nxt)

            return max(skip, take)

        return dfs(0)
