from collections import defaultdict

class Solution:
    def countArrays(self, digitSums: list[int]) -> int:
        MOD = 10**9 + 7
        MAX_VAL = 2000

        by_sum = defaultdict(list)

        for v in range(MAX_VAL + 1):
            s = sum(map(int, str(v)))
            by_sum[s].append(v)

        dp = {v: 1 for v in by_sum[digitSums[0]]}

        for i in range(1, len(digitSums)):
            nxt = {}

            prev_vals = sorted(dp.keys())

            pref = 0
            idx = 0

            for v in sorted(by_sum[digitSums[i]]):
                while idx < len(prev_vals) and prev_vals[idx] <= v:
                    pref = (pref + dp[prev_vals[idx]]) % MOD
                    idx += 1

                nxt[v] = pref

            dp = nxt

        return sum(dp.values()) % MOD
