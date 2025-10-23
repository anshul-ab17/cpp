class Solution:
    def longestSubarray(self, nums):
        l = zeros = 0
        for r, x in enumerate(nums):
            zeros += (x == 0)
            while zeros > 1:
                zeros -= (nums[l] == 0); l += 1
        return len(nums) - l - 1
