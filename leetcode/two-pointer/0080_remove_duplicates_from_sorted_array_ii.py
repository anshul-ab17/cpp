class Solution:
    def removeDuplicates(self, nums):
        k = 0
        for x in nums:
            if k < 2 or x != nums[k-2]:
                nums[k] = x; k += 1
        return k
