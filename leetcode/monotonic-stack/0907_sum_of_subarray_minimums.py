# Find Previous Smaller + Next Smaller elements.
class Solution:
    def sumSubarrayMins(self, arr):
        MOD = 10 ** 9 + 7
        n = len(arr)
        prev_less = [-1] * n
        next_less = [n] * n
        stack = []

        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            prev_less[i] = stack[-1] if stack else -1
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            next_less[i] = stack[-1] if stack else n
            stack.append(i)

        total = 0
        for i in range(n):
            left = i - prev_less[i]
            right = next_less[i] - i
            total += arr[i] * left * right

        return total % MOD
