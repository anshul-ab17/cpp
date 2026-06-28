from collections import defaultdict

class Solution:
    def sumOfBeautifulSubsequences(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        cnt = defaultdict(int)
        total = defaultdict(int)
        ans = 0

        for x in nums:
            ways = 1
            curr_sum = x

            if x - 1 in cnt:
                ways += cnt[x - 1]
                curr_sum += total[x - 1] + cnt[x - 1] * x

            if x + 1 in cnt:
                ways += cnt[x + 1]
                curr_sum += total[x + 1] + cnt[x + 1] * x

            ways %= MOD
            curr_sum %= MOD

            cnt[x] = (cnt[x] + ways) % MOD
            total[x] = (total[x] + curr_sum) % MOD

            ans = (ans + curr_sum) % MOD

        return ans
