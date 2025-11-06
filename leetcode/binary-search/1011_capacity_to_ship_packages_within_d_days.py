class Solution:
    def shipWithinDays(self, weights, days):

        def possible(capacity):
            used_days = 1
            curr = 0

            for w in weights:
                if curr + w > capacity:
                    used_days += 1
                    curr = 0
                curr += w

            return used_days <= days

        l, r = max(weights), sum(weights)

        while l < r:
            m = (l + r) // 2

            if possible(m):
                r = m
            else:
                l = m + 1

        return l
