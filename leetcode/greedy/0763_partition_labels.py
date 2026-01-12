class Solution:
    def partitionLabels(self, s):
        last = {c:i for i,c in enumerate(s)}
        ans, size, end = [], 0, 0
        for i,c in enumerate(s):
            size += 1
            end = max(end, last[c])
            if i == end:
                ans.append(size)
                size = 0
        return ans
