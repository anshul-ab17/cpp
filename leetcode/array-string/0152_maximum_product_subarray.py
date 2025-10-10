class Solution:
    def maxProduct(self, nums):
        cur_max = cur_min = ans = nums[0]

        for n in nums[1:]:
            tmp = cur_max * n

            cur_max = max(n, tmp, cur_min * n)
            cur_min = min(n, tmp, cur_min * n)

            ans = max(ans, cur_max)

        return ans
