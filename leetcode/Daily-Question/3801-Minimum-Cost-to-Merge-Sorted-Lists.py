class Solution:
    def minCostMerge(self, lists: list[list[int]]) -> int:
        n = len(lists)

        merged = [[] for _ in range(1 << n)]
        length = [0] * (1 << n)
        median = [0] * (1 << n)

        for mask in range(1, 1 << n):
            lsb = mask & -mask
            idx = lsb.bit_length() - 1

            if mask == lsb:
                merged[mask] = lists[idx]
            else:
                prev = mask ^ lsb
                a = lists[idx]
                b = merged[prev]

                res = []
                i = j = 0

                while i < len(a) and j < len(b):
                    if a[i] <= b[j]:
                        res.append(a[i])
                        i += 1
                    else:
                        res.append(b[j])
                        j += 1

                res.extend(a[i:])
                res.extend(b[j:])
                merged[mask] = res

            length[mask] = len(merged[mask])

            if length[mask]:
                median[mask] = merged[mask][(length[mask] - 1) // 2]

        dp = [float('inf')] * (1 << n)

        for i in range(n):
            dp[1 << i] = 0

        for mask in range(1, 1 << n):
            if mask.bit_count() < 2:
                continue

            sub = (mask - 1) & mask

            while sub:
                comp = mask ^ sub

                if sub < comp:
                    cost = (
                        dp[sub]
                        + dp[comp]
                        + length[sub]
                        + length[comp]
                        + abs(median[sub] - median[comp])
                    )

                    dp[mask] = min(dp[mask], cost)

                sub = (sub - 1) & mask

        return dp[(1 << n) - 1]
