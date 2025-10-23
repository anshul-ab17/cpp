class Solution:
    def longestOnes(self, nums, k):
        l = zeros = 0
        for r, x in enumerate(nums):
            zeros += (x == 0)
            if zeros > k:
                zeros -= (nums[l] == 0); l += 1
        return len(nums) - l
