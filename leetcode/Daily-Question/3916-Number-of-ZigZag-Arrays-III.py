class Solution:
    def zigZagArraysIII(self, n: int, l: int, r: int, k_mod: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1
        states = 2 * m

        def multiply(A, B):
            C = [[0] * states for _ in range(states)]

            for i in range(states):
                for k in range(states):
                    if A[i][k] == 0:
                        continue

                    for j in range(states):
                        C[i][j] = (
                            C[i][j] + A[i][k] * B[k][j]
                        ) % MOD

            return C

        def power(base, exp):
            res = [[0] * states for _ in range(states)]

            for i in range(states):
                res[i][i] = 1

            while exp:
                if exp & 1:
                    res = multiply(res, base)

                base = multiply(base, base)
                exp >>= 1

            return res

        T = [[0] * states for _ in range(states)]

        for x in range(m):
            down = x
            up = x + m

            for y in range(x + 1, m):
                T[y][up] = 1

            for y in range(x):
                T[y + m][down] = 1

        T = power(T, n - 1)

        start = [1] * states
        ans = 0

        for i in range(states):
            cur = 0
            for j in range(states):
                cur = (cur + T[i][j] * start[j]) % MOD
            ans = (ans + cur) % MOD

        return ans
