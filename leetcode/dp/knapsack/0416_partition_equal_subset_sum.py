# LC 416. Partition Equal Subset Sum | Medium (0/1 Knapsack)
class Solution:
    def canPartition(self, nums):
        total = sum(nums)
        if total % 2: return False
        target = total // 2; dp = {0}
        for n in nums:
            dp = dp | {s + n for s in dp}
            if target in dp: return True
        return target in dp
