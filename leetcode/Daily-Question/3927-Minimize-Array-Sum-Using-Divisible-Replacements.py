class Solution:
    def minimizeArraySum(self, nums: list[int], k: int, maxOps: int) -> int:
        total = sum(nums)
        reductions = []

        for x in nums:
            if x > k and x % k == 0:
                reductions.append(x - k)

        reductions.sort(reverse=True)

        for i in range(min(maxOps, len(reductions))):
            total -= reductions[i]

        return total
