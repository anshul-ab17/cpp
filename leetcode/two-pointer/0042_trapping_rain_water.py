# LC 42. Trapping Rain Water | Hard
class Solution:
    # Two pointers - O(n) time, O(1) space
    def trap(self, height):
        l, r = 0, len(height) - 1
        left_max = right_max = res = 0
        while l <= r:
            if left_max <= right_max:
                left_max = max(left_max, height[l])
                res += left_max - height[l]; l += 1
            else:
                right_max = max(right_max, height[r])
                res += right_max - height[r]; r -= 1
        return res
