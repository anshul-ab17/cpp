# Offline sort by x descending + monotonic stack on (y, sum).
from bisect import bisect_right

class Solution:
    def maximumSumQueries(self, nums1, nums2, queries):
        n = len(nums1)
        pairs = sorted(zip(nums1, nums2), reverse=True)
        indexed_queries = sorted(range(len(queries)), key=lambda i: -queries[i][0])

        res = [-1] * len(queries)
        stack = []  # increasing y, decreasing sum (monotonic on both)
        i = 0

        for qi in indexed_queries:
            x, y = queries[qi]
            while i < n and pairs[i][0] >= x:
                a, b = pairs[i]
                s = a + b
                while stack and stack[-1][1] <= s:
                    stack.pop()
                if not stack or stack[-1][0] < b:
                    stack.append((b, s))
                i += 1

            ys = [p[0] for p in stack]
            pos = bisect_right(ys, y - 1)
            # find first entry with y-value >= y (stack ys increasing)
            lo = 0
            hi = len(stack) - 1
            ans_idx = -1
            while lo <= hi:
                mid = (lo + hi) // 2
                if stack[mid][0] >= y:
                    ans_idx = mid
                    hi = mid - 1
                else:
                    lo = mid + 1
            if ans_idx != -1:
                res[qi] = stack[ans_idx][1]

        return res
