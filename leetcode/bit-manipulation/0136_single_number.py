# LC 136. Single Number | Easy
class Solution:
    def singleNumber_math(self, nums): return 2 * sum(set(nums)) - sum(nums)
    def singleNumber(self, nums):
        res = 0
        for n in nums: res ^= n
        return res
