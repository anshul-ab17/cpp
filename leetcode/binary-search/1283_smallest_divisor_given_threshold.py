import math

class Solution:
    def smallestDivisor(self, nums, threshold):

        def valid(divisor):
            total = sum(math.ceil(x / divisor) for x in nums)
            return total <= threshold

        l, r = 1, max(nums)

        while l < r:
            m = (l + r) // 2

            if valid(m):
                r = m
            else:
                l = m + 1

        return l
