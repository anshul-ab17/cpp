# Contribution technique using monotonic stack.
class Solution:
    def subArrayRanges(self, nums):
        n = len(nums)

        def sum_contribution(is_max):
            stack = []
            total = 0
            for i in range(n + 1):
                cur = nums[i] if i < n else (float('inf') if is_max else float('-inf'))
                while stack and (nums[stack[-1]] < cur if is_max else nums[stack[-1]] > cur):
                    j = stack.pop()
                    left = stack[-1] if stack else -1
                    total += nums[j] * (j - left) * (i - j)
                stack.append(i)
            return total

        return sum_contribution(True) - sum_contribution(False)
