class Solution:
    def rob(self, nums):
        if len(nums) == 1: return nums[0]

        def helper(arr):
            a = b = 0
            for n in arr:
                a, b = b, max(b, a + n)
            return b

        return max(helper(nums[:-1]), helper(nums[1:]))
