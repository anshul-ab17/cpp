# Sort edges by max endpoint value + DSU tracking (max_val, count) per root.
class Solution:
    def numberOfGoodPaths(self, vals, edges):
        n = len(vals)
        parent = list(range(n))
        max_val = vals[:]
        count = [1] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        edges.sort(key=lambda e: max(vals[e[0]], vals[e[1]]))

        good_paths = n  # every single node is a trivial good path

        for u, v in edges:
            ru, rv = find(u), find(v)
            if ru == rv:
                continue
            if max_val[ru] == max_val[rv]:
                good_paths += count[ru] * count[rv]
                parent[rv] = ru
                count[ru] += count[rv]
            elif max_val[ru] > max_val[rv]:
                parent[rv] = ru
            else:
                parent[ru] = rv

        return good_paths
