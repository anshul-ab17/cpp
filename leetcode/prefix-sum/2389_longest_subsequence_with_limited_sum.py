import bisect
class Solution:
    def answerQueries(self, nums, queries):
        nums.sort()
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]

        return [bisect.bisect_right(nums, q) for q in queries]
