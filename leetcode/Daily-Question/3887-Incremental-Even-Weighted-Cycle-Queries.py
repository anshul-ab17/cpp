class Solution:
    def evenCycleQueries(self, n: int, edges: list[list[int]]) -> list[bool]:
        parent = list(range(n))
        parity = [0] * n

        def find(x):
            if parent[x] == x:
                return x, 0

            root, p = find(parent[x])

            parent[x] = root
            parity[x] = (parity[x] + p) % 2

            return parent[x], parity[x]

        ans = []

        for u, v, w in edges:
            ru, pu = find(u)
            rv, pv = find(v)

            if ru != rv:
                parent[ru] = rv
                parity[ru] = (pv + (w % 2) + pu) % 2
                ans.append(False)
            else:
                ans.append((pu + pv + w) % 2 == 0)

        return ans
