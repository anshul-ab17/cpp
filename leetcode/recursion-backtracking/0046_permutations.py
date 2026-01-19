# LC 46. Permutations | Medium
class Solution:
    def permute(self, nums):
        res = []
        def bt(path, remaining):
            if not remaining: res.append(path[:]); return
            for i in range(len(remaining)):
                path.append(remaining[i])
                bt(path, remaining[:i] + remaining[i+1:])
                path.pop()
        bt([], nums); return res
