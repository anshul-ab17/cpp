import sys
sys.setrecursionlimit(300000)

from collections import Counter

class Solution:
    def totalInteractionCost(self, n: int, edges: list[list[int]], group: list[int]) -> int:
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        total_group = Counter(group)
        ans = 0

        def dfs(node, parent):
            nonlocal ans

            cnt = Counter()
            cnt[group[node]] += 1

            for nei in adj[node]:
                if nei != parent:
                    child = dfs(nei, node)

                    for g, c in child.items():
                        ans += c * (total_group[g] - c)

                    cnt.update(child)

            return cnt

        dfs(0, -1)
        return ans
