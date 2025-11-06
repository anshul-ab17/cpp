class Solution:
    def splitArray(self, nums, k):

        def feasible(limit):
            parts, curr = 1, 0

            for x in nums:
                if curr + x > limit:
                    parts += 1
                    curr = 0
                curr += x

            return parts <= k

        l, r = max(nums), sum(nums)

        while l < r:
            m = (l + r) // 2

            if feasible(m):
                r = m
            else:
                l = m + 1

        return l
