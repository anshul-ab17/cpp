from collections import defaultdict

class Solution:
    def sumPerfectSquareAncestors(self, n: int, edges: list[list[int]], nums: list[int]) -> int:
        def get_square_free(val):
            d = 2
            ans = 1
            temp = val

            while d * d <= temp:
                count = 0
                while temp % d == 0:
                    count += 1
                    temp //= d

                if count % 2:
                    ans *= d

                d += 1

            if temp > 1:
                ans *= temp

            return ans

        sq_free = [get_square_free(x) for x in nums]

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        total_pairs = 0
        path_counts = defaultdict(int)

        def dfs(node, parent):
            nonlocal total_pairs

            sf_val = sq_free[node]

            if node != 0:
                total_pairs += path_counts[sf_val]

            path_counts[sf_val] += 1

            for neighbor in adj[node]:
                if neighbor != parent:
                    dfs(neighbor, node)

            path_counts[sf_val] -= 1

        dfs(0, -1)

        return total_pairs
