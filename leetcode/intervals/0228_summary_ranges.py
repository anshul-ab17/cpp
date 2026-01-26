class Solution:
    def summaryRanges(self, nums):
        ans = []
        i = 0

        while i < len(nums):
            start = nums[i]
            while i + 1 < len(nums) and nums[i+1] == nums[i] + 1:
                i += 1
            ans.append(str(start) if start == nums[i] else f"{start}->{nums[i]}")
            i += 1

        return ans
