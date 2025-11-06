class Solution:
    def findPeakElement(self, nums):
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2

            # move toward increasing slope
            if nums[m] > nums[m + 1]:
                r = m
            else:
                l = m + 1

        return l
