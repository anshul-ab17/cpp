from functools import cache

class Solution:
    def canPartitionKSubsets(self, nums, k):
        total = sum(nums)

        if total % k:
            return False

        target = total // k
        nums.sort(reverse=True)

        @cache
        def dfs(mask, cur_sum, groups):
            if groups == k - 1:
                return True

            if cur_sum == target:
                return dfs(mask, 0, groups + 1)

            for i in range(len(nums)):
                if mask & (1 << i):
                    continue

                if cur_sum + nums[i] > target:
                    continue

                if dfs(mask | (1 << i),
                       cur_sum + nums[i],
                       groups):
                    return True

            return False

        return dfs(0, 0, 0)
