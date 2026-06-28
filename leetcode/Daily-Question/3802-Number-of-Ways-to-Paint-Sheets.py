class Solution:
    def paintingWays(self, m: int, n: int, k: int) -> int:
        MOD = 10**9 + 7

        profiles = []

        def generate(idx, cur):
            if idx == m:
                profiles.append(cur[:])
                return

            for color in range(k):
                if idx > 0 and color == cur[-1]:
                    continue

                cur.append(color)
                generate(idx + 1, cur)
                cur.pop()

        generate(0, [])

        sz = len(profiles)
        adj = [[] for _ in range(sz)]

        for i in range(sz):
            for j in range(sz):
                ok = True

                for r in range(m):
                    if profiles[i][r] == profiles[j][r]:
                        ok = False
                        break

                if ok:
                    adj[i].append(j)

        dp = [1] * sz

        for _ in range(1, n):
            ndp = [0] * sz

            for i in range(sz):
                if dp[i] == 0:
                    continue

                for nxt in adj[i]:
                    ndp[nxt] = (ndp[nxt] + dp[i]) % MOD

            dp = ndp

        return sum(dp) % MOD
