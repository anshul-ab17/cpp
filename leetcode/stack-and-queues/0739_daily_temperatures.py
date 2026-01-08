# LC 739. Daily Temperatures | Medium
class Solution:
    # Monotonic stack - O(n)
    def dailyTemperatures(self, temperatures):
        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                j = stack.pop(); res[j] = i - j
            stack.append(i)
        return res
