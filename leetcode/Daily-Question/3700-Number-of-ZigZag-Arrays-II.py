class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
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
                        if B[k][j] == 0:
                            continue
                        C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
            return C

        def power(base, exp):
            res = [[0] * states for _ in range(states)]
            for i in range(states):
                res[i][i] = 1

            while exp > 0:
                if exp & 1:
                    res = multiply(res, base)
                base = multiply(base, base)
                exp >>= 1

            return res

        T = [[0] * states for _ in range(states)]

        for x in range(m):
            down_state = x
            up_state = x + m

            for y in range(x + 1, m):
                T[y][up_state] = 1

            for y in range(x):
                T[y + m][down_state] = 1

        final_T = power(T, n - 1)
        start = [1] * states

        ans = 0
        for i in range(states):
            curr = 0
            for j in range(states):
                curr = (curr + final_T[i][j] * start[j]) % MOD
            ans = (ans + curr) % MOD

        return ans
