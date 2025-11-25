# LC 34. Find First and Last Position of Element in Sorted Array | Medium
class Solution:
    def searchRange(self, nums, target):
        def find(leftBias):
            l, r, idx = 0, len(nums) - 1, -1
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    idx = m
                    if leftBias: r = m - 1
                    else: l = m + 1
                elif nums[m] < target: l = m + 1
                else: r = m - 1
            return idx
        return [find(True), find(False)]
