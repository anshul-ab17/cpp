# LC 56. Merge Intervals | Medium | Google
class Solution:
    def merge(self, intervals):
        intervals.sort()
        res = [intervals[0]]
        for start, end in intervals[1:]:
            if start <= res[-1][1]: res[-1][1] = max(res[-1][1], end)
            else: res.append([start, end])
        return res
