# LC 39. Combination Sum | Medium
class Solution:
    def combinationSum(self, candidates, target):
        res = []
        def bt(start, path, remain):
            if remain == 0: res.append(path[:]); return
            for i in range(start, len(candidates)):
                if candidates[i] > remain: break
                path.append(candidates[i]); bt(i, path, remain - candidates[i]); path.pop()
        candidates.sort(); bt(0, [], target); return res
