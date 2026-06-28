class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -1

        for i in range(n):
            for j in range(i + 1, n):
                if (nums[i] & nums[j]) == 0:
                    ans = max(ans, nums[i] * nums[j])

        return ans
