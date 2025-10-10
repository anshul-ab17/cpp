class Solution:
    def rotate(self, nums, k):
        k %= len(nums)

        # Reverse trick
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
