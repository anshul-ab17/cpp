# Sliding Window + Prefix Sum.
class Solution:
    def getAverages(self, nums, k):
        n = len(nums)
        res = [-1] * n
        window = 2 * k + 1
        if window > n:
            return res

        prefix = [0] * (n + 1)
        for i, num in enumerate(nums):
            prefix[i + 1] = prefix[i] + num

        for i in range(k, n - k):
            total = prefix[i + k + 1] - prefix[i - k]
            res[i] = total // window

        return res
