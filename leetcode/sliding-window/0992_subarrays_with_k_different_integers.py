from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, nums, k):
        def atMost(k):
            cnt = defaultdict(int); l = ans = 0
            for r, x in enumerate(nums):
                if cnt[x] == 0: k -= 1
                cnt[x] += 1
                while k < 0:
                    cnt[nums[l]] -= 1
                    if cnt[nums[l]] == 0: k += 1
                    l += 1
                ans += r - l + 1
            return ans
        return atMost(k) - atMost(k-1)
