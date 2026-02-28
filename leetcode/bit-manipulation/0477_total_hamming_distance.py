class Solution:
    def totalHammingDistance(self, nums):
        ans = 0
        n = len(nums)

        for bit in range(32):
            ones = sum((x >> bit) & 1 for x in nums)
            ans += ones * (n - ones)

        return ans
