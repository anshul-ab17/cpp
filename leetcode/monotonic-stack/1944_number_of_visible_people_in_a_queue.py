# Decreasing monotonic stack.
class Solution:
    def canSeePersonsCount(self, heights):
        n = len(heights)
        res = [0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] < heights[i]:
                stack.pop()
                res[i] += 1
            if stack:
                res[i] += 1
            stack.append(i)

        return res
