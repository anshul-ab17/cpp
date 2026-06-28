class Solution:
    def kthSmallestEven(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        from collections import defaultdict
        import bisect

        evens = []

        for i, x in enumerate(nums):
            if x % 2 == 0:
                evens.append((x, i))

        evens.sort()

        value_indices = defaultdict(list)

        for val, idx in evens:
            value_indices[val].append(idx)

        values = sorted(value_indices.keys())
        ans = []

        for L, R, k in queries:
            low, high = 0, len(values) - 1
            res = -1

            while low <= high:
                mid = (low + high) // 2

                cnt = 0
                for i in range(mid + 1):
                    idxs = value_indices[values[i]]
                    cnt += (
                        bisect.bisect_right(idxs, R)
                        - bisect.bisect_left(idxs, L)
                    )

                if cnt >= k:
                    res = values[mid]
                    high = mid - 1
                else:
                    low = mid + 1

            ans.append(res)

        return ans
