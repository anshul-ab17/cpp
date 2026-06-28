class Solution:
    def minInversionCount(self, nums: list[int], k: int) -> int:
        n = len(nums)

        if k <= 1:
            return 0

        vals = sorted(set(nums))
        rank = {v: i + 1 for i, v in enumerate(vals)}
        MAX = len(vals)

        bit = [0] * (MAX + 1)

        def update(idx, delta):
            while idx <= MAX:
                bit[idx] += delta
                idx += idx & -idx

        def query(idx):
            s = 0
            while idx > 0:
                s += bit[idx]
                idx -= idx & -idx
            return s

        curr = 0

        for i in range(k):
            r = rank[nums[i]]
            curr += i - query(r)
            update(r, 1)

        ans = curr

        for i in range(n - k):
            out_rank = rank[nums[i]]
            update(out_rank, -1)
            curr -= query(out_rank - 1)

            in_rank = rank[nums[i + k]]
            curr += query(MAX) - query(in_rank)
            update(in_rank, 1)

            ans = min(ans, curr)

        return ans
