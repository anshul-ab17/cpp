# Prefix Sum + Monotonic Stack.
class Solution:
    def maxSumMinProduct(self, nums):
        MOD = 10 ** 9 + 7
        n = len(nums)
        prefix = [0] * (n + 1)
        for i, num in enumerate(nums):
            prefix[i + 1] = prefix[i] + num

        prev_less = [-1] * n
        next_less = [n] * n
        stack = []

        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            prev_less[i] = stack[-1] if stack else -1
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            next_less[i] = stack[-1] if stack else n
            stack.append(i)

        best = 0
        for i in range(n):
            total = prefix[next_less[i]] - prefix[prev_less[i] + 1]
            best = max(best, total * nums[i])

        return best % MOD
