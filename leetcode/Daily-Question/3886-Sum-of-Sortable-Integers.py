class Solution:
    def sumSortableIntegers(self, low: str, high: str) -> int:
        MOD = 10**9 + 7

        def solve(s):
            memo = {}

            def dfs(idx, mask, last, tight, lead):
                if idx == len(s):
                    return (1, 0)

                state = (idx, mask, last, tight, lead)

                if state in memo:
                    return memo[state]

                upper = int(s[idx]) if tight else 9

                cnt = sm = 0

                for d in range(upper + 1):
                    ntight = tight and d == upper

                    if lead and d == 0:
                        c, ss = dfs(idx + 1, mask, -1, ntight, True)
                    else:
                        if d <= last or (mask & (1 << d)):
                            continue

                        c, ss = dfs(
                            idx + 1,
                            mask | (1 << d),
                            d,
                            ntight,
                            False
                        )

                        place = pow(10, len(s) - idx - 1, MOD)
                        ss = (ss + c * d * place) % MOD

                    cnt = (cnt + c) % MOD
                    sm = (sm + ss) % MOD

                memo[state] = (cnt, sm)
                return memo[state]

            return dfs(0, 0, -1, True, True)[1]

        return (solve(high) - solve(str(int(low) - 1))) % MOD
