class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        ans = []
        def dfs(start, cur, total):
            if total == target:
                ans.append(cur[:]); return
            if total > target: return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                cur.append(candidates[i])
                dfs(i + 1, cur, total + candidates[i])
                cur.pop()
        dfs(0, [], 0)
        return ans
