# Hard: Prefix sums of prefix sums + Monotonic stack.
class Solution:
    def totalStrength(self, strength):
        MOD = 10 ** 9 + 7
        n = len(strength)

        prefix = [0] * (n + 1)
        for i, v in enumerate(strength):
            prefix[i + 1] = prefix[i] + v

        prefix_of_prefix = [0] * (n + 2)
        for i, v in enumerate(prefix):
            prefix_of_prefix[i + 1] = prefix_of_prefix[i] + v

        prev_less = [-1] * n
        stack = []
        for i in range(n):
            while stack and strength[stack[-1]] >= strength[i]:
                stack.pop()
            prev_less[i] = stack[-1] if stack else -1
            stack.append(i)

        next_less = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and strength[stack[-1]] > strength[i]:
                stack.pop()
            next_less[i] = stack[-1] if stack else n
            stack.append(i)

        total = 0
        for i in range(n):
            left, right = prev_less[i], next_less[i]
            right_sum = prefix_of_prefix[right + 1] - prefix_of_prefix[i + 1]
            left_sum = prefix_of_prefix[i + 1] - prefix_of_prefix[left + 1]
            right_count = right - i
            left_count = i - left
            contribution = (right_sum * left_count - left_sum * right_count) % MOD
            total = (total + strength[i] * contribution) % MOD

        return total % MOD
