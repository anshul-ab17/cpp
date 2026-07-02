# Offline queries + Bit Trie.
class Solution:
    def maximizeXor(self, nums, queries):
        nums.sort()
        indexed_queries = sorted(range(len(queries)), key=lambda i: queries[i][1])
        res = [-1] * len(queries)

        root = {}
        BITS = 30

        def insert(num):
            node = root
            for i in range(BITS, -1, -1):
                bit = (num >> i) & 1
                node = node.setdefault(bit, {})

        def query_max(num):
            node = root
            cur = 0
            for i in range(BITS, -1, -1):
                bit = (num >> i) & 1
                want = 1 - bit
                if want in node:
                    cur = (cur << 1) | 1
                    node = node[want]
                else:
                    cur = cur << 1
                    node = node[bit]
            return cur

        i = 0
        n = len(nums)
        for qi in indexed_queries:
            x, m = queries[qi]
            while i < n and nums[i] <= m:
                insert(nums[i])
                i += 1
            if i > 0:
                res[qi] = query_max(x)

        return res
