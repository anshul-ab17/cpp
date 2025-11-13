class Solution:
    def minDays(self, bloomDay, m, k):

        if m * k > len(bloomDay):
            return -1

        def possible(day):
            flowers = bouquets = 0

            for d in bloomDay:
                if d <= day:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0

            return bouquets >= m

        l, r = min(bloomDay), max(bloomDay)

        while l < r:
            mid = (l + r) // 2

            if possible(mid):
                r = mid
            else:
                l = mid + 1

        return l
