# LC 11. Container With Most Water | Medium
class Solution:
    def maxArea_brute(self, height):
        res = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                res = max(res, min(height[i], height[j]) * (j - i))
        return res

    # Two pointers - O(n)
    def maxArea(self, height):
        l, r, res = 0, len(height) - 1, 0
        while l < r:
            res = max(res, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]: l += 1
            else: r -= 1
        return res
