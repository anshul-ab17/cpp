# LC 268. Missing Number | Easy
class Solution:
    def missingNumber_math(self, nums):
        n = len(nums); return n*(n+1)//2 - sum(nums)
    def missingNumber(self, nums):
        res = len(nums)
        for i, n in enumerate(nums): res ^= i ^ n
        return res
