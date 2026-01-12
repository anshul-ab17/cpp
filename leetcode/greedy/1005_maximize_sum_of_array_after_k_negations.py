class Solution:
    def largestSumAfterKNegations(self, nums, k):
        nums.sort()
        for i in range(len(nums)):
            if nums[i] < 0 and k:
                nums[i] *= -1
                k -= 1
        if k % 2:
            nums.sort()
            nums[0] *= -1
        return sum(nums)
