class Solution:
    def countCoprimeChoices(self, mat: list[list[int]]) -> int:
        MOD = 10**9 + 7
        m = len(mat)

        max_val = max(max(row) for row in mat)

        mu = [0] * (max_val + 1)
        mu[1] = 1
        visited = [False] * (max_val + 1)
        primes = []

        for i in range(2, max_val + 1):
            if not visited[i]:
                primes.append(i)
                mu[i] = -1

            for p in primes:
                if i * p > max_val:
                    break

                visited[i * p] = True

                if i % p == 0:
                    mu[i * p] = 0
                    break
                else:
                    mu[i * p] = -mu[i]

        divisor_counts = [[0] * (max_val + 1) for _ in range(m)]

        for i in range(m):
            for val in mat[i]:
                d = 1
                while d * d <= val:
                    if val % d == 0:
                        divisor_counts[i][d] += 1
                        if d * d != val:
                            divisor_counts[i][val // d] += 1
                    d += 1

        ans = 0

        for g in range(1, max_val + 1):
            if mu[g] == 0:
                continue

            combinations = 1
            for i in range(m):
                combinations = (combinations * divisor_counts[i][g]) % MOD

            if mu[g] == 1:
                ans = (ans + combinations) % MOD
            else:
                ans = (ans - combinations + MOD) % MOD

        return ans
